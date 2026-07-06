### Main Types of Data Models (high-level categories):

1. **Relational Model**
    
    - Data stored in **tables** (rows = records, columns = attributes).
        
    - Relationships via **keys** (primary/foreign).
        
    - Query using **SQL**.
        
    - Example: MySQL, PostgreSQL.
        
2. **Document Model**
    
    - Data stored in **documents** (like ==JSON objects==).
        
    - Flexible schema: each record may have different fields.
        
    - Example: MongoDB, CouchDB.
        
3. **Key–Value Model**
    
    - Simplest: just a **key** and its **value** (like a ==dictionary or hashmap==).
        
    - Very fast for lookups.
        
    - Example: Redis, DynamoDB (in KV mode).
        
4. **Graph Model**
    
    - Data as **==nodes==** (entities) and **==edges==** (relationships).
        
    - Perfect for connected data (social networks, fraud detection).
        
    - Example: Neo4j, Amazon Neptune.