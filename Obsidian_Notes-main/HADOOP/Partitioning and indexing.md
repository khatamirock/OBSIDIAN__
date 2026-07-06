

They’re both about making ==queries faster== — but they work at ==different levels.==

Partitioning (==physical== layout)
- Split data into disjoint files/directories by a key (e.g., `dt=2026-03-01`, `country=bd`).
- Good for pruning entire partitions so the engine reads fewer files.
    
- Pitfall: ==too many partitions → many small files==; 


Indexing (lookup acceleration ==inside files/tables==)
- Structures to find rows quickly without scanning everything. Examples:
    - **B-tree / B+tree**: classic DB index for order and range queries.
    - **Inverted index**: for full-text search (maps token → document list).
    - **Bloom filter**: probabilistic “may-exist” test useful for data skipping in Parquet.
    - **Min/Max statistics**: column block-level stats in Parquet/ORC used for skipping row groups.
        
How they fit together
- Partitioning ==prunes files==; indexing prunes ==inside files==. Use both for best performance.