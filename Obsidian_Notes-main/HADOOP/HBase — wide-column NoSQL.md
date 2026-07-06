What it solves
- Low-latency random reads/writes at scale (==very large sparse tables, time-series==). 
  It provides ==real-time access== over data stored on HDFS.

How it works 
- HBase uses ==HFiles on HDFS for storage==; 
- RegionServers serve ranges (“regions”). A Master manages region assignment. 
  It’s modeled after Google Bigtable. (Compare trade-offs vs ==Cassandra==)

**Modern alternatives / evolution**
- Cloud-managed key-value  (Bigtable, ==DynamoDB==, Cosmos)

