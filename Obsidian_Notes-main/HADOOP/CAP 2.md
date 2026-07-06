# Task Management — Frontend Guide

> **Focus:** What data goes out, what comes back, how to wire it up  
> **Stack:** Plain HTML + Vanilla JS (no framework, no build tools, just open in browser)  
> **Forget:** CSS, styling, animations — none of that matters here

---

## How This Frontend Works

You have a Laravel API running at `http://localhost:8000`.  
Your frontend is just HTML files you open in the browser.  
They talk to each other via `fetch()`.

The only thing you need to manage manually is the **token**.  
After login, you get a token. You store it. You send it with every request after that.

```
Browser                          Laravel API
  │                                   │
  │  POST /api/login                  │
  │  { email, password }  ──────────► │
  │                                   │  checks credentials
  │  ◄──────────────────  { token }   │
  │                                   │
  │  store token in localStorage      │
  │                                   │
  │  GET /api/projects                │
  │  Authorization: Bearer {token} ──►│
  │                                   │  checks token → finds user → runs policy
  │  ◄──────  { data: [...projects] } │
```

---

## Setup — Two Things Only

**1. Enable CORS in Laravel**

Your frontend is on a different origin than the API, so Laravel needs to allow it.

In `config/cors.php`:

```php
'allowed_origins' => ['*'], // during dev only
'allowed_methods' => ['*'],
'allowed_headers' => ['*'],
```

**2. Your file structure**

```
frontend/
├── index.html       ← login page
├── dashboard.html   ← projects list (admin)
├── tasks.html       ← tasks list (admin + member)
└── js/
    └── api.js       ← all your fetch calls live here
```

Open files directly in the browser or use VS Code Live Server.

---

## The Token — Understand This First

Every page needs to check if a token exists. If not, redirect to login.

```js
// js/api.js

const BASE_URL = 'http://localhost:8000/api';

// Save token after login
function saveToken(token) {
    localStorage.setItem('token', token);
}

// Read token on every request
function getToken() {
    return localStorage.getItem('token');
}

// Clear token on logout
function clearToken() {
    localStorage.removeItem('token');
}

// Guard — call this at top of every page except login
function requireAuth() {
    if (!getToken()) {
        window.location.href = 'index.html';
    }
}

// The base fetch wrapper — attaches token automatically
async function apiFetch(endpoint, options = {}) {
    const response = await fetch(`${BASE_URL}${endpoint}`, {
        ...options,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${getToken()}`,
            'Accept': 'application/json',
            ...options.headers,
        },
    });

    const data = await response.json();

    if (response.status === 401) {
        // Token expired or invalid
        clearToken();
        window.location.href = 'index.html';
    }

    return { status: response.status, data };
}
```

> **Why `Accept: application/json`?**  
> Without it, Laravel returns an HTML redirect on auth failures instead of a JSON 401.  
> Always include it.

---

## Page 1 — index.html (Login)

### What this page does

- Shows email + password inputs
- On submit: sends POST to `/api/login`
- On success: saves token, redirects to dashboard
- On failure: shows error message

### What you send

```
POST /api/login
Content-Type: application/json

{
    "email": "admin@example.com",
    "password": "password"
}
```

### What you get back

**Success (200):**

```json
{
    "token": "1|abc123xyz..."
}
```

**Failure (401):**

```json
{
    "message": "Invalid credentials"
}
```

### The HTML

```html
<!-- index.html -->
<h1>Login</h1>

<input type="email"    id="email"    placeholder="Email" />
<input type="password" id="password" placeholder="Password" />
<button id="loginBtn">Login</button>
<p id="error"></p>

<script src="js/api.js"></script>
<script>
    document.getElementById('loginBtn').addEventListener('click', async () => {
        const email    = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        const { status, data } = await apiFetch('/login', {
            method: 'POST',
            body: JSON.stringify({ email, password }),
        });

        if (status === 200) {
            saveToken(data.token);
            window.location.href = 'dashboard.html';
        } else {
            document.getElementById('error').textContent = data.message;
        }
    });
</script>
```

---

## Page 2 — dashboard.html (Projects — Admin)

### What this page does

- On load: fetches all projects, renders them
- Has a form to create a new project
- Has a button per project to assign a member
- Has a button per project to delete it
- Has a logout button

### What you send / get for each action

---

#### GET /api/projects

```
GET /api/projects
Authorization: Bearer {token}
```

**What you get back (200):**

```json
{
    "data": [
        {
            "id": 1,
            "name": "Website Redesign",
            "description": "Redesign the company website",
            "created_by": "John Admin",
            "members": [
                { "id": 2, "name": "Ali Member", "role": "member" }
            ]
        }
    ]
}
```

> The `data` wrapper comes from your API Resource.  
> Always access `response.data.data` — the first `.data` is your fetch result, second `.data` is the API Resource array.

---

#### POST /api/projects

```
POST /api/projects
Authorization: Bearer {token}
Content-Type: application/json

{
    "name": "New Project",
    "description": "Optional description"
}
```

**What you get back (201):**

```json
{
    "data": {
        "id": 2,
        "name": "New Project",
        "description": "Optional description",
        "created_by": "John Admin",
        "members": []
    }
}
```

**If member tries this (403):**

```json
{
    "message": "This action is unauthorized."
}
```

---

#### POST /api/projects/{id}/assign

```
POST /api/projects/1/assign
Authorization: Bearer {token}
Content-Type: application/json

{
    "user_id": 3
}
```

**What you get back (200):**

```json
{
    "message": "Member assigned"
}
```

---

#### DELETE /api/projects/{id}

```
DELETE /api/projects/1
Authorization: Bearer {token}
```

**What you get back (200):**

```json
{
    "message": "Project deleted"
}
```

---

### The HTML

```html
<!-- dashboard.html -->
<h1>Projects</h1>
<button id="logoutBtn">Logout</button>

<h2>Create Project</h2>
<input type="text" id="projectName"        placeholder="Project name" />
<input type="text" id="projectDescription" placeholder="Description" />
<button id="createProjectBtn">Create</button>

<h2>All Projects</h2>
<div id="projectsList"></div>

<script src="js/api.js"></script>
<script>
    requireAuth(); // redirect to login if no token

    // Load projects on page load
    async function loadProjects() {
        const { status, data } = await apiFetch('/projects');

        if (status === 403) {
            document.getElementById('projectsList').textContent = 'Admins only.';
            return;
        }

        const projects = data.data; // unwrap API Resource
        const container = document.getElementById('projectsList');
        container.innerHTML = '';

        projects.forEach(project => {
            const div = document.createElement('div');
            div.innerHTML = `
                <h3>${project.name}</h3>
                <p>${project.description ?? 'No description'}</p>
                <p>Members: ${project.members.map(m => m.name).join(', ') || 'None'}</p>
                <input type="number" id="assignUser-${project.id}" placeholder="User ID to assign" />
                <button onclick="assignMember(${project.id})">Assign Member</button>
                <button onclick="deleteProject(${project.id})">Delete</button>
                <hr />
            `;
            container.appendChild(div);
        });
    }

    // Create project
    document.getElementById('createProjectBtn').addEventListener('click', async () => {
        const name        = document.getElementById('projectName').value;
        const description = document.getElementById('projectDescription').value;

        const { status, data } = await apiFetch('/projects', {
            method: 'POST',
            body: JSON.stringify({ name, description }),
        });

        if (status === 201) {
            loadProjects(); // refresh list
        } else {
            alert(data.message);
        }
    });

    // Assign member
    async function assignMember(projectId) {
        const userId = document.getElementById(`assignUser-${projectId}`).value;

        const { status, data } = await apiFetch(`/projects/${projectId}/assign`, {
            method: 'POST',
            body: JSON.stringify({ user_id: userId }),
        });

        alert(status === 200 ? data.message : data.message);
        loadProjects();
    }

    // Delete project
    async function deleteProject(projectId) {
        const { status, data } = await apiFetch(`/projects/${projectId}`, {
            method: 'DELETE',
        });

        if (status === 200) {
            loadProjects();
        } else {
            alert(data.message);
        }
    }

    // Logout
    document.getElementById('logoutBtn').addEventListener('click', async () => {
        await apiFetch('/logout', { method: 'POST' });
        clearToken();
        window.location.href = 'index.html';
    });

    loadProjects();
</script>
```

---

## Page 3 — tasks.html (Tasks — Admin + Member)

### What this page does

- On load: fetches all tasks
- Supports filtering by status via `?status=todo` query param
- Admin can see a form to create a task
- Member can update task status via dropdown
- Both see the same list

### What you send / get for each action

---

#### GET /api/tasks

```
GET /api/tasks
Authorization: Bearer {token}
```

**With filter:**

```
GET /api/tasks?status=todo
```

**What you get back (200):**

```json
{
    "data": [
        {
            "id": 1,
            "title": "Design homepage",
            "status": "todo",
            "project": { "id": 1, "name": "Website Redesign" },
            "assigned_to": { "id": 2, "name": "Ali Member" },
            "created_at": "2025-04-01 10:00:00"
        }
    ],
    "links": { ... },
    "meta": { "current_page": 1, "last_page": 3, "total": 25 }
}
```

> Pagination is included because you used `->paginate(10)`.  
> `meta.total` tells you how many tasks exist.  
> `links.next` gives you the URL to the next page.

---

#### POST /api/tasks

```
POST /api/tasks
Authorization: Bearer {token}
Content-Type: application/json

{
    "title": "Design homepage",
    "project_id": 1,
    "assigned_to": 2
}
```

**What you get back (201):**

```json
{
    "data": {
        "id": 1,
        "title": "Design homepage",
        "status": "todo",
        "project": { "id": 1, "name": "Website Redesign" },
        "assigned_to": { "id": 2, "name": "Ali Member" },
        "created_at": "2025-04-01 10:00:00"
    }
}
```

---

#### PATCH /api/tasks/{id}/status

```
PATCH /api/tasks/1/status
Authorization: Bearer {token}
Content-Type: application/json

{
    "status": "in_progress"
}
```

**Allowed values:** `todo` | `in_progress` | `done`

**What you get back (200):**

```json
{
    "data": {
        "id": 1,
        "title": "Design homepage",
        "status": "in_progress",
        ...
    }
}
```

**If non-assigned member tries this (403):**

```json
{
    "message": "This action is unauthorized."
}
```

---

### The HTML

```html
<!-- tasks.html -->
<h1>Tasks</h1>
<button id="logoutBtn">Logout</button>

<!-- Filter -->
<select id="statusFilter">
    <option value="">All statuses</option>
    <option value="todo">Todo</option>
    <option value="in_progress">In Progress</option>
    <option value="done">Done</option>
</select>
<button id="filterBtn">Filter</button>

<!-- Create task (admin only — hide this for members in real app) -->
<h2>Create Task</h2>
<input type="text"   id="taskTitle"     placeholder="Task title" />
<input type="number" id="taskProjectId" placeholder="Project ID" />
<input type="number" id="taskAssignTo"  placeholder="Assign to User ID" />
<button id="createTaskBtn">Create Task</button>

<!-- Task list -->
<div id="tasksList"></div>

<!-- Pagination -->
<button id="prevPage" disabled>Previous</button>
<span id="pageInfo"></span>
<button id="nextPage">Next</button>

<script src="js/api.js"></script>
<script>
    requireAuth();

    let currentPage = 1;

    async function loadTasks(page = 1) {
        const status     = document.getElementById('statusFilter').value;
        const statusParam = status ? `&status=${status}` : '';

        const { status: httpStatus, data } = await apiFetch(`/tasks?page=${page}${statusParam}`);

        const tasks     = data.data;
        const meta      = data.meta;
        const container = document.getElementById('tasksList');
        container.innerHTML = '';

        tasks.forEach(task => {
            const div = document.createElement('div');
            div.innerHTML = `
                <strong>${task.title}</strong>
                — Status: <em>${task.status}</em>
                — Project: ${task.project?.name ?? 'N/A'}
                — Assigned to: ${task.assigned_to?.name ?? 'Unassigned'}
                <br/>
                <select id="statusSelect-${task.id}">
                    <option value="todo"        ${task.status === 'todo'        ? 'selected' : ''}>Todo</option>
                    <option value="in_progress" ${task.status === 'in_progress' ? 'selected' : ''}>In Progress</option>
                    <option value="done"        ${task.status === 'done'        ? 'selected' : ''}>Done</option>
                </select>
                <button onclick="updateStatus(${task.id})">Update Status</button>
                <hr/>
            `;
            container.appendChild(div);
        });

        // Pagination controls
        currentPage = meta.current_page;
        document.getElementById('pageInfo').textContent = `Page ${meta.current_page} of ${meta.last_page}`;
        document.getElementById('prevPage').disabled = meta.current_page <= 1;
        document.getElementById('nextPage').disabled = meta.current_page >= meta.last_page;
    }

    // Update task status
    async function updateStatus(taskId) {
        const status = document.getElementById(`statusSelect-${taskId}`).value;

        const { status: httpStatus, data } = await apiFetch(`/tasks/${taskId}/status`, {
            method: 'PATCH',
            body: JSON.stringify({ status }),
        });

        if (httpStatus === 200) {
            loadTasks(currentPage);
        } else {
            alert(data.message); // 403 if not authorized
        }
    }

    // Create task
    document.getElementById('createTaskBtn').addEventListener('click', async () => {
        const title      = document.getElementById('taskTitle').value;
        const project_id = document.getElementById('taskProjectId').value;
        const assigned_to = document.getElementById('taskAssignTo').value;

        const { status, data } = await apiFetch('/tasks', {
            method: 'POST',
            body: JSON.stringify({ title, project_id, assigned_to }),
        });

        if (status === 201) {
            loadTasks(currentPage);
        } else {
            alert(JSON.stringify(data)); // show validation errors
        }
    });

    document.getElementById('filterBtn').addEventListener('click', () => loadTasks(1));
    document.getElementById('prevPage').addEventListener('click', () => loadTasks(currentPage - 1));
    document.getElementById('nextPage').addEventListener('click', () => loadTasks(currentPage + 1));

    document.getElementById('logoutBtn').addEventListener('click', async () => {
        await apiFetch('/logout', { method: 'POST' });
        clearToken();
        window.location.href = 'index.html';
    });

    loadTasks();
</script>
```

---

## Understanding Validation Errors

When you send bad data, Laravel returns a 422 with this shape:

```json
{
    "message": "The title field is required.",
    "errors": {
        "title": ["The title field is required."],
        "project_id": ["The selected project id is invalid."]
    }
}
```

To show these properly instead of just `alert(data.message)`:

```js
function showErrors(errors) {
    // errors is the data.errors object
    return Object.values(errors).flat().join('\n');
}

// Usage:
if (status === 422) {
    alert(showErrors(data.errors));
}
```

---

## What Each HTTP Status Means in This App

|Status|Means|What to do in frontend|
|---|---|---|
|200|OK|Use the data|
|201|Created|Refresh the list|
|401|Unauthenticated|Clear token, redirect to login|
|403|Unauthorized (policy denied)|Show "You don't have permission"|
|404|Not found|Show "Doesn't exist"|
|422|Validation failed|Show `data.errors`|
|500|Server error|Show "Something went wrong, check Laravel logs"|

---

## The Flow to Debug When Something Breaks

**Step 1 — Open browser DevTools → Network tab**  
Click the failing request. Check:

- What URL was called? (did it hit the right endpoint?)
- What was in the Request Headers? (is the token there?)
- What came back in the Response? (read the JSON)

**Step 2 — Check the status code first**

- Got HTML back instead of JSON? → You're missing `Accept: application/json` header
- Got 401? → Token is missing or wrong
- Got 403? → Token is fine but the user's role failed the policy
- Got 405 Method Not Allowed? → Wrong HTTP method (GET vs POST vs PATCH)
- Got 419? → CSRF token issue — not relevant for API routes but double-check you're hitting `/api/...` not a web route

**Step 3 — Check Laravel logs**

```bash
tail -f storage/logs/laravel.log
```

500 errors always explain themselves here.

---

## Quick Reference — What Goes In / What Comes Out

|Endpoint|Method|Body you send|What you get back|
|---|---|---|---|
|`/api/register`|POST|`{ name, email, password, role }`|`{ token }`|
|`/api/login`|POST|`{ email, password }`|`{ token }`|
|`/api/logout`|POST|nothing|`{ message }`|
|`/api/projects`|GET|nothing|`{ data: [...] }`|
|`/api/projects`|POST|`{ name, description }`|`{ data: {...} }`|
|`/api/projects/{id}`|DELETE|nothing|`{ message }`|
|`/api/projects/{id}/assign`|POST|`{ user_id }`|`{ message }`|
|`/api/tasks`|GET|nothing (optional `?status=`)|`{ data: [...], meta, links }`|
|`/api/tasks`|POST|`{ title, project_id, assigned_to }`|`{ data: {...} }`|
|`/api/tasks/{id}/status`|PATCH|`{ status }`|`{ data: {...} }`|

---

_That's the whole frontend. Once this works, you understand the full request cycle. CSS can wait._