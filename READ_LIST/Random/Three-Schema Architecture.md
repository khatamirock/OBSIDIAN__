## Three-Schema Architecture (ANSI/SPARC Model)

It’s a way to **separate the database into three layers** so that changes in one layer don’t break the others.

### 1. **Internal Schema** (Storage Level)

- Lowest level — describes **how data is physically stored**.
    
- Deals with **files, indexes, data blocks, access paths**.
    
- Example:
    
    - A table row stored as a record in a disk page.
        
    - Using a B+ tree index on `StudentID`.
        

👉 Think: **The blueprint of shelves inside a library** (how/where books are kept).

---

### 2. **Conceptual Schema** (Logical Level)

- Middle layer — describes the **entire logical structure** of the database for the organization.
    
- Defines **entities, attributes, relationships, constraints**.
    
- Independent of physical storage.
    
- Example:
    
    - Tables: `Students(StudentID, Name, DeptID)`, `Departments(DeptID, DeptName)`
        
    - Relationships: Student belongs to a Department.
        

👉 Think: **The library catalog** — it lists what books exist, but not how they’re arranged on shelves.

---

### 3. **External Schema** (View Level)

- Highest layer — how **individual users or applications see the data**.
    
- Can be **different for different users** (customized views).
    
- Example:
    
    - Student portal view: shows only `Name, Courses, Grades`.
        
    - Admin view: sees full student info including fees, contact.
        

👉 Think: **A student’s library card portal** — shows _only the books they borrowed_, not the whole library.

---

## Why Important? (Advantages)

- **Data Independence**:
    
    - _Logical independence_: Change in conceptual schema (e.g., add a new attribute) doesn’t affect external views.
        
    - _Physical independence_: Change in internal schema (e.g., new indexing) doesn’t affect logical schema.
        
- Security: Users see only what they need (via external schemas).
    
- Flexibility: Easy to reorganize storage or extend schema without breaking apps.
    

---

✅ In exams, write:  
**External → Conceptual → Internal** (top to bottom), with **data independence** as the key advantage.
