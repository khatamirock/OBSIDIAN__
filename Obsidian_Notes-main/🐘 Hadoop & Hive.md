
> **Goal:** Understand Hadoop & Hive deeply enough, ace interviews, and contribute on the job.  
> [Apache Hadoop Architecture - HDFS, YARN & MapReduce - TechVidvan](https://techvidvan.com/tutorials/hadoop-architecture/)
---

## 📌 Table of Contents

1. [Big Picture — What & Why]()
2. [Phase 1 — Hadoop Core (Week 1)]()
3. [Phase 2 — Hive Deep Dive (Week 2)]()
4. [Phase 3 — Hadoop ↔ Hive Interaction (Week 3)]()
5. [Phase 4 — Hands-On Practice (Week 4)]()
6. [🔥 Most Frequently Asked Interview Topics]()
7. [💬 Top Interview Q&A Bank]()
8. [Cheat Sheet — Key Commands]()
9. [Resources]()

---

## 1. Big Picture

### Why does Hadoop exist?

Traditional databases (RDBMS) can't handle **petabytes of data** across thousands of machines. Hadoop solves this with two core ideas:

- **Distribute the storage** → HDFS
- **Distribute the computation** → MapReduce (or YARN + engines on top)

### The Hadoop Ecosystem (Know the map!)

```
┌─────────────────────────────────────────────────────────┐
│                   YOUR DATA PIPELINE                    │
│                                                         │
│   Ingestion       Storage        Processing   Query     │
│   ─────────       ───────        ──────────   ─────     │
│   Sqoop ──────►  HDFS  ◄──────── MapReduce ◄── Hive     │
│   Flume ──────►  HDFS             Spark    ◄── Pig      │
│   Kafka           │               Tez      ◄── HBase    │
│                   │                                     │
│              YARN (Resource Manager)                    │
│              ZooKeeper (Coordination)                   │
└─────────────────────────────────────────────────────────┘
```

>Hive sits ON TOP of Hadoop. Hive converts your SQL into MapReduce/Tez/Spark jobs that run on HDFS. You write SQL, Hadoop does the heavy lifting.

---

## 2. Phase 1 — Hadoop Core

### 🗓️ Week 1 Roadmap

|Day|Topic|
|---|---|
|1|HDFS Architecture & Concepts|
|2|HDFS Commands & File Operations|
|3|MapReduce — How it works|
|4|YARN — Resource Management|
|5|Hadoop Config & Cluster Modes|
|6–7|Practice + Review|

---

### 📦 HDFS (Hadoop Distributed File System)

#### Core Architecture

![[Pasted image 20260308150719.png]]


#### Key Concepts to Master

| Concept                | What to Know                                                                                                                                                                                                      |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Block size**         | Default 128MB (older: 64MB). Large files split into blocks.                                                                                                                                                       |
| **Replication Factor** | Default = 3. One block is stored on 3 DataNodes for fault tolerance.                                                                                                                                              |
| **NameNode**           | Brain of HDFS. Stores metadata. Single point of failure (use HA setup).                                                                                                                                           |
| **Secondary NameNode** | NOT a backup. Merges `edit logs` with `FsImage` to ==prevent== `NameNode` ==restart lag.==                                                                                                                        |
| **DataNode**           | Worker nodes. Stores actual data blocks. Sends heartbeats to NameNode.                                                                                                                                            |
| **Rack Awareness**     | Hadoop is aware of physical rack placement. Replicates blocks across racks.<br>---<br>Rack Awareness in Hadoop is a **mechanism** that helps the ==NameNode ,,, understand the physical topology== of the cluster |
| **Write Pipeline**     | Client → NameNode (get block list) → DataNode 1 → DN2 → DN3 (chain write)                                                                                                                                         |
| **Read Path**          | Client → NameNode (get block locations) → closest DataNode                                                                                                                                                        |
|                        |                                                                                                                                                                                                                   |

#### HDFS Commands (Must Know)

```bash
# File operations
hdfs dfs -ls /                          # List root directory
hdfs dfs -ls -R /user/hive/warehouse    # Recursive list
hdfs dfs -mkdir -p /data/raw            # Create directories
hdfs dfs -put localfile.csv /data/raw/  # Upload from local       <<<<<<<<<  
hdfs dfs -get /data/raw/file.csv ./     # Download to local       <<<<<<<<<
hdfs dfs -cat /data/raw/file.csv        # Print file contents
hdfs dfs -mv /data/raw/a.csv /data/processed/  # Move
hdfs dfs -cp /data/raw/a.csv /data/backup/     # Copy
hdfs dfs -rm -r /data/temp/             # Delete (recursive)
hdfs dfs -du -s -h /data/               # Disk usage (human readable)
hdfs dfs -chmod 755 /data/              # Change permissions      <<<<<<<<<
hdfs dfs -chown user:group /data/       # Change ownership
hdfs dfs -count /data/                  # Count files/dirs/size

# Admin commands
hdfs dfsadmin -report                   # Cluster health report
hdfs dfsadmin -safemode get             # Check safe mode status
hdfs fsck /data/ -files -blocks         # File system health check
```

---


![[Pasted image 20260308140135.png]]
### ⚙️ MapReduce

#### How MapReduce Works (Simplified)

```
Input Data (HDFS)
      │
      ▼
  ┌─────────┐
  │  Split  │  ← Data split into InputSplits (≈ block size)
  └────┬────┘
       │ (one Mapper per split)
       ▼
  ┌─────────┐
  │  Map    │  ← Processes each record, emits (key, value) pairs
  └────┬────┘
       │
       ▼
  ┌─────────┐
  │ Shuffle │  ← Groups all values by key across all mappers
  │  & Sort │    (most expensive phase — network I/O)
  └────┬────┘
       │
       ▼
  ┌─────────┐
  │ Reduce  │  ← Aggregates grouped values, writes output to HDFS
  └─────────┘
       │
       ▼
  Output (HDFS)
```

#### Classic Word Count Example (Mentally trace this!)

```
Input:  "hello world hello hadoop"

Map Output:
  (hello, 1), (world, 1), (hello, 1), (hadoop, 1)

After Shuffle & Sort:
  (hadoop, [1])
  (hello,  [1, 1])
  (world,  [1])

Reduce Output:
  (hadoop, 1)
  (hello,  2)
  (world,  1)
```

#### MapReduce Key Terms

| Term                           | Meaning                                                                                   |
| ------------------------------ | ----------------------------------------------------------------------------------------- |
| **InputFormat**                | Defines how input data is read (TextInputFormat, SequenceFileInputFormat)                 |
| **Combiner**                   | Mini-reducer that runs locally on mapper output to reduce shuffle data                    |
| **Partitioner**                | Decides which reducer gets which key (default: hash of key % num_reducers)                |
| **Speculative Execution**      | Launches duplicate tasks for slow-running mappers/reducers, uses whichever finishes first |
| **Job Tracker / Task Tracker** | Old MR1 terminology. Replaced by ResourceManager/NodeManager in YARN                      |

---

### 🧠 YARN (Yet Another Resource Negotiator)

![[Pasted image 20260308141738.png]]


- **ResourceManager** → Allocates cluster resources (CPU, RAM)
- **NodeManager** → ==Manages resources on each node==, runs containers
- **ApplicationMaster** → One per job; negotiates resources, monitors tasks
- **Container** → Unit of resource allocation (CPU + memory bundle)

**Why YARN matters:** Before YARN (Hadoop 1.x), MapReduce had its own resource management and could only run MR jobs. YARN decoupled resource management — now Spark, Tez, Flink all run on the same cluster.

---

## 3. Phase 2 — Hive Deep Dive

| Day | Topic                          |
| --- | ------------------------------ |
| 1   | Hive Architecture & Metastore  |
| 2   | HiveQL — DDL (Tables, Schemas) |
| 3   | HiveQL — DML & Querying        |
| 4   | Partitioning & Bucketing       |
| 5   | File Formats & Compression     |
| 6–7 | Joins, UDFs, Optimization      |

---

### 🏗️ Hive Architecture
[A Comprehensive Guide On Apache Hive Basics.](https://blog.devops.dev/a-comprehensive-guide-on-apache-hive-basics-582cc07fe124)


![[Pasted image 20260308142051.png]]
![[Pasted image 20260309103620.png]]
#### How a Hive Query Executes

1. You write HiveQL
2. **Parser** → validates syntax
3. **Semantic Analyzer** → checks table/column existence against Metastore
4. **Logical Plan** → generates query plan
5. **Optimizer** → applies optimizations (predicate pushdown, column pruning)
6. **Physical Plan** → converts to MapReduce/Tez DAG
7. Submits to **YARN** for execution on **HDFS** data
8. Results returned to client

---

### 🗄️ Hive Tables — Internal vs External (CRITICAL TOPIC) [[Internal V External Tables| why ???]]

|Feature|Internal Table|External Table|
|---|---|---|
|Data location|Managed by Hive warehouse|Existing location in HDFS|
|DROP TABLE|**Deletes table + data**|**Deletes only metadata**|
|Data ownership|Hive owns the data|Data owned by external system|
|Typical use|Temporary / managed datasets|Shared datasets, data lake|

---

### Why Hadoop/Hive mostly uses **External Tables**

1️⃣ **Data safety**

If you drop an internal table, Hive deletes the underlying HDFS files.

Example  
`DROP TABLE customers;`  
→ data in HDFS also deleted.

With external tables:

`DROP TABLE customers_ext;`  
→ only schema removed, **data stays in HDFS**.

---

2️⃣ **Data lake architecture**

In Hadoop, data usually lives in **shared HDFS directories** used by multiple tools:

- Apache Hive
    
- Apache Spark
    
- Presto
    

External tables allow all of them to **read the same files**.

Internal tables would make Hive the **owner**, which is not ideal.

---

3️⃣ **ETL pipelines write directly to HDFS**

Most pipelines write data using tools like:

- Apache Spark
    
- Apache Sqoop
    

Then Hive just creates an **external table pointing to that folder**.

---

4️⃣ **Better control of data lifecycle**

In production data lakes:

- Data retention policies
    
- Backup
    
- Multiple consumers
    

External tables prevent accidental deletion.

---

### One-line summary (good for instructor)

> Internal tables let Hive manage and delete the data, while external tables only provide schema over existing HDFS files, which is why data lakes usually prefer external tables to avoid accidental data loss and allow multiple tools to access the same dataset.]]

|Feature|Internal (Managed) Table|External Table|
|---|---|---|
|Data location|Hive warehouse (`/user/hive/warehouse`)|Any HDFS path you specify|
|DROP TABLE|**Deletes data AND metadata**|Deletes metadata ONLY, data stays|
|Use case|Hive owns the data lifecycle|Data shared with other tools (Spark, etc.)|
|Default|No `EXTERNAL` keyword|Uses `CREATE EXTERNAL TABLE`|

```sql
-- Internal table
CREATE TABLE employees (
  id INT,
  name STRING,
  salary DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

-- External table (preferred for DE work!)
CREATE EXTERNAL TABLE sales (
  order_id    INT,
  product     STRING,
  amount      DOUBLE,
  order_date  STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS PARQUET
LOCATION '/data/raw/sales/';
```

> ⚠️ **In real DE work, you'll use External tables 90% of the time** because data is shared across tools and you don't want Hive to accidentally delete it.

---

### 📂 Partitioning & Bucketing

#### Partitioning

**Partitioning** divides a table into **separate folders in HDFS based on a column value**.
Example table:
#### Sales
-------------------------  
date        country   amount  
2026-03-01  BD        100  
2026-03-01  IN        200  
2026-03-02  BD        150

If we partition by **country**, Hive creates folders like:

/sales/  
   country=BD/  
       file1  
       file2  
   country=IN/  
       file3

#### Query Example
	SELECT * FROM sales WHERE country='BD'
	
	Hive will only read:
	country=BD/
	
	and **skip the rest**.
	✅ Result: **huge speed improvement**
	This is called **Partition Pruning**.

#### Partitioning works well **only when column values are limited**.
Good example:
country  
year  
month

### Query Example
```sql
-- Create partitioned table
CREATE TABLE sales_partitioned (
  order_id  INT,
  product   STRING,
  amount    DOUBLE
)
PARTITIONED BY (year INT, month INT)
STORED AS PARQUET;

-- Load data into specific partition
INSERT INTO sales_partitioned PARTITION (year=2024, month=1)
SELECT order_id, product, amount FROM sales_raw
WHERE year=2024 AND month=1;

-- Query benefits from partition pruning
SELECT SUM(amount) FROM sales_partitioned
WHERE year=2024 AND month=1;  -- Only reads that one partition!
```

**Static vs Dynamic Partitioning:**
```sql
-- Enable dynamic partitioning
SET hive.exec.dynamic.partition = true;
SET hive.exec.dynamic.partition.mode = nonstrict;

-- Dynamic: Hive figures out partitions from data
INSERT INTO sales_partitioned PARTITION (year, month)
SELECT order_id, product, amount, year, month FROM sales_raw;
```

#### Bucketing

**Bucketing divides data into a ==fixed number of files== using hashing.**
Instead of folders like partitioning, it creates **N bucket files**.

Example:
```sql
CREATE TABLE customers_bucketed (
  customer_id INT,
  name        STRING,
  email       STRING
)
CLUSTERED BY (customer_id) INTO 32 BUCKETS
STORED AS ORC;
```

#### 4️⃣ Why Bucketing Exists (VERY IMPORTANT)

Buckets solve **three major problems**.
🔹 1. Faster Joins
🔹 2. Better Sampling
🔹 3. Handling High Cardinality Columns

---

### 📄 File Formats (Know these cold!)

|Format|Type|Splittable|Compression|Best For|
|---|---|---|---|---|
|**TextFile**|Row|Yes (with splittable codec)|Gzip, Snappy|Raw ingestion, debugging|
|**ORC**|Columnar|Yes|Zlib, Snappy, LZ4|Hive-heavy workloads, best Hive performance|
|**Parquet**|Columnar|Yes|Snappy, Gzip|Spark + Hive interop, most popular in industry|
|**Avro**|Row|Yes (with index)|Snappy, Deflate|Schema evolution, Kafka integration|
|**SequenceFile**|Row|Yes|Various|MapReduce intermediate data|

> 💡 **Rule of thumb:** Use **Parquet** for most DE work (universal support). Use **ORC** if you're Hive-only and want the best Hive query performance.

---

### 🔗 Hive Joins

```sql
-- Common Join Types
-- 1. Regular join (both sides loaded into memory if small enough)
SELECT a.order_id, b.customer_name
FROM orders a JOIN customers b ON a.customer_id = b.customer_id;

-- 2. Map-side join (broadcast small table to all mappers — FAST!)
SELECT /*+ MAPJOIN(b) */ a.order_id, b.customer_name
FROM orders a JOIN customers b ON a.customer_id = b.customer_id;

-- 3. Left join
SELECT a.*, b.customer_name
FROM orders a LEFT JOIN customers b ON a.customer_id = b.customer_id;

-- 4. Skew join (for data skew problems)
SET hive.optimize.skewjoin = true;
```

**Join Optimization Tips:**

- Put the **largest table last** in a series of joins (Hive streams it)
- Use `MAPJOIN` hint for small dimension tables (< 25MB by default)
- Enable `hive.auto.convert.join = true` for automatic map joins

---

### 🔧 Key Hive Settings

```sql
-- Performance settings you'll use daily
SET hive.execution.engine = tez;           -- Use Tez instead of MR (faster)
SET hive.vectorized.execution.enabled = true;  -- Vectorized processing
SET hive.auto.convert.join = true;         -- Auto map-join for small tables
SET hive.exec.parallel = true;             -- Run independent stages in parallel
SET hive.exec.compress.output = true;      -- Compress output files
SET mapreduce.job.reduces = 50;            -- Control number of reducers

-- Partitioning settings
SET hive.exec.dynamic.partition = true;
SET hive.exec.dynamic.partition.mode = nonstrict;
SET hive.exec.max.dynamic.partitions = 1000;
```

---

## 4. Phase 3 — Interaction & Architecture

### 🔄 How Hadoop and Hive Work Together

```
You (write SQL)
      │
      ▼
   HIVE CLI / Beeline
      │
      ▼
   Hive Driver
   ├── Checks Metastore → "Where is the 'sales' table data?" → /data/sales/ on HDFS
   ├── Compiles SQL → Logical Plan → Physical Plan (MapReduce or Tez DAG)
   └── Submits job to YARN
                  │
                  ▼
            YARN ResourceManager
            ├── Allocates containers on DataNodes
            └── Runs Map/Reduce tasks
                      │
                      ▼
               DataNodes (where HDFS data lives)
               ├── Read data blocks
               ├── Process (filter, aggregate)
               └── Write results back to HDFS
                          │
                          ▼
                   Results → Hive → You
```

### The Metastore — Bridge Between Hive & HDFS

The Metastore is what makes Hive possible. It stores:

- Table names, column names, data types
- Where data lives on HDFS (LOCATION)
- Partition information
- File format (ORC, Parquet, etc.)
- Statistics for query optimization

Without the Metastore, Hive wouldn't know what schema to apply to files sitting in HDFS.

### Execution Engines: MR vs Tez vs Spark

|Engine|Speed|How it works|
|---|---|---|
|**MapReduce**|Slow|Each stage writes to HDFS between Map and Reduce|
|**Tez**|~2-10x faster than MR|Uses DAG; keeps data in memory between stages|
|**Spark**|~10-100x faster than MR|Full in-memory DAG; best for iterative processing|

```sql
-- Switch execution engine per query
SET hive.execution.engine = mr;    -- MapReduce
SET hive.execution.engine = tez;   -- Tez (recommended for Hive)
SET hive.execution.engine = spark; -- Spark
```

---

### HDFS + Hive Data Flow (End-to-End Example)

```
1. Raw CSV lands in HDFS:
   hdfs dfs -put orders.csv /data/raw/orders/

2. Create external Hive table pointing to that path:
   CREATE EXTERNAL TABLE orders_raw (...)
   LOCATION '/data/raw/orders/';

3. Transform and load into partitioned ORC table:
   INSERT INTO orders_clean PARTITION (year, month)
   SELECT ..., year(order_date), month(order_date)
   FROM orders_raw
   WHERE amount > 0;

4. This INSERT triggers a Tez/MR job on YARN:
   - Reads /data/raw/orders/ from HDFS DataNodes
   - Filters, transforms data
   - Writes ORC files to /user/hive/warehouse/orders_clean/year=.../month=.../

5. Query the clean table:
   SELECT SUM(amount) FROM orders_clean WHERE year=2024;
   (Only reads 2024 partitions from HDFS!)
```

---

## 5. Phase 4 — Hands-On Practice

### 🛠️ Local Setup Options

**Option A: Docker (Easiest)**

```bash
# Single-node Hadoop + Hive cluster
docker pull apache/hive:3.1.3
docker run -d -p 10000:10000 -p 10002:10002 \
  --name hive apache/hive:3.1.3

# Connect with Beeline
beeline -u jdbc:hive2://localhost:10000
```

**Option B: Hive on your machine (Mac/Linux)**

```bash
brew install hadoop hive   # Mac
# Then configure hive-site.xml, hadoop configs
```

**Option C: Cloud free tier**

- AWS EMR free tier
- Google Cloud Dataproc (free trial)
- Cloudera sandbox VM (download)

---

### 🏋️ Practice Projects (Do All 3)

#### Project 1 — NYC Taxi Data Analysis

```sql
-- Dataset: NYC Yellow Taxi Trip Records (public)
-- Download: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

CREATE EXTERNAL TABLE taxi_trips (
  vendor_id       STRING,
  pickup_datetime STRING,
  dropoff_datetime STRING,
  passenger_count INT,
  trip_distance   DOUBLE,
  fare_amount     DOUBLE,
  tip_amount      DOUBLE,
  total_amount    DOUBLE
)
PARTITIONED BY (year INT, month INT)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS PARQUET
LOCATION '/data/taxi/';

-- Analysis queries to write:
-- 1. Average tip by hour of day
-- 2. Top 10 busiest pickup hours
-- 3. Revenue by month (use partitions!)
-- 4. Average trip distance by passenger count
```

#### Project 2 — Log Analysis

```sql
-- Simulate web server logs
-- Parse raw text logs, extract fields, analyze traffic patterns
-- Practice: regex_extract, UDFs, window functions
```

#### Project 3 — Sales Data Warehouse

```sql
-- Build a star schema in Hive:
-- Fact table: sales_fact (partitioned by date)
-- Dim tables: customers, products, stores
-- Practice: all join types, aggregations, CTEs
```

---

## 6. Most Frequently Asked Topics

> These are the topics that come up in **80%+ of DE intern interviews** and on-the-job situations.

### 🔴 Tier 1 — Must Know (Always Asked)

1. **HDFS Architecture** — NameNode, DataNode, block size, replication
2. **Internal vs External Tables** — when to use each, what DROP TABLE does
3. **Partitioning** — how it works, partition pruning, static vs dynamic
4. **File Formats** — ORC vs Parquet vs TextFile tradeoffs
5. **MapReduce flow** — Map → Shuffle → Sort → Reduce
6. **How Hive query becomes a MR/Tez job** — end-to-end execution
7. **Hive Metastore** — what it stores, why it exists
8. **YARN** — ResourceManager, NodeManager, ApplicationMaster roles

### 🟡 Tier 2 — Should Know (Often Asked)

9. **Bucketing** — vs partitioning, use cases
10. **Map-side join** — when and why it's faster
11. **Data skew** — what it is, how to handle it
12. **Execution engines** — MR vs Tez vs Spark on Hive
13. **Secondary NameNode** — what it actually does (not a backup!)
14. **HDFS Write & Read pipeline** — step by step
15. **Vectorized execution** — what it means in Hive ORC
16. **Hive window functions** — RANK, ROW_NUMBER, LEAD/LAG

### 🟢 Tier 3 — Good to Know (Bonus Points)

17. **ACID transactions in Hive** — ORC + bucketing requirement
18. **Hive SerDe** — what it is, custom SerDe for JSON/CSV
19. **Cost-Based Optimizer (CBO)** — how Hive estimates query plans
20. **Rack awareness** — how HDFS places replicas
21. **Small files problem** — why it hurts HDFS, how to fix it
22. **Compaction in Hive** — minor vs major compaction for ACID tables

---

## 7. Top Interview Q&A Bank

### Hadoop Questions

**Q1: What is the difference between NameNode and DataNode?**

> **NameNode** is the master that stores metadata (file names, block locations, permissions). It never stores actual data. **DataNode** stores actual data blocks and sends heartbeats to NameNode every 3 seconds. If NameNode crashes, HDFS is unavailable — which is why HA (High Availability) NameNode exists.

**Q2: What does the Secondary NameNode do?**

> It periodically merges the **FsImage** (snapshot of metadata) with **EditLog** (recent changes) to create a new FsImage. This prevents the EditLog from growing too large and speeds up NameNode restart. It does NOT act as a hot standby.

**Q3: What happens if the NameNode fails?**

> In a non-HA cluster — HDFS becomes unavailable, but data isn't lost (DataNodes still have blocks). In an **HA setup**, a Standby NameNode takes over automatically via ZooKeeper-based failover.

**Q4: How does HDFS achieve fault tolerance?**

> Through **block replication** (default factor = 3). Blocks are replicated across DataNodes on different racks. If a DataNode fails, NameNode detects the missing heartbeat, finds under-replicated blocks, and instructs other DataNodes to re-replicate.

**Q5: What is Rack Awareness?**

> Hadoop is aware of physical rack locations. For replication factor 3, it places: 1 replica on the local node, 1 on a different node in the same rack, 1 on a node in a different rack. This balances fault tolerance with network efficiency.

**Q6: What is the difference between Hadoop 1.x and 2.x?**

> In Hadoop 1.x: JobTracker managed both resource allocation AND job monitoring (single point of failure, couldn't scale beyond ~4000 nodes). In 2.x: **YARN** split this into ResourceManager (resources) + ApplicationMaster per job (job monitoring), enabling multiple frameworks (Spark, MR, Tez) to coexist.

**Q7: What is speculative execution?**

> When a task is running slowly (straggler), Hadoop launches a duplicate copy of that task on another node. Whichever finishes first — its output is used, the other is killed. Useful for hardware hotspots but can waste resources.

---

### Hive Questions

**Q8: Internal vs External table — what happens on DROP TABLE?**

> **Internal**: Both metadata AND data on HDFS are deleted. **External**: Only metadata is deleted; HDFS data remains safe. Always use external tables when data is shared between tools or managed outside Hive.

**Q9: How does Hive execute a SQL query on Hadoop?**

> 1. Hive Driver parses SQL, consults Metastore for schema/location 2. Compiler creates logical plan 3. Optimizer applies rules (predicate pushdown, column pruning) 4. Converts to physical plan (MapReduce/Tez DAG) 5. Submits to YARN 6. YARN runs tasks on DataNodes reading from HDFS 7. Results written back to HDFS, then returned to user.

**Q10: What is partition pruning?**

> When you filter on a partition column (e.g., `WHERE year=2024`), Hive only reads HDFS subdirectories matching that partition instead of scanning the entire table. Can reduce data scanned by 99%+ on large partitioned tables.

**Q11: What's the difference between partitioning and bucketing?**

> **Partitioning**: Creates subdirectories by column value (good for filtering with WHERE). Number of partitions = number of unique values. **Bucketing**: Hashes rows into a fixed number of files (good for joins and sampling). Bucketing gives more predictable file sizes.

**Q12: ORC vs Parquet — which do you use and when?**

> Both are columnar formats. **ORC** is optimized for Hive (better predicate pushdown within Hive, supports ACID transactions). **Parquet** has broader ecosystem support (Spark, Presto, Athena, BigQuery). For Hive-only workloads → ORC. For multi-tool environments → Parquet.

**Q13: What is the Hive Metastore and can it be shared?**

> The Metastore is a relational database (MySQL, PostgreSQL, etc.) storing table schemas, partition info, and HDFS locations. Yes — it can be shared across multiple Hive instances and even with Spark (Spark can read Hive Metastore directly using `enableHiveSupport()`).

**Q14: What is data skew in Hive and how do you handle it?**

> Skew occurs when most data maps to a few reducer keys, causing those reducers to take much longer (one reducer processes 90% of data while others sit idle). Solutions: `SET hive.optimize.skewjoin=true`, salt the skewed key (add random prefix), use `SKEWED BY` clause in table DDL, or pre-aggregate upstream.

**Q15: What are window functions? Give an example.**

```sql
-- Rank customers by total purchase amount within each region
SELECT
  customer_id,
  region,
  total_amount,
  RANK() OVER (PARTITION BY region ORDER BY total_amount DESC) AS rank_in_region,
  SUM(total_amount) OVER (PARTITION BY region) AS region_total,
  LAG(total_amount, 1) OVER (PARTITION BY region ORDER BY order_date) AS prev_month_amount
FROM sales;
```

**Q16: What is a Map-side join?**

> A join where the smaller table is loaded into memory on every mapper, and join is done locally without a reduce phase (no shuffle). Eliminates the expensive shuffle & sort phase. Use when one table fits in memory (< 25MB default threshold, configurable). Enable with `SET hive.auto.convert.join=true` or `/*+ MAPJOIN(small_table) */` hint.

**Q17: What is the small files problem in HDFS?**

> Each file, regardless of size, consumes one block entry in NameNode memory. Millions of small files → NameNode runs out of memory, and MapReduce launches one task per file (massive overhead). Solutions: Use `CONCATENATE` to merge ORC files, use Hive's `hive.merge.mapfiles=true`, or use HAR (Hadoop Archive).

---

### Scenario-Based Questions

**Q18: You notice a Hive query is running slow. How do you debug it?**

> 1. Check `EXPLAIN` plan for unexpected stages 2. Look at data size — are partitions being pruned? 3. Check for data skew in reducer tasks (one reducer taking 10x longer) 4. Verify file format is columnar (ORC/Parquet) 5. Check if map join can apply 6. Look at execution engine (switch to Tez if on MR) 7. Review statistics — run `ANALYZE TABLE` if CBO is enabled

**Q19: Your Hive job is failing with "Too many dynamic partitions" error. What do you do?**

```sql
SET hive.exec.max.dynamic.partitions = 5000;           -- increase limit
SET hive.exec.max.dynamic.partitions.pernode = 2000;   -- per node limit
-- Also check if data has unexpected cardinality in partition column
```

**Q20: Difference between `hive.execution.engine=tez` vs `mr`?**

> MapReduce writes intermediate data to HDFS between each stage — very disk I/O heavy. Tez builds a DAG and keeps intermediate data in memory where possible, dramatically reducing disk I/O. Tez is typically 2-10x faster for Hive workloads. Most modern clusters use Tez as default.

---

## 8. Cheat Sheet

### HDFS Quick Reference

```bash
hdfs dfs -ls /path                    # List
hdfs dfs -put local hdfs_path         # Upload
hdfs dfs -get hdfs_path local         # Download
hdfs dfs -cat /path/file              # Print
hdfs dfs -du -s -h /path              # Size
hdfs dfs -rm -r /path                 # Delete
hdfs dfsadmin -report                 # Cluster status
hdfs fsck /path -files -blocks        # Health check
```

### Hive DDL Quick Reference

```sql
-- Show things
SHOW DATABASES;
SHOW TABLES;
SHOW PARTITIONS table_name;
DESCRIBE table_name;
DESCRIBE FORMATTED table_name;     -- detailed info including location
EXPLAIN SELECT ...;                -- query plan

-- Table operations
CREATE [EXTERNAL] TABLE ... STORED AS [ORC|PARQUET|TEXTFILE];
ALTER TABLE t ADD PARTITION (year=2024, month=1);
ALTER TABLE t DROP PARTITION (year=2023);
MSCK REPAIR TABLE t;               -- sync partitions from HDFS to Metastore
ANALYZE TABLE t COMPUTE STATISTICS;
DROP TABLE [IF EXISTS] t [PURGE];  -- PURGE skips Trash

-- Data loading
LOAD DATA [LOCAL] INPATH '...' INTO TABLE t PARTITION (...);
INSERT INTO t SELECT ... FROM ...;
INSERT OVERWRITE t SELECT ... FROM ...;
```

### HiveQL Window Functions

```sql
ROW_NUMBER() OVER (PARTITION BY col ORDER BY col2)
RANK()        OVER (PARTITION BY col ORDER BY col2)
DENSE_RANK()  OVER (PARTITION BY col ORDER BY col2)
LAG(col, n)   OVER (PARTITION BY col ORDER BY col2)
LEAD(col, n)  OVER (PARTITION BY col ORDER BY col2)
SUM(col)      OVER (PARTITION BY col ORDER BY col2 ROWS BETWEEN ...)
```

---

## 9. Resources

### Free Learning Resources

|Resource|What it's good for|
|---|---|
|[Apache Hive Wiki](https://cwiki.apache.org/confluence/display/Hive)|Official, authoritative reference|
|[HDFS Architecture Guide](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html)|Deep HDFS understanding|
|[Hadoop: The Definitive Guide (O'Reilly)](https://www.oreilly.com/library/view/hadoop-the-definitive/9781491901687/)|The bible of Hadoop|
|[Hive Tutorial (TutorialsPoint)](https://www.tutorialspoint.com/hive/)|Quick practical reference|
|YouTube: "Hive Tutorial for Beginners" by Edureka|Visual architecture explanations|

### Practice Data Sources

- [NYC Taxi Dataset](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) — Huge, partitioned well
- [Kaggle Datasets](https://www.kaggle.com/datasets) — Various domains
- [AWS Open Data Registry](https://registry.opendata.aws/) — Large-scale datasets

### Tools to Know Alongside Hive

|Tool|Why relevant|
|---|---|
|**Beeline**|Modern Hive CLI (use instead of `hive` command)|
|**Apache Spark**|Often used alongside/instead of Hive for processing|
|**Apache Sqoop**|Import/export data between RDBMS and HDFS|
|**Apache Oozie**|Workflow scheduler for Hadoop jobs|
|**Apache Zeppelin**|Notebook for writing Hive/Spark queries|

---

## ✅ Final Checklist — Are You Ready?

- [ ] Can explain HDFS architecture with a diagram from memory
- [ ] Know what NameNode, DataNode, Secondary NameNode each do
- [ ] Can explain MapReduce with a word count example
- [ ] Know YARN components and why it was introduced
- [ ] Can explain Internal vs External tables and when to use each
- [ ] Know how partitioning improves query performance
- [ ] Can explain the difference between ORC and Parquet
- [ ] Understand how a Hive query becomes a YARN job step-by-step
- [ ] Can write window function queries
- [ ] Know what causes data skew and how to fix it
- [ ] Can debug a slow Hive query systematically
- [ ] Have run at least one hands-on project

---

_Good luck with your internship! The fact that you're preparing this thoroughly already puts you ahead of most interns. 🚀_