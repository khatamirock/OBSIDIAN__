

==SOLVES:== Stores very large files across many commodity machines, tolerates node failure via block replication.


**How it works (high level)**

- Files are split into ==blocks==; blocks stored on DataNodes. 
- A ==single NameNode holds filesystem metadata== (file→block mapping) 
  and controls replication decisions; 
- DataNodes send ==heartbeats & blockreports==. 
  This central metadata design is key to HDFS behavior


**Drawbacks & trade-offs**

- **Single metadata master (NameNode)**: simpler but historically ==a single point of failure== (mitigations exist with HA NameNode).
- **Not optimized for millions of tiny files** — metadata explosion.


**Modern alternatives / evolution**
- Object stores (==S3, GCS, Azure Blob==) replaced on-prem HDFS
