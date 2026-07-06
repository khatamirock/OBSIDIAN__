## Types of Integrity Constraints

1. **Domain Constraint**
    
    - Ensures that attribute values come from a **valid set of values** (domain).
        
    - Example: `Age INT CHECK (Age >= 0 AND Age <= 150)` → no negative ages.
        
2. **Entity Integrity**
    
    - Every table must have a **primary key**.
        
    - Primary key values must be **unique** and **NOT NULL**.
        
    - Example: StudentID in `Students(StudentID, Name, Age)` must always exist and be unique.
        
3. **Referential Integrity**
    
    - A **foreign key** in one table must match a **primary key** in another (or be NULL if allowed).
        
    - Prevents “dangling references.”
        
    - Example: If `Enrollments(StudentID)` references `Students(StudentID)`, you cannot enroll a student who doesn’t exist in Students.
        
4. **Key Constraint**
    
    - No two tuples (rows) in a relation can have the same value for a **candidate key**.
        
    - Example: Two employees cannot have the same EmployeeID.
        
5. **General Constraints (User-defined)**
    
    - Custom rules defined using **CHECK**, triggers, or stored procedures.
        
    - Example: `Salary > 0` or `StartDate <= EndDate`.
        

---

## Why Integrity Constraints Matter

- Prevent **data anomalies** (like duplicates, invalid references, impossible values).
    
- Maintain **consistency** across multiple tables.
    
- Enforce **business rules** automatically.
    

---

👉 In exams/interviews, you usually need to mention **Domain, Entity, Referential, and Key constraints** as the four main ones.

Do you want me to also show you **SQL examples** for each constraint so it’s crystal clear?