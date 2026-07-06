#  Airflow 

---

## 1. WHAT IS AIRFLOW? (Core Concept)

Apache Airflow is a **workflow orchestration platform** where you define pipelines as code using Python. It schedules, monitors, and manages tasks.

Key philosophy: **"workflows as code"** — DAGs are just Python files.

> ⚠️ **Trap Q:** _"Is Airflow a data processing tool?"_ **NO.** Airflow **orchestrates** work. It tells other systems what to do and when. It does NOT move/process data itself.

---

## 2. DAGs (Directed Acyclic Graphs)

### What is a DAG?

- A **graph** of tasks with **directed** edges and **no cycles**
- Defines the order and relationship of tasks
- Airflow scans `$AIRFLOW_HOME/dags/` folder for `.py` files

### Basic DAG Structure

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'email_on_failure': True,
    'email': ['you@example.com']
}

with DAG(
    dag_id='my_dag',
    default_args=default_args,
    schedule_interval='@daily',         # or cron: '0 12 * * *'
    start_date=datetime(2024, 1, 1),
    catchup=False,                       # ⚠️ IMPORTANT
    tags=['example']
) as dag:
    ...
```

### Key DAG Parameters

| Param               | What it does                                                     |
| ------------------- | ---------------------------------------------------------------- |
| `schedule_interval` | When to run: `@daily`, `@hourly`, cron string, or `None`         |
| `start_date`        | When the DAG becomes active                                      |
| `catchup=False`     | Don't backfill missed runs — **almost always set this to False** |
| `max_active_runs`   | Max concurrent DAG runs                                          |
| `concurrency`       | Max tasks running simultaneously in this DAG                     |
| `default_args`      | Applied to all tasks unless overridden                           |

> ⚠️ **Trap Q:** _"What happens if `catchup=True` and your DAG has a `start_date` from 2 years ago?"_ Airflow will **create a run for every missed interval**, potentially flooding your system with hundreds of runs.

---

## 3. OPERATORS

Operators define **what a task does**. One operator = one task.

### Core Operators

```python
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator  # formerly DummyOperator
from airflow.operators.email import EmailOperator
from airflow.operators.python import BranchPythonOperator
```

### BashOperator

```python
run_script = BashOperator(
    task_id='run_script',
    bash_command='echo "Hello World" && python /path/to/script.py',
)
```

### PythonOperator

```python
def my_function(**kwargs):
    print("Running!")
    return "done"

run_python = PythonOperator(
    task_id='run_python',
    python_callable=my_function,
    op_kwargs={'param1': 'value1'},   # pass arguments
)
```

### EmptyOperator (formerly DummyOperator)

Used as **start/end markers** or for grouping tasks:

```python
start = EmptyOperator(task_id='start')
end = EmptyOperator(task_id='end')
```

### BranchPythonOperator (KEY for skipping!)

```python
from airflow.operators.python import BranchPythonOperator

def decide_branch(**kwargs):
    if some_condition:
        return 'task_a'       # return task_id to execute
    else:
        return 'task_b'       # other tasks get SKIPPED

branch = BranchPythonOperator(
    task_id='branch_task',
    python_callable=decide_branch,
)

task_a = PythonOperator(task_id='task_a', python_callable=func_a)
task_b = PythonOperator(task_id='task_b', python_callable=func_b)

branch >> [task_a, task_b]
```

> ⚠️ **Trap Q:** _"What state do skipped tasks show in the UI?"_ They show as **SKIPPED** (pink/magenta color), not FAILED.

### Sensors (special operators that wait)

```python
from airflow.sensors.filesystem import FileSensor
from airflow.sensors.http_sensor import HttpSensor

wait_for_file = FileSensor(
    task_id='wait_for_file',
    filepath='/data/input.csv',
    poke_interval=30,    # check every 30 seconds
    timeout=3600,        # fail after 1 hour
    mode='reschedule',   # ← releases worker slot while waiting (better than 'poke')
)
```

> ⚠️ **Trap Q:** _"Difference between `mode='poke'` and `mode='reschedule'`?"_
> 
> - `poke`: holds the worker slot the entire time (blocks resources)
> - `reschedule`: releases the slot between checks (much more efficient for long waits)

---

## 4. TASK DEPENDENCY (Setting Order)

### Methods to set dependencies

```python
# Method 1: Bitshift operators (most common)
task_a >> task_b >> task_c          # a → b → c
task_a >> [task_b, task_c]          # a → b AND a → c (parallel)
[task_b, task_c] >> task_d          # b AND c → d (join)

# Method 2: set_upstream / set_downstream
task_b.set_upstream(task_a)         # same as task_a >> task_b
task_b.set_downstream(task_c)       # same as task_b >> task_c

# Complex pipeline:
start >> extract >> [transform_1, transform_2] >> load >> end
```

### Cross-DAG Dependencies

```python
from airflow.sensors.external_task import ExternalTaskSensor

wait_for_other_dag = ExternalTaskSensor(
    task_id='wait_for_other_dag',
    external_dag_id='other_dag',
    external_task_id='final_task',  # None = wait for entire DAG
    timeout=3600,
)
```

---

## 5. PARALLELISM & SKIPPING TASKS

### Running Tasks in Parallel

```python
# These 3 tasks run simultaneously:
start >> [task_a, task_b, task_c] >> end
```

Parallel execution requires:

- Multiple workers (CeleryExecutor or KubernetesExecutor)
- Or enough slots with LocalExecutor
- `parallelism` setting in `airflow.cfg`

### Skipping Tasks — TriggerRule

By default, downstream tasks r==un only if ALL upstream== tasks **SUCCEED**. Change this with `trigger_rule`:

```python
from airflow.utils.trigger_rule import TriggerRule

task_d = PythonOperator(
    task_id='task_d',
    python_callable=func,
    trigger_rule=TriggerRule.ONE_SUCCESS,  # run if at least one upstream succeeded
)
```

|TriggerRule|Runs when...|
|---|---|
|`ALL_SUCCESS` (default)|All upstream tasks succeeded|
|`ALL_FAILED`|All upstream tasks failed|
|`ALL_DONE`|All upstream tasks are done (any state)|
|`ONE_SUCCESS`|At least one upstream succeeded|
|`ONE_FAILED`|At least one upstream failed|
|`NONE_FAILED`|No upstream tasks failed (skipped is OK)|
|`NONE_FAILED_MIN_ONE_SUCCESS`|Common for branch joins|

> ⚠️ **Trap Q:** _"You use BranchPythonOperator and the downstream join task never runs — why?"_ Because the join task's default `trigger_rule=ALL_SUCCESS` requires ALL parents to succeed, but the skipped branch was SKIPPED. Fix with `trigger_rule='none_failed_min_one_success'` on the join task.

```python
# CORRECT pattern for BranchPythonOperator with join:
join = EmptyOperator(
    task_id='join',
    trigger_rule=TriggerRule.NONE_FAILED_MIN_ONE_SUCCESS  # ← KEY
)
branch >> [task_a, task_b]
[task_a, task_b] >> join
```

---

## 6. XCOMS — PASSING DATA BETWEEN TASKS

XComs let tasks share small pieces of data.

```python
# Push data (task 1)
def push_data(**kwargs):
    kwargs['ti'].xcom_push(key='my_key', value='hello world')
    # OR just return a value (auto-pushes with key='return_value')
    return 42

# Pull data (task 2)
def pull_data(**kwargs):
    ti = kwargs['ti']
    value = ti.xcom_pull(task_ids='task_1', key='my_key')
    return_val = ti.xcom_pull(task_ids='task_1')  # pulls 'return_value'
    print(value, return_val)
```

> ⚠️ **Trap Q:** _"Can you pass a large DataFrame via XCom?"_ **NO.** XComs are stored in the metadata DB — use them for small values only (IDs, file paths, counts). For large data, pass a file path or use external storage.

---

## 7. FILE READING IN DAGS — DIFFERENT APPROACHES

This is a key topic in your hints. There are multiple ways to read config/data files:

### Method 1: Reading from the DAG file itself (relative path — BAD)

```python
# ❌ AVOID — relative paths break depending on where Airflow runs from
with open('config.json') as f:
    config = json.load(f)
```

### Method 2: Using `__file__` (good for files next to DAG)

```python
import os, json

dag_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(dag_dir, 'config.json')

with open(config_path) as f:
    config = json.load(f)
```

### Method 3: Airflow Variables (recommended for config)

```python
from airflow.models import Variable

# Set in UI: Admin → Variables
api_key = Variable.get("my_api_key")
config = Variable.get("my_config", deserialize_json=True)  # parses JSON
```

### Method 4: Airflow Connections (for DB/API credentials)

```python
from airflow.hooks.base import BaseHook

conn = BaseHook.get_connection('my_postgres_conn')
print(conn.host, conn.login, conn.password)
```

### Method 5: Environment Variables

```python
import os
db_url = os.environ.get('DATABASE_URL')
```

### Method 6: Reading from cloud storage (S3, GCS)

```python
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

hook = S3Hook(aws_conn_id='my_aws_conn')
content = hook.read_key('my_file.json', bucket_name='my-bucket')
```

> ⚠️ **Trap Q:** _"What's wrong with reading a file at DAG-level (outside a task)?"_ DAG files are parsed frequently by the scheduler (every few seconds/minutes). File reads at DAG level happen on EVERY parse, creating performance issues. Always read files **inside task callables**.

---

## 8. TEMPLATING & MACROS (Jinja)

Airflow supports Jinja templating in operator parameters:

```python
task = BashOperator(
    task_id='dated_task',
    bash_command='python process.py --date {{ ds }}',  # {{ ds }} = execution date YYYY-MM-DD
)
```

### Key Built-in Variables

|Variable|Value|
|---|---|
|`{{ ds }}`|Execution date as `YYYY-MM-DD`|
|`{{ ds_nodash }}`|Execution date as `YYYYMMDD`|
|`{{ ts }}`|Timestamp|
|`{{ execution_date }}`|Pendulum datetime object|
|`{{ next_ds }}`|Next execution date|
|`{{ prev_ds }}`|Previous execution date|
|`{{ dag.dag_id }}`|DAG ID|
|`{{ task.task_id }}`|Task ID|
|`{{ var.value.my_var }}`|Airflow Variable|
|`{{ conn.my_conn.host }}`|Connection host|

---

## 9. EXECUTORS (How tasks actually run)

|Executor|Description|Use Case|
|---|---|---|
|`SequentialExecutor`|One task at a time, uses SQLite|Local dev/testing only|
|`LocalExecutor`|Parallel tasks, single machine, uses Postgres/MySQL|Small production|
|`CeleryExecutor`|Distributed workers via message broker (Redis/RabbitMQ)|Production scale|
|`KubernetesExecutor`|Each task = a K8s pod|Cloud-native production|

> ⚠️ **Trap Q:** _"Can you run parallel tasks with SequentialExecutor?"_ **NO.** It runs tasks one at a time, regardless of dependencies. You need LocalExecutor or higher for parallelism.

---

## 10. TASK STATES

|State|Color|Meaning|
|---|---|---|
|`none`|White|Not yet queued|
|`scheduled`|Tan|Scheduler picked it up|
|`queued`|Gray|Waiting for an executor slot|
|`running`|Green (light)|Currently executing|
|`success`|Green (dark)|Finished successfully|
|`failed`|Red|Task threw an exception|
|`skipped`|Pink/Magenta|Skipped by BranchOperator or `trigger_rule`|
|`up_for_retry`|Yellow|Failed but will retry|
|`up_for_reschedule`|Cyan|Sensor waiting (reschedule mode)|
|`upstream_failed`|Orange|Parent task failed|

---

## 11. RETRIES & ERROR HANDLING

```python
default_args = {
    'retries': 3,
    'retry_delay': timedelta(minutes=10),
    'retry_exponential_backoff': True,  # 10m, 20m, 40m...
    'max_retry_delay': timedelta(hours=1),
    'on_failure_callback': my_failure_func,
    'on_success_callback': my_success_func,
    'on_retry_callback': my_retry_func,
}

def my_failure_func(context):
    # context has dag, task, execution_date, exception, etc.
    print(f"Task failed: {context['task_instance'].task_id}")
```

---

## 12. TASKFLOW API (Modern Airflow 2.x)

Cleaner syntax using decorators — avoids boilerplate:

```python
from airflow.decorators import dag, task
from datetime import datetime

@dag(schedule_interval='@daily', start_date=datetime(2024,1,1), catchup=False)
def my_pipeline():

    @task
    def extract():
        return {"data": [1, 2, 3]}

    @task
    def transform(data: dict):
        return [x * 2 for x in data["data"]]

    @task
    def load(result: list):
        print(result)

    raw = extract()
    transformed = transform(raw)      # XCom is handled automatically!
    load(transformed)

dag_instance = my_pipeline()
```

> ⚠️ **Trap Q:** _"How does XCom work in TaskFlow API?"_ It's automatic — return values are pushed as XComs and function parameters receive pulled values. No manual `ti.xcom_push/pull` needed.

---

## 13. DYNAMIC DAGS

Generating multiple DAGs or tasks from config:

```python
# Dynamic tasks from a list
tasks = ['task_1', 'task_2', 'task_3']

with DAG('dynamic_dag', ...):
    prev = None
    for t in tasks:
        current = PythonOperator(
            task_id=t,
            python_callable=lambda name=t: print(name),
        )
        if prev:
            prev >> current
        prev = current
```

> ⚠️ **Trap Q:** _"What's the lambda gotcha in dynamic task creation?"_ `lambda: print(t)` captures `t` by reference, so all lambdas will use the last value. Fix with `lambda name=t: print(name)` (default arg captures by value).

---

## 14. CONNECTIONS & HOOKS
[[HOOK & TOOK|see. more..]]
- **Connection**: credentials stored in Airflow (UI or env var)
- **Hook**: Python class that uses a connection to interact with external systems

```python
from airflow.providers.postgres.hooks.postgres import PostgresHook

def query_db(**kwargs):
    hook = PostgresHook(postgres_conn_id='my_postgres')
    df = hook.get_pandas_df("SELECT * FROM users LIMIT 10")
    return df.shape[0]
```

---

## 15. COMMON TRAP QUESTIONS SUMMARY

|Question|Answer|
|---|---|
|DAG file loaded but not appearing in UI?|Syntax error in DAG file, or DAG file not in dags folder|
|Task is stuck in "queued"?|No worker slots available / executor issue|
|`catchup=True` and old start_date?|Backfill runs for ALL missed intervals — dangerous|
|How to skip a task programmatically?|Raise `AirflowSkipException`|
|Can DAGs call each other?|Not directly — use ExternalTaskSensor or TriggerDagRunOperator|
|Execution date vs actual run time?|Execution date = the START of the schedule interval, not when Airflow actually runs it|
|How does Airflow schedule?|DAG with `start_date=Jan 1` and `@daily` runs AFTER Jan 1 ends, i.e., Jan 2|

---

## 16. RAISE SKIP MANUALLY

```python
from airflow.exceptions import AirflowSkipException

def conditional_task(**kwargs):
    if not some_condition:
        raise AirflowSkipException("Skipping — condition not met")
    # do real work
```

---

## 17. POOLS (Resource Limiting)

```python
# Limit concurrent tasks hitting a slow system
task = PythonOperator(
    task_id='api_call',
    python_callable=call_api,
    pool='api_pool',           # set max slots in UI: Admin → Pools
    pool_slots=1,              # how many slots this task consumes
)
```

---

## 18. QUICK MENTAL MODEL

```
Scheduler reads DAG files
    → Creates DagRuns based on schedule
        → Creates TaskInstances
            → Executor picks up tasks
                → Workers run them
                    → State updated in metadata DB
                        → UI reads metadata DB to show you
```

---
## 19. READING SQL & BASH FROM EXTERNAL FILES (Best Practice)

### ❌ What NOT to do — hardcoded queries

python

```python
# BAD — messy, hard to maintain, untestable
task = PythonOperator(
    task_id='run_query',
    python_callable=lambda: postgres_hook.run("""
        SELECT user_id, SUM(amount)
        FROM orders
        WHERE status = 'completed'
        GROUP BY user_id
    """)
)
```

---

### ✅ Folder Structure (recommended)

```
dags/
├── my_dag.py
├── sql/
│   ├── get_orders.sql
│   ├── insert_summary.sql
│   └── cleanup.sql
└── scripts/
    ├── process_data.sh
    └── validate.sh
```

---

### ✅ Reading SQL from a File

python

```python
import os

DAG_DIR = os.path.dirname(os.path.abspath(__file__))

def read_sql(filename):
    filepath = os.path.join(DAG_DIR, 'sql', filename)
    with open(filepath, 'r') as f:
        return f.read()

# Use inside a task (NOT at DAG level)
def run_query(**kwargs):
    from airflow.providers.postgres.hooks.postgres import PostgresHook
    hook = PostgresHook(postgres_conn_id='my_postgres')
    sql = read_sql('get_orders.sql')
    hook.run(sql)

query_task = PythonOperator(
    task_id='run_query',
    python_callable=run_query,
)
```

---

### ✅ Some operators support `sql` as a file path natively

python

```python
from airflow.providers.postgres.operators.postgres import PostgresOperator

# Airflow reads the file FOR you — just point to it
run_sql = PostgresOperator(
    task_id='run_sql',
    postgres_conn_id='my_postgres',
    sql='sql/get_orders.sql',     # ← relative to DAG folder, no open() needed
)
```

> ⚠️ **Trap Q:** _"Does PostgresOperator accept a file path or only a query string?"_ It accepts **both** — if the string ends in `.sql`, Airflow treats it as a file path relative to the DAGs folder. Same pattern works for `MySqlOperator`, `SqliteOperator`, etc.

---

### ✅ Templating inside SQL files (Jinja still works!)

**File: `sql/get_orders.sql`**

sql

```sql
SELECT user_id, SUM(amount)
FROM orders
WHERE status = 'completed'
  AND order_date = '{{ ds }}'    -- ← Jinja templating works here too!
GROUP BY user_id;
```

> Airflow will render `{{ ds }}` inside `.sql` files automatically when using providers like `PostgresOperator`. The file just needs to be passed as `sql='sql/get_orders.sql'`.

---

### ✅ Reading Bash Scripts from Files

python

```python
from airflow.operators.bash import BashOperator
import os

DAG_DIR = os.path.dirname(os.path.abspath(__file__))

# Method 1: Read file content and pass as bash_command string
def get_bash_script(filename):
    filepath = os.path.join(DAG_DIR, 'scripts', filename)
    with open(filepath, 'r') as f:
        return f.read()

run_bash = BashOperator(
    task_id='run_bash',
    bash_command=get_bash_script('process_data.sh'),
)

# Method 2: Just call the script directly (even cleaner)
run_script = BashOperator(
    task_id='run_script',
    bash_command=f'bash {DAG_DIR}/scripts/process_data.sh ',  # ← note trailing space (Airflow quirk)
    env={'MY_DATE': '{{ ds }}'},   # pass variables to the script
)
```

> ⚠️ **Trap Q:** _"Why the trailing space in `bash_command`?"_ Airflow treats `bash_command` values ending in `.sh` as **Jinja templates to locate**, and may throw a `Template not found` error. Adding a trailing space bypasses this lookup and treats it as a plain shell command.

---

### ✅ Passing Parameters into SQL/Bash Files

**Parameterized SQL with Jinja:**

sql

```sql
-- sql/get_orders.sql
SELECT * FROM orders
WHERE region = '{{ params.region }}'
  AND order_date = '{{ ds }}';
```

python

```python
PostgresOperator(
    task_id='query',
    postgres_conn_id='my_db',
    sql='sql/get_orders.sql',
    params={'region': 'Asia'},    # ← injected into {{ params.region }}
)
```

**Bash script receiving env vars:**

bash

```bash
# scripts/process_data.sh
echo "Processing date: $EXECUTION_DATE"
python /opt/etl/run.py --date "$EXECUTION_DATE"
```

python

```python
BashOperator(
    task_id='process',
    bash_command=f'bash {DAG_DIR}/scripts/process_data.sh ',
    env={'EXECUTION_DATE': '{{ ds }}'},
)
```

---

### Why This Matters (what to say in the interview)

- **Separation of concerns** — SQL/bash logic lives separately from orchestration logic
- **Reusability** — the same `.sql` file can be used in multiple DAGs or tested standalone
- **Version control friendly** — SQL reviewers don't need to read Python files
- **Easier testing** — you can run the `.sql` or `.sh` file directly without spinning up Airflow
- **Avoids DAG file bloat** — long hardcoded queries make DAG files unreadable

---

_Good luck tomorrow! Focus on: BranchOperator + trigger_rule combo, XCom limitations, catchup behavior, file-reading best practices, and the SQL/Bash-from-files pattern — those are the most common traps._


_Good luck tomorrow! Focus on: BranchOperator + trigger_rule combo, XCom limitations, catchup behavior, and file-reading best practices — those are the most common traps._