### links:
1. Lec-22: Finding Closure of Functional dependency in DBMS | Easiest & Simplest way (gate smahser)
	1. for understanding the candidate key,
	2. super key,
	3. Functional dependency
	4. closure method
### **Keys Definitions in DBMS**
#### **Keys in Database: Super Key, Candidate Key, and Primary Key**

Let’s break down these concepts using a **complex example** of a university database table for **Online Course Enrollment**:

##### **Table Schema**:  
| **EnrollmentID** | **StudentID** | **CourseCode** | **ProfessorID** | **Semester** | **EnrollmentTimestamp** |  
|-------------------|---------------|----------------|------------------|--------------|--------------------------|  
| E001              | S101          | CS101          | P001             | Fall-2023    | 2023-08-25 09:15:00      |  
| E002              | S102          | CS101          | P001             | Fall-2023    | 2023-08-25 09:16:30      |  
| E003              | S101          | MATH201        | P002             | Fall-2023    | 2023-08-26 10:00:00      |  

---

###### **1. Super Key**  
A **super key** is ==*any set of attributes== that uniquely identifies a record*. It may ==include redundant attributes.==  

**Examples**:  
- `{EnrollmentID}`  
- `{StudentID, CourseCode, Semester}`  
- `{StudentID, EnrollmentTimestamp}`  
- `{ProfessorID, CourseCode, Semester, EnrollmentTimestamp}`  

**Why?**  
- `EnrollmentID` alone is unique.  
- `StudentID + CourseCode + Semester` works if a student can’t enroll in the same course twice in one semester.  
- `EnrollmentTimestamp` might be unique but is impractical for querying.  

---

###### **2. Candidate Key**  
A **candidate key** is a ==*minimal super key==*           $\to$       ==no redundant attributes.==  

**Valid Candidate Keys**:  
- `{EnrollmentID}`  
- `{StudentID, CourseCode, Semester}` (if unique)  
- `{EnrollmentTimestamp}` (if timestamps are enforced to be unique)  

**Invalid Super Keys (Non-Candidate)**:  
- `{StudentID, CourseCode, Semester, ProfessorID}` → Redundant (ProfessorID isn’t needed for uniqueness).  
- `{EnrollmentID, StudentID}` → Redundant (EnrollmentID alone suffices).  

---

###### **3. Primary Key**  
The **primary key** is the ==*chosen candidate key*== to uniquely identify records.  

**Common Choice**:  
- `EnrollmentID` (simple, guaranteed unique).  

**Alternative**:  
- `{StudentID, CourseCode, Semester}` if the university ensures no duplicate enrollments.  


######  4. **UNIQUE key** ( Can be ==NULL==):

1. In a School System:
- Student ID (Primary Key) - Must be unique and can't be empty
- Email Address (Unique Key) - Must be unique but a student might not have one yet
- Phone Number (Unique Key) - Must be unique but could be updated if changed


1. In a Library System:
- ISBN numbers (Unique Key) - Each book has a unique ISBN, but you might have old books without ISBN
- Book ID (Primary Key) - Must have one for every book
- Library Card Number (Unique Key) - Each member has a unique number, but it can be changed if card is lost
-
---

##### **Why This Matters**  
2. **Super Keys** are broad but inefficient (e.g., `{StudentID, CourseCode, Semester, EnrollmentTimestamp}`).  
3. **Candidate Keys** eliminate redundancy (e.g., `{EnrollmentID}` or `{StudentID, CourseCode, Semester}`).  
4. **Primary Key** is selected for efficiency and usability (e.g., `EnrollmentID` for quick lookups).  

---

##### **Real-World Complexity**  
Imagine the university allows **waitlisted enrollments** with the same `StudentID + CourseCode + Semester`. Now:  
- `{StudentID, CourseCode, Semester}` is no longer a candidate key.  
- A new candidate key emerges: `{StudentID, CourseCode, Semester, EnrollmentType}` (e.g., "Waitlisted" vs. "Confirmed").  

**Revised Candidate Keys**:  
- `{EnrollmentID}`  
- `{StudentID, CourseCode, Semester, EnrollmentType}`  

---

#### **Summary Table**  
| **Key Type**      | **Definition**                                           | **Example**                                           |     |
| ----------------- | -------------------------------------------------------- | ----------------------------------------------------- | --- |
| **Super Key**     | Any set of attributes that uniquely identifies a record. | `{EnrollmentID}`, `{StudentID, CourseCode, Semester}` |     |
| **Candidate Key** | ==Minimal super key== (no redundant attributes).         | `{EnrollmentID}`                                      |     |
| **Primary Key**   | ==Chosen candidate== key for unique identification.      | `EnrollmentID` (selected for simplicity).             |     |
#look
==this is in short **ACTUALLY**  **Super Key**  $=>$ **Candidate Key** $=>$  **Primary Key==**   ( S $\to$ C $\to$ P )
                    each is chosen from the **upper layer**!!!!


---


**Answer:**  
The correct answer is **(c) Min 2 and max 3**.  
### **Er- Diagram & Number of tables  
`number of tables` `how many tables`

---

==The **number of tables** depends on the **cardinality** of the relationship (1:1, 1:N, or M:N), *not* the participation constraints (partial/total).==  
**Partial participation only affects whether foreign keys can be `NULL`, *not* the number of tables.**  

---




| ![[1_1DB.png]] |     |
| ------------------------------------ | --- |
| ![[1_mDB.png]] |     |
| ![[m_1DB.png]] |     |
| ![[n_mDB.png]] |     |


#### **Examples with Tables**  
Let’s use two entities: **`Student`** and **`Course`**, with a relationship **`Enrolls`**.  
==**Partial participation**:==  
- Not all students enroll in courses.  
- Not all courses have enrolled students.  

##### **Case 1: One-to-Many (1:N) Relationship**  
**Scenario**:  
- A student can enroll in **many courses**, but a course can have **only one student** (==unlikely, but for example)==.  
- **Tables required**: **2** (no third table needed).  

**Table Structure**:  
1. **`Student`** table (stores students):  
   | StudentID (PK) | Name  |  
   |----------------|-------|  
   | 1                    | Alice |  
   | 2                    | Bob   |  

2. **`Course`** table (stores courses + foreign key for the enrolling student):  
   | CourseID (PK) | StudentID (FK, nullable) | CourseName |  
   |---------------|---------------------------|------------|  
   | C101             | 1 (Alice)                         | Math       |  
   | C102            | NULL (no student)          | Physics    |  
    -------------------------------------------------------
**Explanation**:  
- Partial participation allows `StudentID` in `Course` to be `NULL` (e.g., Bob hasn’t enrolled in any course).  
- **No third table** – t==he relationship is embedded in the "many" side (`Course`).==  

---

##### **Case 2: Many-to-Many (M:N) Relationship**  
**Scenario**:  
- A student can enroll in **many courses**, and a course can have **many students**.  
- **Tables required**: **3** (third table for the relationship).  

**Table Structure**:  
3. **`Student`** table:  
   | StudentID (PK) | Name  |  
   |----------------|-------|  
   | 1                    | Alice |  
   | 2                    | Bob   |  

4. **`Course`** table:  
   | CourseID (PK) | CourseName |  
   |---------------|------------|  
   | C101          | Math       |  
   | C102          | Physics    |  

5. **`Enrolls`** table (relationship table):  
   | StudentID (FK) | CourseID (FK) |  
   |----------------|----------------|  
   | 1              | C101           |  
   | 1              | C102           |  
   | 2              | C101           |  

**Explanation**:  
- Partial participation allows:  
  - Students like Bob to exist without enrolling in any course.  
  - Courses like Physics (`C102`) to exist without students.  
- **Third table** is mandatory for M:N relationships, regardless of participation constraints.  

---

##### **Key Takeaways**  
6. **Min Tables = 2** (for 1:1 or 1:N relationships).  
   - Foreign keys are embedded in one of the entity tables.  
   - Example: `Course` table has a nullable `StudentID` for 1:N.  
7. **Max Tables = 3** (for M:N relationships).  
   - A third table is always required to map the relationship.  
8. **Partial Participation ≠ More Tables**:  
   - It only allows `NULL` foreign keys.  

---

##### **Why Partial Participation Doesn’t Change Table Count**  
- **1:1 or 1:N**:  
  - Use 2 tables even with partial participation (foreign keys can be `NULL`).  
- **M:N**:  
  - Use 3 tables regardless of participation.  

---

##### **Summary**  
| **Relationship Type** | **Tables Required** | **Example**                  |  
|------------------------|---------------------|------------------------------|  
| **One-to-One (1:1)**   | 2                   | Student ↔ ID Card (partial)  |  
| **One-to-Many (1:N)**  | 2                   | Student ↔ Course (1:N)       |  
| **Many-to-Many (M:N)** | 3                   | Student ↔ Course (M:N)       |  

**The answer is (c) because:**  
- Minimum tables = 2 (for 1:1/1:N).  
- Maximum tables = 3 (for M:N).  
- Partial participation only affects `NULL` values, not table count.  

Let me know if you need more examples! 🚀
#### Here are some practice questions  **ER diagrams** and **relational database design**:

---

##### **Question 1**  
**Scenario**:  
A hospital database has two entities: **`Patient`** and **`Doctor`**. A patient is assigned to exactly one doctor, and a doctor can have many patients. Both entities have **total participation** in the relationship.  
**How many tables are required?**  
(a) 2  
(b) 3  
(c) 1  
(d) 4  

---

##### **Question 2**  
**Scenario**:  
In a university database, a **`Student`** can enroll in multiple **`Courses`**, and a course can have multiple students. The relationship **`Enrolls`** has an attribute **`grade`**.  
**What is the correct table design?**  
(a) 2 tables (`Student`, `Course`) with `grade` in `Student`.  
(b) 3 tables (`Student`, `Course`, `Enrolls`) with `grade` in `Enrolls`.  
(c) 1 table combining all data.  
(d) 2 tables (`Student`, `Course`) with `grade` in `Course`.  

---

##### **Question 3**  
**Scenario**:  
A company database has **`Employee`** and **`Dependent`**. A dependent cannot exist without an employee.  
**What type of entity is `Dependent`?**  
(a) Strong entity  
(b) Weak entity  
(c) Associative entity  
(d) Composite entity  

---

##### **Question 4**  
**Scenario**:  
A library database has **`Book`** and **`Author`**. A book can have multiple authors, and an author can write multiple books.  
**What is the relationship type and minimum tables required?**  
(a) 1:1, 2 tables  
(b) 1:N, 3 tables  
(c) M:N, 3 tables  
(d) M:N, 2 tables  

---

##### **Question 5**  
**Scenario**:  
A car rental system has three entities: **`Car`**, **`Customer`**, and **`Rental`**. Each rental involves one car, one customer, and a `rental_date`.  
**What is the relationship type and tables required?**  
(a) Ternary relationship, 3 tables  
(b) Binary relationship, 4 tables  
(c) Ternary relationship, 4 tables  
(d) Binary relationship, 3 tables  

---

##### **Question 6**  
**Scenario**:  
In an ER diagram, a **`Student`** has a **`StudentID`** and a **`Name`**. A **`Course`** has a **`CourseCode`** and **`Title`**. The relationship **`Takes`** has no attributes. Both entities have **partial participation**.  
**What is the minimum number of tables required if the relationship is M:N?**  
(a) 2  
(b) 3  
(c) 4  
(d) 1  

---

##### **Question 7**  
**Scenario**:  
An entity **`Employee`** has a composite attribute **`Address`** (with `street`, `city`, `zip`).  
**How is this modeled in tables?**  
(a) Split `Address` into separate columns in the `Employee` table.  
(b) Create a new table for `Address`.  
(c) Store `Address` as a single JSON column.  
(d) Both (a) and (b) are valid.  

---

##### **Question 8**  
**Scenario**:  
A **`BankAccount`** entity has a **`account_number`** (primary key) and **`balance`**. A **`Transaction`** entity records deposits/withdrawals linked to an account.  
**What is the relationship type?**  
(a) 1:1  
(b) 1:N  
(c) M:N  
(d) Ternary  

---

##### **Answers**  
9. **(a) 2 tables**  
   - **`Doctor`** (DoctorID, ...) and **`Patient`** (PatientID, DoctorID (FK), ...). Total participation means `DoctorID` in `Patient` is NOT NULL.  

10. **(b) 3 tables**  
   - M:N relationships require a third table (`Enrolls`) to store the `grade` attribute.  

11. **(b) Weak entity**  
   - Depends on `Employee` for existence (identifying relationship).  

12. **(c) M:N, 3 tables**  
   - Books and authors have a many-to-many relationship. Tables: `Book`, `Author`, `Writes` (relationship table).  

13. **(a) Ternary relationship, 3 tables**  
   - Ternary relationships involve three entities. Tables: `Car`, `Customer`, `Rental` (with foreign keys for Car, Customer, and `rental_date`).  

14. **(b) 3 tables**  
   - M:N relationships always require 3 tables, regardless of participation constraints.  

15. **(d) Both (a) and (b) are valid**  
   - Composite attributes can be flattened into columns (a) or split into a separate table (b).  

16. **(b) 1:N**  
   - One account can have many transactions. Tables: `BankAccount` and `Transaction` (with `account_number` as FK).  
 
---


#### Shortcut for Exams: Ques 60

17. **L==ook for junction tables**==: If a table has **two foreign keys** (e.g., OrderNumber and ProductID in Orderline), it typically mediates a **many-to-many** relationship.
    
18. **Foreign key count**:
    
    - **One foreign key** → Likely one-to-many.
    - **Two foreign keys** → Likely many-to-many.
19. **Real-world logic**:
    - Can one order have multiple products? → Yes.
    - Can one product be in multiple orders? → Yes.  
        → Many-to-Many.


### **SQL Command Categories**

| **Category**                           | **Commands**                                                        | **Full Form**                | **Purpose**                             | **Examples**                                         |
| -------------------------------------- | ------------------------------------------------------------------- | ---------------------------- | --------------------------------------- | ---------------------------------------------------- |
| **DDL**                                | `DROP`, `RENAME`, `CREATE`, `ALTER`,`TRUNCATE`  $\to$ (==DR. CAT==) | Data Definition Language     | Defines/modifies database **structure** | `CREATE TABLE`, `ALTER COLUMN`, `DROP DATABASE`      |
| **DM**(idus)**L**                      | `MERGE`, `INSERT` , `DELETE`,`UPDATE` `SELECT`,  $\to$  (==MIDUS==) | Data Manipulation Language   | Manipulates data **within tables**      | `UPDATE users SET name='John'`, `INSERT INTO orders` |
| **DCL**  (Data Control Language)       | `GRANT`, `REVOKE`                                                   | Data Control Language        | Controls **access/permissions**         | `GRANT SELECT ON employees TO user1`                 |
| **TCL** (Transaction Control Language) | `COMMIT`, `ROLLBACK`, `SAVEPOINT`                                   | Transaction Control Language | Manages **transactions**                | `COMMIT`, `ROLLBACK TO SAVEPOINT`                    |
>SQL statement must be required to end the transaction. List the SQL statements, required to end the transaction and also write their functions.*

- **Use `DELETE`** if you need to ==remove specific records== and may want to roll back.
- **Use `TRUNCATE`** if you need to ==quickly clear all data== but keep the structure.
- **Use `DROP`** if you ==no== longer ==need the table== at all.
---

### The SQL Problem 25:

```sql
SELECT ROUND(232.420, -2) AS RoundValue;
```

#### **Explanation of the ROUND Function**:

The **`ROUND`** function in SQL is used to round a number to a specified number of decimal places or significant digits. Its syntax is:

```sql
ROUND(number, precision)
```

- **`number`**: The value to be rounded.
- **`precision`**: The number of digits to round to:
    - A **positive** precision means rounding after the decimal point.
    - A ==**negative** precision means rounding== to the ==left of the decimal point== (to the nearest tens, hundreds, etc.).

---

#### **Breaking Down the Query**:

- **Number**: `232.420`
- **Precision**: `-2`

#### **What Does `-2` Mean?**

A precision of `-2` means:

- Round the number to **two places to the left of the decimal point**.
- This effectively rounds the number to the nearest **hundred**.

---

#### **Step-by-Step Calculation**:

20. Original number: `232.420`
21. Identify the place to round to: Two digits to the left of the decimal is the **hundreds place**.
22. Round `232.420` to the nearest hundred:
    - Look at the **tens place** (`3`). Since it’s less than 5, **round down**.
    - ==The result is **200**.==

---

#### **Output**:

The query will return:

```
RoundValue
-----------
200
```

---

#### **Additional Examples**:

23. **`ROUND(345.678, -1)`**:
    
    - Round to the nearest **ten**.
    - Result: **350**.
24. **`ROUND(789.456, 1)`**:
    
    - Round to **one decimal place**.
    - Result: **789.5**.
25. **`ROUND(1234.567, -3)`**:
    
    - Round to the nearest **thousand**.
    - Result: **1000**.

Let me know if you'd like more examples or clarification! 😊





 
### **Explanation of Each Option of prob 5:**

#### **a) Lsps -a**

- **Command**: `lsps -a`
- This command is specific to **AIX systems**, not Linux. It displays details about paging spaces, which are equivalent to swap spaces in AIX.

---

#### **b) Swapinfo -m**

- **Command**: `swapinfo -m`
- This command is used in **HP-UX systems**, not Linux. It shows swap space usage in megabytes.

---

#### **c) Swapon -s**

- **Command**: `swapon -s`
- This is the correct answer for **Linux OS**.
- It shows information about active swap spaces, including their file/device names, size, used space, and priority.
- Example output:
    
    ```
    Filename                                Type        Size        Used    Priority
    /swapfile                               file        2048        512     -1
    ```
    

---

#### **d) Swap -l and Swap -s**

- **Command**: `swap -l` and `swap -s`
- These commands are **Solaris-specific**, not Linux.
- `swap -l`: Lists active swap areas.
- `swap -s`: Displays summary information about swap usage.

---

#### **Correct Answer:**

- **(c) Swapon -s**

---

#### **Additional Commands to Monitor Swap Space in Linux:**

26. **`free -h`**:
    
    - Shows memory usage (RAM and swap) in a human-readable format.
    - Output:
        
        ```
        total        used        free      shared  buff/cache   available
        Mem:          7.8Gi       2.3Gi       3.9Gi       100Mi       1.6Gi       5.2Gi
        Swap:         2.0Gi       512Mi       1.5Gi
        ```
        
27. **`cat /proc/swaps`**:
    
    - Displays swap information from the system’s `/proc` file.
28. **`vmstat`**:
    
    - Provides information about system performance, including swap usage.
    - Example: `vmstat -s` to display memory and swap stats.

---






### **Explanation of Functional Dependency (FD) with Examples**

#### **Functional Dependency (FD) Definition**

A **functional dependency** X→Y   in a database means that the value of attribute(s) X uniquely determines the value of attribute(s) Y.

- **Determinant (X)**: The attribute(s) that determine the value of another attribute.
    
- **Dependent (Y)**: The attribute(s) whose value is determined by X.
    

---

#### **Example from the Provided Table**

|**A**|**B**|
|---|---|
|1|ABC|
|2|DEF|
|3|GHI|
|4|JKL|

**Functional Dependency**: A→B

- **Determinant**: A.
- **Dependent**: B.
- **Explanation**: Each value of A uniquely determines B.
    - A=1→B=ABC
    - A=2→B=DEF, etc.
---

#### **Key Properties of Functional Dependencies**

29. **Uniqueness**: For a given X, there is **exactly one Y**.
    
30. **Transitivity**: If X→Y and Y→Z , then X→ Z.
    
31. **Reflexivity**: If Y⊆X  then X→Y 
    

---

#### **Real Example**
**Answer:**  
The correct answer is **(b) BD → CD**.  

---

##### **Explanation:**  
To determine which functional dependency (FD) is **not implied** by the given set, we compute the **closure** of the left-hand side (LHS) of each option. If the right-hand side (RHS) is in the closure, the FD is implied.  

##### **Given FDs:**  

$$
\begin{aligned}
32. ( A \rightarrow B )  \\
33. ( A \rightarrow C )  \\
34. ( CD \rightarrow E )  \\
35. ( B \rightarrow D )  \\
36. ( E \rightarrow A )  \\
\end{aligned}
$$

---

##### **Option-by-Option Analysis**  
**a) \( CD $\rightarrow$ AC \)**  
- Compute  ($CD^+$):  
$$
  - ( CD \rightarrow E ) (FD3) → ( CD^+ = CDE ).  
$$
$$
  - ( E \rightarrow A ) (FD5) → ( CD^+ = ACDE ).  
$$
$$
  - ( A \rightarrow B, A \rightarrow C ) (FD1, FD2) → ( CD^+ = ABCDE ).  
$$
$$
- ( AC \subseteq CD^+ ). \ Implied.  
$$

	**b) $BD \rightarrow CD$**  
	- Compute $BD^+$:  
	  - $B \rightarrow D$ (FD4) $\rightarrow BD^+ = BD$.  
	  - No FDs derive $C$ from $BD$.  
	- $CD \not\subseteq BD^+$. **Not Implied**.  
	
	**c) $BC \rightarrow CD$**  
	- Compute $BC^+$:  
	  - $B \rightarrow D$ (FD4) $\rightarrow BC^+ = BCD$  
	  - $CD \rightarrow E$ (FD3) $\rightarrow BC^+ = BCDE$  
	  - $E \rightarrow A$ (FD5) $\rightarrow BC^+ = ABCDE$  
	- $CD \subseteq BC^+$. **Implied**.  
	
	**d) $AC \rightarrow BC$**  
	- Compute $AC^+$:  
	  - $A \rightarrow B, A \rightarrow C$ (FD1, FD2) $\rightarrow AC^+ = ABC$  
	  - $B \rightarrow D$ (FD4) $\rightarrow AC^+ = ABCD$  
	  - $CD \rightarrow E$ (FD3) $\rightarrow AC^+ = ABCDE$  
	- $BC \subseteq AC^+$. **Implied**.

---

### RAID:
**(a) RAID-0** is correct because it uses **striping without parity**, maximizing read/write speed and storage efficiency (no redundancy overhead).  



#### **RAID Levels Explained**  

| **RAID Level** | **Structure**                                                                | **Key Features**                                                                                                                | **Use Case**                                    |     |
| -------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | --- |
| **RAID-0**     | **Striping** (data ==split across disks==).                                  | - **Fastest performance** (parallel read/write).<br>- ==**No redundancy** (no fault tolerance==).<br>- Minimum 2 disks.         | High-speed applications (e.g., video editing).  |     |
| **RAID-1**     | **Mirroring** (data ==duplicated across== disks).                            | - **Redundancy** (one disk failure tolerated).<br>- **Slower writes** (data written twice).<br>- Minimum 2 disks.               | Critical data requiring backup (e.g., servers). |     |
| **RAID-3**     | **==Byte-level== striping + dedicated parity  disk**.                        | - **Parity for redundancy** (single disk failure tolerance).<br>- **Parity bottleneck** (dedicated disk).<br>- Minimum 3 disks. | Rarely used; ==replaced by RAID-5/6.==          |     |
| **RAID-5**     | **==Block-level== striping + distributed parity**.                           | - **Balanced performance and redundancy**.<br>- Single disk failure tolerance.<br>- Minimum 3 disks.                            | General-purpose storage (e.g., file servers).   |     |
| **RAID-6**     | **Block-level striping + double distributed parity**.                        | - **Tolerates two disk failures**.<br>- Higher storage overhead.<br>- Minimum 4 disks.                                          | High-reliability needs (e.g., archival data).   |     |
| **RAID-10**    | **Combination of RAID-1 (mirroring) + RAID-0 (striping)**.                   | - **High performance + redundancy**.<br>- Tolerates multiple disk failures (per mirrored pair).<br>- Minimum 4 disks.           | Databases, enterprise applications.             |     |
| **RAID-20**    | **Non-standard** (likely a typo; could mean nested RAID like RAID-0+RAID-2). | - Hypothetical combination (not commonly used).<br>- Avoid assuming unless explicitly defined.                                  | Rarely tested; clarify context.                 |     |
 - parity is used for data **redundancy and fault** tolerance. When parity is implemented (such as in RAID 5 or RAID 6), the system calculates and stores extra information that can be used to reconstruct data if one or more drives fail
---

#### ==**Key Recognition Points for Exams**==  
37. **RAID-0**:  
   - **Keywords**: "==Striping==," "no redundancy," "fastest performance."  
38. **RAID-1**:  
   - **Keywords**: "==Mirroring==," "duplicate data," "50% storage efficiency."  
39. **RAID-3/5/6**:  
   - **Focus on ==parity**==:  
     - RAID-3: Dedicated parity disk.  
     - RAID-5: Distributed parity (single failure tolerance).  
     - RAID-6: Double parity (two failures tolerance).  
40. **RAID-10**:  
   - **Keywords**: =="Striping + mirroring," "best of RAID-0 and RAID-1."==  

---

#### **Why RAID-0 is the Fastest?**  
- **No Parity Overhead**: All disk space is used for data.  
- **Parallel Operations**: Data is split across disks, enabling simultaneous read/write.  
- **Trade-off**: No fault tolerance – one disk failure loses all data.  

**Example**:  
- Storing a 1 GB file across 2 disks in RAID-0:  
  - Each disk holds 500 MB.  
  - Both disks work in parallel, halving read/write time.  

---

#### **Exam Tips**  
- **RAID-0 vs. RAID-1**: RAID-0 is faster; RAID-1 is safer.  
- **RAID-5/6**: Use parity for redundancy; RAID-6 is more reliable but costlier.  
- **RAID-10**: Combines speed (striping) and safety (mirroring).  

#### **36. Explanation of RAID :**

RAID (Redundant Array of Independent Disks) provides **data protection** by employing one of the following techniques:

41. **Data Mirroring:**
    
    - Data is duplicated across multiple disks. If one disk fails, the copy on the other disk(s) ensures no data is lost.
    - Example: **RAID 1**.
42. **Parity:**
    
    - Parity bits are used to provide fault tolerance. Parity allows the system to recreate lost data if a disk fails by calculating based on the remaining data.
    - Example: **RAID 5, RAID 6**.

---

##### **Why Other Options Are Incorrect:**

##### **(b) Using either data mirroring or striping:**

- **Incorrect** because striping (used in **RAID 0**) does not provide data protection.
    - **Striping** improves performance by splitting data across multiple disks but offers no redundancy or fault tolerance.
    - If one disk fails, all data is lost.

---

##### **(c) Using high-quality disk drives:**

- **Incorrect** because:
    - While high-quality drives reduce the chance of failure, they **do not inherently provide data protection**.
    - RAID is designed to tolerate disk failures by redundancy mechanisms, regardless of the quality of the disk.

---

##### **(d) Using dedicated data protection hardware:**

- **Incorrect** because:
    - RAID does not rely on specialized hardware for data protection. Instead, it uses techniques like **mirroring** or **parity**.
    - Some RAID controllers may enhance performance, but data protection is still achieved through mirroring or parity.

---


### Star Schema
A **star schema** is a type of database design used in **data warehousing** to organize data in a way that makes it efficient for querying and analysis. It is called a "star" schema because the diagram looks like a star, with a **central fact table** surrounded by **dimension tables**.

---

#### **Components of a Star Schema:**

43. **Fact Table:**
    
    - The **==central== table** in the schema.
    - Contains **numerical metrics** (e.g., sales, revenue, quantity) that you want to analyze.
    - ==Includes **foreign keys** to connect with dimension tables.==
44. **Dimension Tables:**
    
    - Tables that provide ==**context** to the data in the fact table.==
    - Contain descriptive attributes (e.g., product name, customer name, region).
    - Examples: Product, Time, Customer.

---

#### **Relationship in a Star Schema:**

- The relationship between a **dimension table** and the **fact table** is typically **one-to-many**.  
    This means:
    - **One record in the dimension table** (e.g., one product or one customer) can be associated with **many records in the fact table** (e.g., many sales transactions).

---

##### **Answer to the Question:**

- The correct answer is: **(c) One-to-many**

----

### Normalization:
#### **Correct Answer: (d) Transitive Dependency**

---

#### **Explanation:**

- **Third Normal Form (3NF)** ensures that a table is in **Second Normal Form (2NF)** and that **no transitive dependencies** exist.
- **Transitive Dependency** occurs when a non-prime attribute depends on another non-prime attribute, indirectly depending on a primary key.

For example:

- Table: Student (StudentID → DepartmentID, DepartmentID → DepartmentName)
- Here, `DepartmentName` is transitively dependent on `StudentID` through `DepartmentID`. To resolve this, we separate `Department` into a new table.

---

#### **How to Recognize  Normal Forms:**

| **Normalization** | **Main Features**                                                                                                        | **Key Traits to Recognize**                                                                                   |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| **1NF**           | Eliminate ==repeating groups== and ensure all attributes are atomic (indivisible).                                       | - No arrays or nested values.- Data is stored in tabular form.- Each column contains a single value.          |
| **2NF**           | Be in 1NF and ==eliminate partial dependency== (no non-prime attribute depends only on part of a composite primary key). | - Look for == ==.- Ensure every non-prime attribute is fully functionally dependent on the whole primary key. |
| **3NF**           | Be in 2NF and ==eliminate transitive dependency==.                                                                       | - No non-prime attribute depends on another non-prime attribute.- Look for indirect dependencies.             |
| **BCNF**          | Be in 3NF and ensure every determinant is a candidate key.                                                               | - Check for functional dependencies.- Ensure no attribute determines a non-candidate key.                     |
| **4NF**           | Be in BCNF and eliminate multi-valued dependencies (MVDs).                                                               | - Look for attributes that are independent of each other but depend on the same key.                          |
| **5NF**           | Be in 4NF and eliminate join dependency.                                                                                 | - Check if the table can be decomposed into smaller tables without loss of information or redundancy.         |

---

##### **Quick Guide to Recognizing Normal Forms:**

45. **1NF:** Are there repeating groups or non-atomic columns? Fix them.
46. **2NF:** Are there attributes depending on part of a composite key? Fix partial dependencies.
47. **3NF:** Are there attributes depending on other non-prime attributes? Remove transitive dependencies.
48. **BCNF:** Does any attribute determine a non-candidate key? Ensure every determinant is a candidate key.
49. **4NF/5NF:** Are there multi-valued dependencies or unnecessary join dependencies? Eliminate them.

---




#### **Normalization of `MusicFestivalManagement` Table** -an elaborate example 

##### **Step 1: First Normal Form (1NF)**  
**Original Table**: 

| ArtistID | ArtistName      | BandGenre        | RecordLabel           | LabelCountry | StageID | StageName           | StageCapacity | PerformanceTime | TicketPrice |
| -------- | --------------- | ---------------- | --------------------- | ------------ | ------- | ------------------- | ------------- | --------------- | ----------- |
| A001     | Luna Eclipse    | Alternative Rock | Moonlight Records     | UK           | S01     | Main Stage          | 50000         | 20:00           | 150         |
| A002     | Rhythm Rebels   | Indie Pop        | Soundwave Productions | USA          | S02     | Electronic Pavilion | 25000         | 18:30           | 120         |
| A003     | Jazz Collective | Jazz             | Global Harmony        | France       | S01     | Main Stage          | 50000         | 22:15           | 175         |

**1NF Compliance**:

**1NF Compliance**:  
- Already in 1NF (atomic values, no repeating groups).  

---

##### **Step 2: Second Normal Form (2NF)**  
Consider the following table:

| **StudentID** | **CourseID** | **CourseName** | **Instructor** |
| ------------- | ------------ | -------------- | -------------- |
| 101           | CSE101       | Programming    | Dr. Smith      |
| 101           | MAT101       | Mathematics    | Dr. Johnson    |
| 102           | CSE101       | Programming    | Dr. Smith      |
| 102           | PHY101       | Physics        | Dr. Brown      |

- **Composite Primary Key:**  {StudentID, CourseID}
#### 🧠 Real-world problems this causes:

##### 🔁 **Redundancy**:

- “CSE101 → Programming → Dr. Smith” is repeated for every student who takes that course.
    
- Waste of space and inefficient.
    

##### ✏️ **Update anomalies**:

- If the instructor of CSE101 changes (e.g., to Dr. Allen), you have to update **every row** where a student took CSE101.
    
- Easy to forget some rows — leading to incorrect data.
    

##### ⚠️ **Inconsistency**:

- Some rows might say “CSE101 → Dr. Smith”, others say “CSE101 → Dr. Allen” — **which one is right?**
    
- Database becomes unreliable.
    

##### 🚫 **Missing information**:

- If no student enrolls in a course, you **can’t store the course name or instructor**, because no row exists y
#### Dependencies:

50. $( \text{CourseName} ) and ( \text{Instructor} )$ depend only on **CourseID**, not on the entire composite key $( \text{(StudentID, CourseID)} )$.
    - Example: The course "CSE101" is always "Programming" and taught by "Dr. Smith," regardless of the student.
    - This is a **Partial Dependency** because $CourseName$ and ( $\text{Instructor}$ ) depend only on part of the composite key $CourseID$.

---

#### **Solution (Normalization to 2NF):**

To remove partial dependencies, we split the table into two tables:

51. **Student-Course Table (StudentID, CourseID):**

| StudentID | CourseID |
| --------- | -------- |
| 101       | CSE 101  |
| 101       | MAT101   |
| 102       | CSE102   |
| 102       | PHY101   |
 
52. **Course Table (CourseID, CourseName, Instructor):**
    |**CourseID** | **CourseName**      |**Instructor** |
    |CSE101    |   Programming    |   Dr. Smith |
    |MAT101   |    Mathematics   |    Dr. Johnson |
    |PHY101   |    Physics            |     Dr. Brown | 
    

Now, ( $\text{CourseName}$ ) and ( $\text{Instructor}$) depend fully on ( $\text{CourseID}$ ), while the student-course relationship is maintained in the first table. This is in **2NF**.

---

##### **Step 3: Third Normal Form (3NF)**  
- **Transitive Dependency** occurs when a ==non-prime attribute== depends on ==another non-prime attribute,== **which** ==in turn depends on the primary key==.
- It violates **Third Normal Form (3NF)**, which requires that there be no transitive dependencies; non-prime attributes must depend only on the primary key.

---

#### **Example of Transitive Dependency:**

Consider the following table:

|**EmployeeID**|**DepartmentID**|**DepartmentName**|**Manager**|
|---|---|---|---|
|1|101|HR|Alice|
|2|102|IT|Bob|
|3|101|HR|Alice|
|4|103|Finance|Charlie|

- **Primary Key:** ( $\text{EmployeeID}$ )

#### Dependencies:

53. $( \text{DepartmentName} ) and ( \text{Manager} )$ depend on $( \text{DepartmentID} )$, ==not directly== on ( $\text{EmployeeID}$ ).
    
    - $(\text{DepartmentID} \to \text{DepartmentName}, \text{Manager} )$
    - $( \text{EmployeeID} \to \text{DepartmentID} )$
    - Therefore, $( \text{EmployeeID} \to \text{DepartmentName}$, $\text{Manager} ) via ( \text{DepartmentID}$ ).
    
    T==his is a **Transitive Dependency** because== $( \text{DepartmentName} )$ and $( \text{Manager} )$ depend on $( \text{DepartmentID} )$, which in turn depends on $( \text{EmployeeID} )$.
    

---

#### **Solution (Normalization to 3NF):**

To remove transitive dependencies, we split the table into two tables:

54. **Employee Table (EmployeeID, DepartmentID):**

| EmployeeID | DepartmentID |
| ---------- | ------------ |
| 1          | 101          |
| 2          | 102          |
| 3          | 103          |
| 4          | 104          |

55. **Department Table (DepartmentID, DepartmentName, Manager):**

| DepartmentID | DepartmentName | Manager |
| ------------ | -------------- | ------- |
| 101          | HR             | Alice   |
| 102          | IT\|           | Bob     |
| 103          | Finance        | Charlie |

Now, $( \text{DepartmentName} ) and ( \text{Manager} )$ depend only on $( \text{DepartmentID} )$, and there are no transitive dependencies.

---

### **Summary Table of Differences**

---

##### **Step 4: Boyce-Codd Normal Form (BCNF)**  
**Problem**: If `RecordLabel` determines `LabelCountry`, but `RecordLabel` is not a candidate key.  

**Split Tables**:  
56. **RecordLabels**:  
   | RecordLabel (PK)      | LabelCountry |  
   |-----------------------|--------------|  
   | Moonlight Records     | UK           |  
   | Soundwave Productions | USA          |  
   | Global Harmony        | France       |  

57. **Artists (Final)**:  
   | ArtistID | ArtistName       | BandGenre          | RecordLabel (FK)      |  
   |----------|------------------|--------------------|-----------------------|  

---

#### **Final Normalized Tables**  
| **Artists**             | **Stages**               | **Performances**          | **RecordLabels**       |  
|-------------------------|--------------------------|---------------------------|------------------------|  
| ArtistID (PK)           | StageID (PK)             | ArtistID (FK)             | RecordLabel (PK)       |  
| ArtistName              | StageName                | StageID (FK)              | LabelCountry           |  
| BandGenre               | StageCapacity            | PerformanceTime           |                        |  
| RecordLabel (FK)        |                          | TicketPrice               |                        |  

---

##### **Key Improvements**  
58. **Eliminated Redundancy**:  
   - `LabelCountry` stored once per `RecordLabel`, not repeated for each artist.  
59. **Avoided Anomalies**:  
   - Deleting an artist doesn’t delete stage or label data.  
60. **Improved Flexibility**:  
   - Add/update stages or labels independently.  

**Example Query**:  
```sql  
-- Find all artists performing on the "Main Stage":  
SELECT ArtistName, PerformanceTime  
FROM Artists  
JOIN Performances ON Artists.ArtistID = Performances.ArtistID  
JOIN Stages ON Performances.StageID = Stages.StageID  
WHERE StageName = 'Main Stage';  
```  

---


### Primer on Database Locks 🗝️

Database locks are mechanisms used in Database Management Systems (DBMS) to manage access to data and maintain data consistency during concurrent transactions. They ensure that multiple users or processes can work with a database without causing logical errors or inconsistencies.

---

#### Why Do We Need Locks?

- **Preventing Conflicts**: Avoid issues like lost updates, dirty reads, or uncommitted data being accessed.
- **Concurrency Control**: Allow multiple transactions to run simultaneously without violating data integrity.
- **Maintain Isolation**: Ensure transactions execute independently of one another, a key part of the **ACID properties**.

---

#### Types of Locks

##### 1. **Based on Access Type**

- **Shared Lock (S Lock)**:
    - Used for read operations.
    - Multiple transactions can hold a shared lock on the same data.
    - Example: Two users can read the same record simultaneously.
- **Exclusive Lock (X Lock)**:
    - Used for write operations.
    - Only one transaction can hold an exclusive lock on a piece of data.
    - Prevents both read and write access by others.
    - Example: If a transaction is updating a row, no one else can read or write that row.

##### 2. **Based on Scope**

- **Row-Level Lock**:
    
    - Locks a single row in a table.
    - Example: Updating a specific user record in a database.
- **Page-Level Lock**:
    
    - Locks a data page (a block of rows).
    - Example: Useful when accessing multiple rows in the same memory page.
- **Table-Level Lock**:
    
    - Locks the entire table.
    - Example: Adding a column to a table structure or bulk updating rows.
- **Database-Level Lock**:
    
    - Locks the entire database.
    - Example: During backups or maintenance.

---

#### Modes of Locking

##### 1. **Read Locks**:

- Prevent others from writing but allow reading.
- Example: Multiple users reading a product catalog.

##### 2. **Write Locks**:

- Prevent others from reading or writing.
- Example: A transaction updating a bank account balance.

##### 3. **Intent Locks**:

- Used in hierarchical locking.
- Indicates that a transaction intends to acquire locks at a lower level (e.g., row level).
- Types:
    - **Intent Shared (IS)**: Intends to acquire shared locks.
    - **Intent Exclusive (IX)**: Intends to acquire exclusive locks.

---

#### Locking Protocols

##### 1. **Two-Phase Locking (2PL)**:

- **Growing Phase**: Transaction acquires all the locks it needs.
- **Shrinking Phase**: Once it releases a lock, it cannot acquire new ones.
- Ensures serializability (order of transactions is consistent).

##### 2. **Strict Two-Phase Locking**:

- Similar to 2PL, but holds all exclusive locks until the transaction commits or aborts.
- Prevents dirty reads.

##### 3. **Deadlock Prevention**:

- Deadlocks occur when two or more transactions wait indefinitely for resources locked by each other.
- Prevention techniques:
    - **Timeouts**: Automatically abort transactions after a time limit.
    - **Wait-Die / Wound-Wait**: Priority-based schemes to decide which transaction to abort.

---

#### Lock Compatibility Matrix

|Requested Lock|Existing Lock|Allowed?|
|---|---|---|
|Shared (S)|Shared (S)|Yes|
|Shared (S)|Exclusive (X)|No|
|Exclusive (X)|Shared (S)|No|
|Exclusive (X)|Exclusive (X)|No|

---

#### Common Issues with Locks

61. **Deadlocks**:
    
    - Circular wait where two or more transactions are stuck waiting for resources held by each other.
    - Example: Transaction A locks Row 1 and needs Row 2; Transaction B locks Row 2 and needs Row 1.
62. **Starvation**:
    
    - A transaction keeps waiting indefinitely for a resource because higher-priority transactions keep preempting it.
63. **Overhead**:
    
    - Managing locks can slow down performance, especially in high-concurrency environments.

---

#### Real-Life Example

Imagine you're using an online shopping app:

64. **Shared Lock**: While browsing, multiple users can view product details simultaneously.
65. **Exclusive Lock**: When you add an item to your cart, the system locks that product's inventory record to prevent others from purchasing it until your transaction is complete.

---


### Diff. between Table and View 
Here’s a table that highlights the differences between a **Table** and a **View** in a Database:

| Feature                                   | Table                                                | View                                                                               |
| ----------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **Definition**                            | A table is a physical storage of data in a database. | A view is a virtual table that presents data from one or more tables.              |
| **Storage**                               | Stores actual data.                                  | Does not store data; ==only stores the SQL query definition.==                     |
| **Data Retrieval**                        | Data is retrieved directly from the table.           | Data is retrieved dynamically from the underlying tables when accessed.            |
| **Modification (INSERT, UPDATE, DELETE)** | Supports data modification operations.               | ==May or may not allow modification== (depends on whether it’s an updatable view). |
| **Performance**                           | ==Faster as== data is physically stored.             | ==Slower== than tables because it runs a query each time it is accessed.           |
| **Dependencies**                          | Independent; does not rely on other objects.         | Depends on the underlying table(s).                                                |
| **Use Case**                              | Used for storing raw data permanently.               | Used for simplifying complex queries, security, or presenting filtered data.       |

   
### **🛢️ LIKE Operator, `%`, and `_` in SQL**

The **LIKE** operator is used in SQL to **search for patterns** in **text-based columns** (like names, addresses, etc.). It works with two wildcards:

|Wildcard|Meaning|Example|Matches|
|---|---|---|---|
|`%` (percent)|**Any number of characters** (including zero)|`WHERE name LIKE 'J%'`|John, Jack, James, but NOT Alex|
|`_` (underscore)|**Exactly one character**|`WHERE name LIKE 'J_n'`|Jon, Jan, but NOT John|

---

#### **📌 Examples in SQL**

##### **1️⃣ Find Names Starting with "A"**

```sql
SELECT * FROM users WHERE name LIKE 'A%';
```

✅ **Matches**: Alice, Andrew, Alex  
❌ **Does NOT Match**: Brian, John

---

##### **2️⃣ Find Names Ending with "y"**

```sql
SELECT * FROM users WHERE name LIKE '%y';
```

✅ **Matches**: Emily, Henry, Lily  
❌ **Does NOT Match**: Robert, Alice

---

##### **3️⃣ Find Names with "o" in Second Place**

```sql
SELECT * FROM users WHERE name LIKE '_o%';
```

✅ **Matches**: Tom, Bob, Tony  
❌ **Does NOT Match**: Alice, Sam

---

##### **🎯 When to Use?**

- Searching **partial matches** (e.g., phone numbers, email domains).
- Finding words with **specific patterns** (e.g., "_o__" for "John").
- Filtering **large datasets** efficiently.

Would you like a **real-world example** or an **optimization tip**? 😊


### **quick cheat sheet of basic database (DB):**

---

#### **1. Data Definition Language (DDL)** [[#**SQL Command Categories**|see ths]]

##### **Create a Table**

```sql
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    BirthDate DATE
);
```

##### **Alter a Table**

```sql
ALTER TABLE Students ADD Email VARCHAR(100);
```

##### **Drop a Table**

```sql
DROP TABLE Students;
```

---

#### **2. Data Manipulation Language (DML)**

##### **Insert Data**

```sql
INSERT INTO Students (StudentID, FirstName, LastName, BirthDate)
VALUES (1, 'John', 'Doe', '2000-01-15');
```

##### **Update Data**

```sql
UPDATE Students
SET Email = 'john.doe@example.com'
WHERE StudentID = 1;
```

##### **Delete Data**

```sql
DELETE FROM Students
WHERE StudentID = 1;
```

---

#### **3. Basic Queries**

##### **Select All Rows & Columns**

```sql
SELECT * FROM Students;
```

##### **Select Specific Columns**

```sql
SELECT FirstName, LastName FROM Students;
```

##### **Filtering with WHERE**

```sql
SELECT * FROM Students
WHERE LastName = 'Doe';
```

---

#### **4. Sorting and Limiting**

##### **Order Results**

```sql
SELECT * FROM Students
ORDER BY LastName ASC, FirstName DESC;
```

##### **Limit the Number of Results**

```sql
SELECT * FROM Students
ORDER BY BirthDate DESC
LIMIT 5;
```

---

#### **5. Aggregation and Grouping**

##### **Using Aggregate Functions**

```sql
SELECT COUNT(*) AS TotalStudents, AVG(YEAR(BirthDate)) AS AvgBirthYear
FROM Students;
```

##### **Grouping Data**

```sql
SELECT LastName, COUNT(*) AS Count
FROM Students
GROUP BY LastName;
```

##### **Using HAVING for Group Filters**

```sql
SELECT LastName, COUNT(*) AS Count
FROM Students
GROUP BY LastName
HAVING COUNT(*) > 1;
```

| Feature                 | `WHERE`                                | `HAVING`                                 |
| ----------------------- | -------------------------------------- | ---------------------------------------- |
| **Used for**            | Filtering **rows**                     | Filtering **groups** (after `GROUP BY`)  |
| **Works on**            | **Raw data** (before grouping)         | **Aggregated data** (after grouping)     |
| **Can use aggregates?** | ❌ No (can’t use `SUM()`, `AVG()` etc.) | ✅ Yes (can use `COUNT()`, `SUM()`, etc.) |
| **When applied**        | Before grouping                        | After grouping                           |
| **Example use**         | `WHERE age > 18`                       | `HAVING COUNT(*) > 2`                    |

---

#### **6. Joins **  - (Inner,Left,Right)  [[DBMS_JOINS#SQL Joins (Inner, Left, Right and Full Join)|see more..]]

##### **Inner Join**

```sql
SELECT s.FirstName, s.LastName, e.CourseName
FROM Students s
INNER JOIN Enrollments e ON s.StudentID = e.StudentID;
```

##### **Left Join**

```sql
SELECT s.FirstName, s.LastName, e.CourseName
FROM Students s
LEFT JOIN Enrollments e ON s.StudentID = e.StudentID;
```

##### **Right Join**

```sql
SELECT s.FirstName, s.LastName, e.CourseName
FROM Students s
RIGHT JOIN Enrollments e ON s.StudentID = e.StudentID;
```

##### **Full Outer Join** _(syntax may vary by DBMS)_

```sql
SELECT s.FirstName, s.LastName, e.CourseName
FROM Students s
FULL OUTER JOIN Enrollments e ON s.StudentID = e.StudentID;
```

### 🧾 Use Case: Students & Courses

#### Table 1: `students`

|student_id|name|
|---|---|
|1|Alice|
|2|Bob|
|3|Charlie|

#### Table 2: `enrollments`

|student_id|course|
|---|---|
|1|Math|
|2|English|
|4|Science|

---

### ✅ 1. **INNER JOIN** — Only matching records in both tables

```sql
SELECT s.name, e.course
FROM students s
INNER JOIN enrollments e
ON s.student_id = e.student_id;
```

**Returns:**

|name|course|
|---|---|
|Alice|Math|
|Bob|English|

🧠 **Use Case**: When you only care about students **who are enrolled**.

---

### ✅ 2. **LEFT JOIN** — All from the left table + matched from the right

```sql
SELECT s.name, e.course
FROM students s
LEFT JOIN enrollments e
ON s.student_id = e.student_id;
```

**Returns:**

|name|course|
|---|---|
|Alice|Math|
|Bob|English|
|Charlie|NULL|

🧠 **Use Case**: When you want **all students**, even if they are **not enrolled in any course**.

---

### ✅ 3. **RIGHT JOIN** — All from the right table + matched from the left

```sql
SELECT s.name, e.course
FROM students s
RIGHT JOIN enrollments e
ON s.student_id = e.student_id;
```

**Returns:**

|name|course|
|---|---|
|Alice|Math|
|Bob|English|
|NULL|Science|

🧠 **Use Case**: When you want **all course enrollments**, even if the **student info is missing**.

---

### 🧠 Summary Table:

|Join Type|Returns|
|---|---|
|`INNER JOIN`|Only matching rows in both tables|
|`LEFT JOIN`|All rows from **left**, with matches from right or NULL|
|`RIGHT JOIN`|All rows from **right**, with matches from left or NULL|

---

Let me know if you'd like this as an Anki MCQ or table-flip flashcard!


---

#### **7. Subqueries**

##### **Subquery in WHERE Clause**

```sql
SELECT FirstName, LastName
FROM Students
WHERE StudentID IN (
    SELECT StudentID FROM Enrollments WHERE CourseID = 101
);
```

##### **Correlated Subquery**

```sql
SELECT s.FirstName, s.LastName
FROM Students s
WHERE BirthDate = (
    SELECT MIN(BirthDate) FROM Students WHERE LastName = s.LastName
);
```

---

#### **8. Set Operations**

##### **UNION (Combining Results)**

```sql
SELECT FirstName FROM Students
UNION
SELECT FirstName FROM Instructors;
```

---

#### **9. Advanced (Optional)**

##### **Window Functions**

```sql
SELECT FirstName, LastName,
       ROW_NUMBER() OVER (ORDER BY BirthDate) AS RowNum
FROM Students;
```

---






### **Relational Algebra:**
 
#### **1. Selection (σ)**

- **Symbol**: `σ`
    
- **Purpose**: Filters rows (tuples) from a relation based on a condition.
    
- **Syntax**: `σ_condition(Relation)`
    
- **Example**:  
    Suppose we have a `Students` table:

|ID|Name|Age|Major|
|---|---|---|---|
|101|Alice|22|CS|
|102|Bob|24|Math|
|103|Carol|22|Physics|
    
    If we want to select students who are 22 years old:
    
    ```
    σ_Age=22(Students)
    ```
    
    **Result:**
    
    |ID|Name|Age|Major|
    |---|---|---|---|
    |101|Alice|22|CS|
    |103|Carol|22|Physics|
    
- **Key Points**:
    
    - Selection **only filters rows**; it does **not** modify columns.
    - It uses conditions like `=`, `<`, `>`, `<=`, `>=`, `≠`, `AND (∧)`, `OR (∨)`, and `NOT (¬)`.

---

#### **2. Projection (π)**

- **Symbol**: `π`
- **Purpose**: Selects specific columns (attributes) from a relation.
- **Syntax**: `π_column1, column2,...(Relation)`

- **Example**:  
    If we only want the `Name` and `Major` from the `Students` table:

    ```
    π_Name, Major(Students)
    ```

|Name|Major|
|---|---|
|Alice|CS|
|Bob|Math|
|Carol|Physics|
 
- **Key Points**:
    
    - Projection **only filters columns**; it does **not** modify rows.
    - Duplicate rows may be removed since relational algebra operates on sets.

---

#### **Combining Selection and Projection**

We can **combine** both operations to refine the results.  
Example: Get only the `Name` of students who are 22 years old:

```
π_Name(σ_Age=22(Students))
```

**Result:**

| Name  |
| ----- |
| Alice |
| Carol |

---
#### **Union (∪) and Cross Product (×) in Relational Algebra**

In relational algebra, **Union (∪) and Cross Product (×)** are two fundamental operations used to manipulate tables (relations). Let's break them down with examples.

---

#### **1. Union (∪)**

- **Symbol**: `∪`
- **Purpose**: Combines two relations (tables) and returns all unique rows.
- **Condition**: Both relations must have:
    - The same number of columns.
    - The same column names and data types.

#### **Example**

Consider two tables, `Students_CS` and `Students_Math`:

**Students_CS:**

|ID|Name|
|---|---|
|101|Alice|
|102|Bob|

**Students_Math:**

|ID|Name|
|---|---|
|103|Carol|
|102|Bob|

#### **Union operation:**

```
Students_CS ∪ Students_Math
```

**Result:**

|ID|Name|
|---|---|
|101|Alice|
|102|Bob|
|103|Carol|

**Key Points:**

- **Duplicates are removed**, since relational algebra deals with sets.
- Both tables **must be union-compatible** (same schema).

---

#### **2. Cross Product (×)**

- **Symbol**: `×`
- **Purpose**: Combines every row of the first table with every row of the second table (also called Cartesian Product).
- **Result**: If `Relation1` has `m` rows and `Relation2` has `n` rows, the result will have `m × n` rows.

#### **Example**

Consider `Students` and `Courses` tables:

**Students:**

|ID|Name|
|---|---|
|101|Alice|
|102|Bob|

**Courses:**

|CourseID|CourseName|
|---|---|
|C1|Database|
|C2|Algebra|

##### **Cross Product operation:**

```
Students × Courses
```

**Result:**

|ID|Name|CourseID|CourseName|
|---|---|---|---|
|101|Alice|C1|Database|
|101|Alice|C2|Algebra|
|102|Bob|C1|Database|
|102|Bob|C2|Algebra|

**Key Points:**

- The result combines **every row from the first table** with **every row from the second table**.
- The number of rows grows **multiplicatively** (`m × n`).
- It is usually followed by **Selection (σ)** to filter relevant results.

---

#### **When to Use Union vs. Cross Product**

|Operation|Purpose|
|---|---|
|**Union (∪)**|Combines similar rows from two tables (removes duplicates).|
|**Cross Product (×)**|Forms all possible row combinations between two tables.|

 #### An Example:
 To solve these queries using **relational algebra**, let's analyze the given database schema and how we can retrieve the required information.

---

##### **1. List the customers with a yearly bill of more than Taka 5,000**

###### **Understanding the Calculation**

The **yearly bill** for a customer is calculated as:

$\text{Yearly Bill}$ = $\sum_{\text{months}}$ ( $\text{monthly demand}$ $\times$ $\text{unit price}$)

We need to:

1. **Join** `Customer_usage_profile` with `Powerplant` to get the `unit price` for each powerplant.
2. **Join** with `Customer` to get the `monthly_demand` for each customer.
3. **Compute the total yearly bill** (sum of `monthly_demand × unit price` for 12 months).
4. **Filter** customers whose yearly bill is more than **Taka 5,000**.

###### **Relational Algebra Solution**

```
Bill = π_Customer_ID, SUM(monthly_demand * unit_price) (Customer ⨝ Customer_usage_profile ⨝ Powerplant)
FilteredCustomers = σ_Bill > 5000 (Bill)
Result = π_Customer_ID, name (FilteredCustomers ⨝ Customer)
```

---

##### **2. List the customers who use nuclear power during December**

###### **Understanding the Condition**

- We need to **filter** customers who:
    - Use **nuclear power** (`type = 'nuclear power'`)
    - During **December** (`month_name = 'December'`)

###### **Relational Algebra Solution**

```
NuclearCustomers = σ_type='nuclear power' (Powerplant) ⨝ Customer_usage_profile
DecemberNuclearCustomers = σ_month_name='December' (NuclearCustomers)
Result = π_Customer_ID, name (DecemberNuclearCustomers ⨝ Customer)
```

---

###### **Summary of the Approach**

- **Query 1 (Yearly Bill > 5000)** → Join tables, compute bill, filter results.
- **Query 2 (Uses nuclear power in December)** → Filter by power type and month, then join with customer data.
