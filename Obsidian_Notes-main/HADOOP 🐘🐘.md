# Hadoop Getting Started — Full Plan

> **Assumption:** Hadoop is running in Docker, WebUI is accessible. Skip installation. Start learning from here.

---

## Where You Are Right Now

You have:

- Hadoop running inside a Docker container
- WebUI accessible (NameNode UI: `http://localhost:9870`, YARN UI: `http://localhost:8088`)
- A terminal open (either inside the container or SSH'd in)

---

## Phase 1 — Get Comfortable with the Cluster

### Step 1: Get inside the container

```bash
docker ps                                  # find your hadoop container name/id
docker exec -it <container_name> bash      # get a shell inside it
```

### Step 2: Verify everything is running

```bash
jps
```

You should see these 5 processes. If any are missing, that service is down:

|Process|What it does|
|---|---|
|`NameNode`|Manages HDFS metadata — the "directory" of all files|
|`DataNode`|Stores the actual data blocks|
|`ResourceManager`|Manages cluster resources (CPU/RAM) for jobs|
|`NodeManager`|Runs tasks on this specific node|
|`SecondaryNameNode`|Backs up NameNode metadata periodically|

### Step 3: Check cluster health via WebUI

| URL                     | What to check                             |
| ----------------------- | ----------------------------------------- |
| `http://localhost:9870` | HDFS health, live nodes, storage used     |
| `http://localhost:8088` | YARN — running/completed jobs, node stats |

On the **9870 page**: look for "Live Nodes: 1" and check DFS Used %.  
On the **8088 page**: this is where all your MapReduce jobs will show up after you submit them.

---

## Phase 2 — Learn HDFS (Hadoop's File System)

HDFS is NOT your local filesystem. Think of it as a separate hard drive that lives inside Hadoop. Everything you want to process must be uploaded here first.

### Basic HDFS navigation

```bash
hadoop fs -ls /                            # list root of HDFS
hadoop fs -ls /user/                       # list /user directory
hadoop fs -mkdir -p /user/hadoop/data      # create your working directory
hadoop fs -df -h                           # check total HDFS disk space
hadoop fs -du -h /user/hadoop/             # check size of your folder
```

### Upload files to HDFS

```bash
# First create a test file locally
echo -e "hello world\nhello hadoop\nlearn hadoop" > test.txt
wc -l test.txt                             # verify line count before upload

# Upload to HDFS
hadoop fs -put test.txt /user/hadoop/data/
hadoop fs -ls /user/hadoop/data/           # confirm it's there
```

### Read files on HDFS (without downloading)

```bash
hadoop fs -cat /user/hadoop/data/test.txt           # print entire file
hadoop fs -cat /user/hadoop/data/test.txt | head -5 # first 5 lines only
hadoop fs -cat /user/hadoop/data/test.txt | wc -l   # count lines
```

### Download files from HDFS back to local

```bash
hadoop fs -get /user/hadoop/data/test.txt ./downloaded.txt
hadoop fs -getmerge /user/hadoop/output/ ./merged_result.txt  # merge all output part files into one
```

### Delete on HDFS

```bash
hadoop fs -rm /user/hadoop/data/test.txt            # delete a file
hadoop fs -rm -r /user/hadoop/output/               # delete a folder (MUST do before re-running jobs)
```

> ⚠️ **Critical rule:** Hadoop will REFUSE to run a job if the output folder already exists. Always delete it before rerunning:
> 
> ```bash
> hadoop fs -rm -r /user/hadoop/output/ && hadoop jar ...
> ```

---

## Phase 3 — Run Your First MapReduce Job

Hadoop ships with built-in example jobs. Use these to learn before writing your own.

### The classic WordCount example

```bash
# Step 1: Prepare input — create a bigger test file
echo -e "the quick brown fox\nthe fox jumps high\nhadoop is fast\nhadoop mapreduce works" > words.txt

# Step 2: Upload to HDFS input folder
hadoop fs -mkdir -p /user/hadoop/input
hadoop fs -put words.txt /user/hadoop/input/
hadoop fs -ls /user/hadoop/input/               # confirm upload

# Step 3: Run WordCount MapReduce job
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar \
  wordcount /user/hadoop/input /user/hadoop/output

# Step 4: Watch the job run (also visible in WebUI at localhost:8088)

# Step 5: Check results
hadoop fs -ls /user/hadoop/output/              # see output files (part-r-00000 etc.)
hadoop fs -cat /user/hadoop/output/part-r-00000 # read the word counts
```

Expected output:

```
brown   1
fast    1
fox     2
hadoop  2
...
```

### Re-running the job (after changes)

```bash
hadoop fs -rm -r /user/hadoop/output/           # MUST delete output first
hadoop fs -rm -r /user/hadoop/input/            # clear input if changing data
hadoop fs -mkdir -p /user/hadoop/input          # recreate input dir
hadoop fs -put newdata.txt /user/hadoop/input/  # upload new data
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar \
  wordcount /user/hadoop/input /user/hadoop/output
```

---

## Phase 4 — Monitor Jobs

### While a job is running

```bash
hadoop job -list                               # see all running jobs + map/reduce %
yarn application -list                         # same but via YARN
yarn application -list -appStates RUNNING      # only active ones
```

### Check job status by ID

```bash
# Get the job ID from "hadoop job -list" first
hadoop job -status job_1704883200_0001
```

### Kill a stuck/wrong job

```bash
hadoop job -kill job_1704883200_0001           # via MapReduce
yarn application -kill application_1704883200_0001  # via YARN
```

### After job finishes — verify results

```bash
hadoop fs -ls /user/hadoop/output/             # list output files
hadoop fs -cat /user/hadoop/output/part-r-00000 | wc -l    # count output rows
hadoop fs -getmerge /user/hadoop/output/ result.txt         # merge all parts
wc -l result.txt                               # final count check
```

---

## Phase 5 — Reading Logs (Debugging)

When jobs fail, logs are your only clue.

### Get logs for a specific application

```bash
yarn logs -applicationId application_1704883200_0001
yarn logs -applicationId application_1704883200_0001 | grep -i "error"
yarn logs -applicationId application_1704883200_0001 | grep -i "exception"
```

### Hadoop daemon logs (stored on disk)

```bash
ls -lh $HADOOP_HOME/logs/                            # list all log files
tail -100 $HADOOP_HOME/logs/hadoop-*-namenode-*.log  # last 100 lines of namenode log
tail -100 $HADOOP_HOME/logs/yarn-*-resourcemanager-*.log
grep -i "error" $HADOOP_HOME/logs/hadoop-*.log       # search all hadoop logs for errors
grep -i "exception" $HADOOP_HOME/logs/yarn-*.log     # exceptions in yarn logs
```

### Live log watching (while starting cluster or a job)

```bash
tail -f $HADOOP_HOME/logs/hadoop-*-namenode-*.log    # watch namenode live
tail -f $HADOOP_HOME/logs/yarn-*-resourcemanager-*.log
```

---

## Phase 6 — Working with Real Data Files

This is the actual day-to-day file workflow before and after Hadoop jobs.

### Preparing data before upload

```bash
wc -l bigdata.csv                              # count rows — know your input
head -5 bigdata.csv                            # check structure/headers
tail -5 bigdata.csv                            # check end of file
du -h bigdata.csv                              # check file size

# If file is huge, split it first
split -l 500000 bigdata.csv chunk_             # split into 500k line chunks
ls -lh chunk_*                                 # verify chunks created
wc -l chunk_*                                  # verify each chunk row count

# Upload all chunks to HDFS
hadoop fs -put chunk_* /user/hadoop/input/
hadoop fs -ls /user/hadoop/input/              # confirm all uploaded
```

### Validating data after job

```bash
hadoop fs -getmerge /user/hadoop/output/ final.csv   # merge all output parts
wc -l bigdata.csv                                    # original input count
wc -l final.csv                                      # output count — should match (or know why not)
head -10 final.csv                                   # check output looks right
grep -i "null\|error\|nan" final.csv | wc -l         # check for bad records
```

### Config files you'll need to read often

```bash
cat $HADOOP_HOME/etc/hadoop/core-site.xml      # main settings (namenode address etc.)
cat $HADOOP_HOME/etc/hadoop/hdfs-site.xml      # HDFS settings (replication factor etc.)
cat $HADOOP_HOME/etc/hadoop/mapred-site.xml    # MapReduce settings
cat $HADOOP_HOME/etc/hadoop/yarn-site.xml      # YARN resource settings
cat $HADOOP_HOME/etc/hadoop/hadoop-env.sh      # JAVA_HOME and env settings
```

---

## Phase 7 — Cluster Info & Health Checks

Run these regularly to understand what's happening on the cluster:

```bash
hdfs dfsadmin -report                          # full HDFS health report
hdfs dfsadmin -safemode get                    # check if namenode is in safe mode (blocks writes)
yarn node -list                                # list all nodes and their status
yarn node -list -showDetails                   # detailed node info (memory, CPU, containers)
hadoop version                                 # check hadoop version
hadoop checknative                             # check native library support
```

> ⚠️ **Safe mode:** If NameNode just restarted, it enters "safe mode" temporarily and HDFS is read-only. Wait for it to exit automatically, or force it:
> 
> ```bash
> hdfs dfsadmin -safemode leave
> ```

---

## Useful Combos (Pipe Chains You'll Use All the Time)

```bash
# Find errors in logs across ALL log files at once
grep -r -i "error" $HADOOP_HOME/logs/ | tail -50

# Check if a specific file exists on HDFS
hadoop fs -ls /user/hadoop/data/ | grep "myfile"

# Count total files in an HDFS directory
hadoop fs -ls /user/hadoop/input/ | wc -l

# See output of job without downloading, with line numbers
hadoop fs -cat /user/hadoop/output/part-r-00000 | cat -n | head -30

# Quick data validation: compare input vs output row count
echo "Input:  $(hadoop fs -cat /user/hadoop/input/data.txt | wc -l)"
echo "Output: $(hadoop fs -cat /user/hadoop/output/part-r-00000 | wc -l)"
```

---

## The Daily Workflow (What You'll Actually Do Every Day)

```
1.  docker exec -it <container> bash          → get into hadoop
2.  jps                                       → verify cluster is healthy
3.  hadoop fs -mkdir -p /user/hadoop/input    → create input dir
4.  wc -l localfile.csv                       → check input size
5.  hadoop fs -put localfile.csv /user/hadoop/input/   → upload data
6.  hadoop fs -ls /user/hadoop/input/         → confirm upload
7.  hadoop fs -rm -r /user/hadoop/output/     → clear old output
8.  hadoop jar examples.jar wordcount /user/hadoop/input /user/hadoop/output  → run job
9.  yarn application -list                    → monitor while running
10. hadoop fs -ls /user/hadoop/output/        → check output files exist
11. hadoop fs -getmerge /user/hadoop/output/ result.txt  → merge results
12. wc -l result.txt && head -20 result.txt   → validate output
```

---

## Quick Reference Card

|Task|Command|
|---|---|
|Check cluster running|`jps`|
|List HDFS files|`hadoop fs -ls /path/`|
|Upload to HDFS|`hadoop fs -put local.txt /hdfs/path/`|
|Download from HDFS|`hadoop fs -get /hdfs/path/ local/`|
|Merge output parts|`hadoop fs -getmerge /output/ merged.txt`|
|Delete HDFS folder|`hadoop fs -rm -r /path/`|
|Run example job|`hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar wordcount /input /output`|
|Check running jobs|`yarn application -list`|
|Kill a job|`hadoop job -kill <job_id>`|
|Get job logs|`yarn logs -applicationId <app_id>`|
|HDFS health report|`hdfs dfsadmin -report`|
|Check disk space|`hadoop fs -df -h`|
|Exit safe mode|`hdfs dfsadmin -safemode leave`|

---

> **Next after this:** Learn to write your own MapReduce Java program, then move to Hive (SQL on Hadoop) and Spark (faster than MapReduce).