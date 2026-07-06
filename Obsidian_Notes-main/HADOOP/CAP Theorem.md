# Laravel Task Management REST API — Full Build Guide

> **Stack:** Laravel 11 · Sanctum · Laravel Gates & Policies · MySQL  
> **Time:** 2–3 days  
> **Goal:** Mini Trello backend, interview-ready

---

## Prerequisites

Make sure these are installed on your machine:

- PHP >= 8.2
- Composer
- MySQL
- Postman (for testing)

---

## DAY 1 — Project Setup, Auth & Migrations

### Step 1 — Create Laravel Project

```bash
composer create-project laravel/laravel task-management-api
cd task-management-api
```

---

### Step 2 — Configure `.env`

Open `.env` and update the database section:

```env
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=task_management
DB_USERNAME=root
DB_PASSWORD=your_password
```

Create the database in MySQL:

```sql
CREATE DATABASE task_management;
```

---

### Step 3 — Install Laravel Sanctum

```bash
composer require laravel/sanctum
php artisan vendor:publish --provider="Laravel\Sanctum\SanctumServiceProvider"
```

---

### Step 4 — Define Gates in AppServiceProvider

This is where you define your authorization rules using Laravel's native Gate facade.  
No third-party package — just pure Laravel.

In `app/Providers/AppServiceProvider.php`:

```php
use Illuminate\Support\Facades\Gate;
use App\Models\User;

public function boot(): void
{
    // Anyone with role 'admin' passes this gate
    Gate::define('is-admin', function (User $user): bool {
        return $user->role === 'admin';
    });

    // Only the assigned member OR admin can update a task
    Gate::define('update-task-status', function (User $user, \App\Models\Task $task): bool {
        return $user->role === 'member' && $task->assigned_to === $user->id
            || $user->role === 'admin';
    });
}
```

> **Why Gates here and Policies later?**  
> Gates are for simple checks not tied to a specific model (`is-admin`).  
> Policies are for model-specific actions (`can I delete THIS project?`).  
> You'll use both — that's exactly what interviewers want to see.

---

### Step 5 — Create Migrations

#### Users table (modify the default one)

```bash
php artisan make:migration modify_users_table --table=users
```

Inside the migration `up()`:

```php
$table->string('role')->default('member'); // 'admin' or 'member'
```

#### Projects table

```bash
php artisan make:migration create_projects_table
```

Inside `up()`:

```php
Schema::create('projects', function (Blueprint $table) {
    $table->id();
    $table->string('name');
    $table->text('description')->nullable();
    $table->foreignId('created_by')->constrained('users')->onDelete('cascade');
    $table->timestamps();
});
```

#### Project–User pivot table

```bash
php artisan make:migration create_project_user_table
```

Inside `up()`:

```php
Schema::create('project_user', function (Blueprint $table) {
    $table->foreignId('project_id')->constrained()->onDelete('cascade');
    $table->foreignId('user_id')->constrained()->onDelete('cascade');
    $table->primary(['project_id', 'user_id']);
});
```

#### Tasks table

```bash
php artisan make:migration create_tasks_table
```

Inside `up()`:

```php
Schema::create('tasks', function (Blueprint $table) {
    $table->id();
    $table->string('title');
    $table->enum('status', ['todo', 'in_progress', 'done'])->default('todo');
    $table->foreignId('project_id')->constrained()->onDelete('cascade');
    $table->foreignId('assigned_to')->nullable()->constrained('users')->onDelete('set null');
    $table->timestamps();
});
```

#### Run all migrations

```bash
php artisan migrate
```

---

### Step 6 — Create Models

```bash
php artisan make:model Project
php artisan make:model Task
```

#### `app/Models/User.php`

```php
use HasApiTokens; // Sanctum only — no Spatie trait needed

protected $fillable = ['name', 'email', 'password', 'role'];

// Helper method — use this anywhere in your app
public function isAdmin(): bool
{
    return $this->role === 'admin';
}

public function projects(): BelongsToMany
{
    return $this->belongsToMany(Project::class);
}

public function tasks(): HasMany
{
    return $this->hasMany(Task::class, 'assigned_to');
}
```

#### `app/Models/Project.php`

```php
protected $fillable = ['name', 'description', 'created_by'];

public function members(): BelongsToMany
{
    return $this->belongsToMany(User::class);
}

public function tasks(): HasMany
{
    return $this->hasMany(Task::class);
}

public function creator(): BelongsTo
{
    return $this->belongsTo(User::class, 'created_by');
}
```

#### `app/Models/Task.php`

```php
protected $fillable = ['title', 'status', 'project_id', 'assigned_to'];

public function project(): BelongsTo
{
    return $this->belongsTo(Project::class);
}

public function assignee(): BelongsTo
{
    return $this->belongsTo(User::class, 'assigned_to');
}
```

---

### Step 7 — Create Policies

```bash
php artisan make:policy ProjectPolicy --model=Project
php artisan make:policy TaskPolicy --model=Task
```

#### `app/Policies/ProjectPolicy.php`

```php
public function viewAny(User $user): bool
{
    return $user->isAdmin();
}

public function create(User $user): bool
{
    return $user->isAdmin();
}

public function delete(User $user, Project $project): bool
{
    // Only the admin who created it can delete it
    return $user->isAdmin() && $project->created_by === $user->id;
}

public function assignMember(User $user): bool
{
    return $user->isAdmin();
}
```

#### `app/Policies/TaskPolicy.php`

```php
public function create(User $user): bool
{
    return $user->isAdmin();
}

public function updateStatus(User $user, Task $task): bool
{
    // Assigned member OR any admin can update the status
    return $user->role === 'member' && $task->assigned_to === $user->id
        || $user->isAdmin();
}
```

> Laravel **auto-discovers** policies when the model and policy names match.  
> `Project` → `ProjectPolicy`, `Task` → `TaskPolicy`. No manual registration needed in Laravel 11.

---

### Step 8 — Create Auth Controller

```bash
php artisan make:controller Api/AuthController
```

Methods to implement in `AuthController.php`:

```php
// register() — validate input, create user, return token
// login()    — validate credentials, return token
// logout()   — revoke current token
```

**register logic:**

```php
$user = User::create([
    'name'     => $request->name,
    'email'    => $request->email,
    'password' => Hash::make($request->password),
    'role'     => $request->role ?? 'member', // just save it to the column
]);

$token = $user->createToken('auth_token')->plainTextToken;

return response()->json(['token' => $token], 201);
```

**login logic:**

```php
if (!Auth::attempt($request->only('email', 'password'))) {
    return response()->json(['message' => 'Invalid credentials'], 401);
}

$user = User::where('email', $request->email)->first();
$token = $user->createToken('auth_token')->plainTextToken;

return response()->json(['token' => $token]);
```

**logout logic:**

```php
$request->user()->currentAccessToken()->delete();
return response()->json(['message' => 'Logged out']);
```

---

### Step 9 — Register Auth Routes

In `routes/api.php`:

```php
use App\Http\Controllers\Api\AuthController;

Route::post('/register', [AuthController::class, 'register']);
Route::post('/login',    [AuthController::class, 'login']);

Route::middleware('auth:sanctum')->post('/logout', [AuthController::class, 'logout']);
```

### Step 10 — Test Auth in Postman

```
POST /api/register     { name, email, password, role }
POST /api/login        { email, password }
POST /api/logout       Header: Authorization: Bearer {token}
```

---

## DAY 2 — Projects, Tasks & Authorization

### Step 11 — Create Controllers

```bash
php artisan make:controller Api/ProjectController --resource
php artisan make:controller Api/TaskController --resource
```

---

### Step 12 — Project Routes

All project routes are behind `auth:sanctum`. The **authorization** (who can do what) is handled inside the controller via `$this->authorize()` — not in the route file.

In `routes/api.php`:

```php
use App\Http\Controllers\Api\ProjectController;

Route::middleware('auth:sanctum')->group(function () {
    Route::get('/projects',                   [ProjectController::class, 'index']);
    Route::post('/projects',                  [ProjectController::class, 'store']);
    Route::delete('/projects/{project}',      [ProjectController::class, 'destroy']);
    Route::post('/projects/{project}/assign', [ProjectController::class, 'assignMember']);
});
```

---

### Step 13 — ProjectController Logic

```php
public function index()
{
    $this->authorize('viewAny', Project::class);

    return ProjectResource::collection(
        Project::with(['members', 'creator'])->get()
    );
}

public function store(StoreProjectRequest $request)
{
    $this->authorize('create', Project::class);

    $project = Project::create([
        'name'        => $request->name,
        'description' => $request->description,
        'created_by'  => $request->user()->id,
    ]);

    return new ProjectResource($project);
}

public function destroy(Project $project)
{
    $this->authorize('delete', $project); // passes the model instance

    $project->delete();
    return response()->json(['message' => 'Project deleted']);
}

public function assignMember(Request $request, Project $project)
{
    $this->authorize('assignMember', $project);

    $request->validate(['user_id' => 'required|exists:users,id']);

    $project->members()->syncWithoutDetaching([$request->user_id]);
    return response()->json(['message' => 'Member assigned']);
}
```

> `$this->authorize()` automatically returns a **403 JSON response** if the policy returns false.  
> No manual if-checks needed — Laravel handles it.

---

### Step 14 — Task Routes

```php
use App\Http\Controllers\Api\TaskController;

Route::middleware('auth:sanctum')->group(function () {
    Route::get('/tasks',                 [TaskController::class, 'index']);
    Route::post('/tasks',                [TaskController::class, 'store']);
    Route::patch('/tasks/{task}/status', [TaskController::class, 'updateStatus']);
});
```

---

### Step 15 — TaskController Logic

```php
public function index(Request $request)
{
    // Both admin and member can list tasks — no authorization check needed here
    $tasks = Task::query()
        ->when($request->status, fn($q) => $q->where('status', $request->status))
        ->with(['project', 'assignee'])
        ->paginate(10);

    return TaskResource::collection($tasks);
}

public function store(StoreTaskRequest $request)
{
    $this->authorize('create', Task::class);

    $task = Task::create($request->validated());
    return new TaskResource($task);
}

public function updateStatus(Request $request, Task $task)
{
    $this->authorize('updateStatus', $task); // passes task to TaskPolicy@updateStatus

    $request->validate([
        'status' => 'required|in:todo,in_progress,done',
    ]);

    $task->update(['status' => $request->status]);
    return new TaskResource($task);
}
```

---

### Step 16 — Create Form Requests (Validation)

```bash
php artisan make:request StoreProjectRequest
php artisan make:request StoreTaskRequest
```

In `StoreProjectRequest.php`:

```php
// Keep authorize() as true — policy checks live in the controller
public function authorize(): bool
{
    return true;
}

public function rules(): array
{
    return [
        'name'        => 'required|string|max:255',
        'description' => 'nullable|string',
    ];
}
```

In `StoreTaskRequest.php`:

```php
public function authorize(): bool
{
    return true;
}

public function rules(): array
{
    return [
        'title'       => 'required|string|max:255',
        'project_id'  => 'required|exists:projects,id',
        'assigned_to' => 'nullable|exists:users,id',
    ];
}
```

---

## DAY 3 — API Resources, Testing & README

### Step 17 — Create API Resources

```bash
php artisan make:resource UserResource
php artisan make:resource ProjectResource
php artisan make:resource TaskResource
```

#### `TaskResource.php`

```php
public function toArray(Request $request): array
{
    return [
        'id'          => $this->id,
        'title'       => $this->title,
        'status'      => $this->status,
        'project'     => $this->whenLoaded('project', fn() => [
            'id'   => $this->project->id,
            'name' => $this->project->name,
        ]),
        'assigned_to' => $this->whenLoaded('assignee', fn() => [
            'id'   => $this->assignee?->id,
            'name' => $this->assignee?->name,
        ]),
        'created_at'  => $this->created_at->toDateTimeString(),
    ];
}
```

#### `ProjectResource.php`

```php
public function toArray(Request $request): array
{
    return [
        'id'          => $this->id,
        'name'        => $this->name,
        'description' => $this->description,
        'created_by'  => $this->whenLoaded('creator', fn() => $this->creator->name),
        'members'     => UserResource::collection($this->whenLoaded('members')),
    ];
}
```

#### `UserResource.php`

```php
public function toArray(Request $request): array
{
    return [
        'id'   => $this->id,
        'name' => $this->name,
        'role' => $this->role,
    ];
}
```

---

### Step 18 — Final Postman Testing Checklist

|#|Test|Expected|
|---|---|---|
|1|Register admin user|201 + token|
|2|Register member user|201 + token|
|3|Login|200 + token|
|4|Create project (admin token)|201|
|5|Create project (member token)|403 Forbidden|
|6|Assign member to project (admin)|200|
|7|Create task (admin)|201|
|8|List tasks with `?status=todo`|200 + filtered list|
|9|Update task status (assigned member)|200|
|10|Update task status (non-assigned member)|403|
|11|Logout|200|

---

### Step 19 — Write Your README.md

Your `README.md` should include these sections:

```
# Task Management API

## About
## Tech Stack
## Installation & Setup
## Environment Variables
## API Endpoints (with example request/response)
## ER Diagram
## Roles & Permissions
```

#### ER Diagram (paste this as ASCII in README)

```
users
├── id
├── name
├── email
├── password
└── role (admin | member)
      │
      │  project_user (pivot)
      ├──────────────────── projects
      │                     ├── id
      │                     ├── name
      │                     ├── description
      │                     └── created_by → users.id
      │
tasks
├── id
├── title
├── status (todo | in_progress | done)
├── project_id → projects.id
└── assigned_to → users.id
```

#### Example endpoint docs block:

```markdown
### POST /api/register
**Body:**
\`\`\`json
{ "name": "Ali", "email": "ali@example.com", "password": "password", "role": "admin" }
\`\`\`
**Response:**
\`\`\`json
{ "token": "1|abc123..." }
\`\`\`
```

---

## Quick Reference — All Commands

```bash
# New project
composer create-project laravel/laravel task-management-api

# Packages (Sanctum only — no Spatie)
composer require laravel/sanctum
php artisan vendor:publish --provider="Laravel\Sanctum\SanctumServiceProvider"

# Generate migrations
php artisan make:migration modify_users_table --table=users
php artisan make:migration create_projects_table
php artisan make:migration create_project_user_table
php artisan make:migration create_tasks_table

# Generate models
php artisan make:model Project
php artisan make:model Task

# Generate policies
php artisan make:policy ProjectPolicy --model=Project
php artisan make:policy TaskPolicy --model=Task

# Generate controllers
php artisan make:controller Api/AuthController
php artisan make:controller Api/ProjectController --resource
php artisan make:controller Api/TaskController --resource

# Generate form requests
php artisan make:request StoreProjectRequest
php artisan make:request StoreTaskRequest

# Generate API resources
php artisan make:resource UserResource
php artisan make:resource ProjectResource
php artisan make:resource TaskResource

# Run migrations
php artisan migrate

# Serve
php artisan serve
```

---

## Common Gotchas

- **Sanctum guards:** Always use `auth:sanctum` on protected routes, not just `auth`
- **`$this->authorize()` argument types:** For model-specific policies pass the instance (`$this->authorize('delete', $project)`). For non-instance checks pass the class string (`$this->authorize('create', Project::class)`)
- **Policy auto-discovery:** Laravel 11 auto-discovers policies — no manual registration needed as long as the model and policy names match
- **`isAdmin()` helper:** That method on the User model is reusable everywhere — inside policies, gates, and controllers. Don't repeat `$user->role === 'admin'` raw all over the place
- **API responses:** Always return API Resources — raw Eloquent models expose hidden fields
- **Pivot table naming:** Laravel expects `project_user` (alphabetical, singular) — don't rename it

---

_Good luck bro. Ship it clean._