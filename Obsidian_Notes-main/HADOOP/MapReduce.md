**Solves**
- Provides a simple programming model (Map + Reduce) that hides distributed systems complexity and ==scales to thousands of nodes.==
    

**How it works (high level)**
- Input ==split== → map tasks ==process splits== → ==shuffle & sort== → ==reduce== tasks aggregate results. MapReduce jobs are batch-oriented and typically write intermediate results to disk between stages.

**Drawbacks & trade-offs**

- **Disk-heavy** ==(writes to disk between map/reduce)== → high I/O overhead and high latency for iterative or interactive workloads.
- **Rigid two-stage model** — awkward for complex DAGs (multiple steps) and streaming or iterative algorithms.
    

**Modern alternatives / evolution**

- ==**Apache Spark**==: keeps data in-memory and supports DAGs, iterative algorithms, streaming APIs.