
- **Data warehouse** — ==structured==, schema-on-write, curated for BI/analytics with strong governance, indexes, and performance (typical examples: Redshift, Snowflake).
    
- **Data lake** — stores ==raw/unstructured==/structured data ==cheaply== (object stores/HDFS), schema-on-read. Flexible for data science but historically lacks transactional guarantees and consistent metadata.
    
- **Lakehouse** — attempts to ==combine both==: open table formats (Iceberg/Delta/Hudi) + object storage deliver ACID-like semantics, time-travel, and performant analytics across engines (SQL engines, Spark, Flink). 
  Lakehouses give the flexibility of lakes with many warehouse features