**Solves**
- Lets analysts use SQL to query data stored in HDFS (or object stores) by translating ==**SQL into MapReduce**==, Tez, or Spark jobs.

How it works
- SQL statements are ==parsed into logical plans, optimized, and executed== via execution engines (originally MapReduce; later Tez or Spark backends). Metadata about tables/partitions lives in the Hive Metastore.

**Latest Iterations:**
- **Presto/==Trino==**, **Spark SQL**
