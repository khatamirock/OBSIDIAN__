
# 💀Traps  & Most-Asked Questions

---
## 🔹 1️⃣ SELECT + WHERE confusion traps

### ❌ Trap

```sql
SELECT * FROM students WHERE marks = NULL;
```

### ✅ Correct

```sql
SELECT * FROM students WHERE marks IS NULL;
```

> 👉 `= NULL` never works — must use `IS NULL` or `IS NOT NULL`.

---

## 🔹 2️⃣ DISTINCT vs GROUP BY trap

```sql
SELECT DISTINCT city FROM students;
-- same as
SELECT city FROM students GROUP BY city;
```

> ⚠️ Teachers often mix these and ask:  
> “Which one removes duplicates?”  
> ✅ Both do, but `GROUP BY` can also **aggregate**.

---

## ❗See This nested select....
[Using nested SELECT - SQLZoo](https://sqlzoo.net/wiki/Using_nested_SELECT)


---

## 🔹 3️⃣ COUNT() trap questions

### Common trick

```sql
SELECT COUNT(address) FROM students;
```

> ❗ This **ignores NULLs**.  
> If `address` has NULL values → they **don’t count**.

✅ To count all rows:

```sql
SELECT COUNT(*) FROM students;
```

---

## 🔹 4️⃣ BETWEEN, IN, and LIKE traps

|Keyword|Meaning|Trick|
|---|---|---|
|`BETWEEN 10 AND 20`|Inclusive (`10 ≤ x ≤ 20`)|Some think it excludes 20|
|`LIKE '%a%'`|Contains ‘a’ anywhere|`%` = any chars, `_` = one char|
|`IN (1, 2, 3)`|Matches any listed value|Fails if `NULL` involved|

---

## 🔹 5️⃣ INNER JOIN vs LEFT JOIN trap

### Question:

> Show all students, even if they have no matching course.

✅ Correct:

```sql
SELECT s.name, c.course_name
FROM students s
LEFT JOIN courses c ON s.course_id = c.id;
```

> ❌ If you use `INNER JOIN`, students with no course will disappear.

---

## 🔹 6️⃣ Aggregate functions + GROUP BY

### Trap question:

> Find total marks of each student.

❌ Wrong (missing GROUP BY):

```sql
SELECT name, SUM(marks) FROM students;
```

✅ Correct:

```sql
SELECT name, SUM(marks) FROM students GROUP BY name;
```

> 👉 Rule: Any column not inside an aggregate function must appear in GROUP BY.

---

## 🔹 7️⃣ HAVING vs WHERE trap

|Clause|Works On|Example|
|---|---|---|
|`WHERE`|Filters **before** grouping|`WHERE marks > 50`|
|`HAVING`|Filters **after** grouping|`HAVING AVG(marks) > 50`|

Example:

```sql
SELECT dept, AVG(salary)
FROM employees
GROUP BY dept
HAVING AVG(salary) > 50000;
```

> ❌ `WHERE AVG(salary)` would cause an error.

---

## 🔹 8️⃣ ORDER of execution trap

Teachers love this:

> “What runs first: SELECT, WHERE, GROUP BY, HAVING, ORDER BY?”

✅ Correct order:

```
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

---

## 🔹 9️⃣ Subquery traps

> “Find students who got more marks than the average.”

✅ Correct:

```sql
SELECT name
FROM students
WHERE marks > (SELECT AVG(marks) FROM students);
```

> ❌ If you use `HAVING` or forget parentheses, wrong results.

---

## 🔹 🔟 UPDATE and DELETE traps

**Trap:** Forgetting WHERE clause 😱

```sql
DELETE FROM students; -- deletes all rows!
```

✅ Always:

```sql
DELETE FROM students WHERE id = 5;
```

---

## 🔹 11️⃣ Aliases trap

```sql
SELECT name AS student_name FROM students;
```

> ❌ You can’t use `student_name` in the **WHERE** clause.  
> It only exists **after SELECT** executes.

---

## 🔹 13️⃣ Self Join trap

> “Find pairs of employees who share the same manager.”

✅

```sql
SELECT e1.name AS emp1, e2.name AS emp2
FROM employees e1
JOIN employees e2
ON e1.manager_id = e2.manager_id
AND e1.id <> e2.id;
```

> 💡 Many students forget the `<>` part → duplicate/self pairs appear.

---

## 🔹 14️⃣ String / Date function traps

```sql
SELECT SUBSTRING(name, 1, 3) FROM students;  -- first 3 letters
SELECT YEAR(dob) FROM students;              -- extract year
SELECT DATE_FORMAT(dob, '%d-%M-%Y');         -- nice format
```

> Teachers might ask:  
> “Which returns part of a string?” or  
> “How to extract month name?”

---

## 🔹 15️⃣ Nested Aggregation trap

> Find the **maximum** of average salary per department.

✅

```sql
SELECT MAX(avg_salary)
FROM (
  SELECT AVG(salary) AS avg_salary
  FROM employees
  GROUP BY department
) AS temp;
```

> ❌ Forgetting alias `AS temp` → syntax error.

---

# 💣 BONUS — Rapid-Fire “Teacher Trap” Questions

|Question|Common Mistake|Correct Concept|
|---|---|---|
|Can `HAVING` be used without `GROUP BY`?|Students say “No”|It **can**, but rarely useful|
|Difference between `DELETE`, `TRUNCATE`, `DROP`|Think they’re same|`DELETE` = rows, `TRUNCATE` = fast remove all, `DROP` = remove table|
|Which comes first: HAVING or WHERE?|Wrong order|`WHERE` first, `HAVING` after aggregation|
|How many NULLs does COUNT(*) include?|Think 0|`COUNT(*)` includes NULLs (counts rows), others skip NULLs|
|Primary vs Unique key|Think both same|Primary → 1 per table, Unique → many allowed|

---

> **Q:** Find all departments where the **total salary** > **average of all department totals**.

| emp_id | name  | dept  | salary | bonus |
| ------ | ----- | ----- | ------ | ----- |
| 1      | Alice | HR    | 20000  | 1000  |
| 2      | Bob   | HR    | 30000  | 1500  |
| 3      | Carol | IT    | 40000  | 2000  |
| 4      | David | IT    | 60000  | 3000  |
| 5      | Emma  | Sales | 25000  | 1200  |
| 6      | Frank | Sales | 25000  | 1000  |
## 💥 What’s really happening here?

Let’s rewrite your query piece by piece:

```sql
SELECT dept, total_salary
FROM (
  SELECT dept, SUM(salary) AS total_salary
  FROM employees
  GROUP BY dept
) AS x
WHERE total_salary > (
  SELECT AVG(total_salary)
  FROM (
    SELECT SUM(salary) AS total_salary
    FROM employees
    GROUP BY dept
  ) AS y
);
```

---

## 🧱 Step 1 — Inner-most layer (the one inside the `WHERE`)

```sql
SELECT SUM(salary) AS total_salary
FROM employees
GROUP BY dept;
```

This gives:

|dept|total_salary|
|---|---|
|HR|50000|
|IT|100000|
|Sales|50000|

So this is just a table of total salaries per department.

---

## 🧱 Step 2 — Middle part (inside the `WHERE total_salary > (...)`)

```sql
SELECT AVG(total_salary)
FROM (
  SELECT SUM(salary) AS total_salary
  FROM employees
  GROUP BY dept
) AS y;
```

That says:

> “Take the average of all those totals.”

So:

```
(50000 + 100000 + 50000) / 3 = 66666.67
```

✅ **AVG(total_salary) = 66666.67**

---

## 🧱 Step 3 — Outer layer (our main query)

```sql
SELECT dept, total_salary
FROM (
  SELECT dept, SUM(salary) AS total_salary
  FROM employees
  GROUP BY dept
) AS x
WHERE total_salary > 66666.67;
```

Now the inner query (`x`) gives this:

|dept|total_salary|
|---|---|
|HR|50000|
|IT|100000|
|Sales|50000|

So only departments whose total > 66666.67 survive.

✅ **Result → only IT.**

---

## 🧠 What’s the mental model?

Let’s translate to English:

> “First, find how much salary each department pays in total.  
> Then, find the _average_ of those total salaries.  
> Finally, show me only the departments whose total is _above that average_.”

---

## 🧩 Why it looks “WTF-level nested”

Because we have **three layers** of logic:  
1️⃣ Compute totals per department  
2️⃣ Compute average of those totals  
3️⃣ Compare totals again to that average

SQL forces you to literally _nest each step_ since each depends on the previous one’s result.

---

## 🧠 Summary Shortcut

| Step | What it does                      | Keyword            |
| ---- | --------------------------------- | ------------------ |
| 1    | Aggregate within each group       | `GROUP BY`         |
| 2    | Aggregate across those aggregates | Subquery + `AVG()` |
| 3    | Compare results                   | `WHERE`            |


---

# 💡 Common & Tricky ==Self-Join== Question Patterns

---

## 🧩 1️⃣ Employee–Manager Relationship

**(Most common exam question!)**

> “Display the employee’s name and their manager’s name.”

**Table:**

| id  | name   | manager_id |
| --- | ------ | ---------- |
| 1   | Alice  | 3          |
| 2   | Bob    | 3          |
| 3   | Carol  | NULL       |
| 4   | Sam    | 2          |
| 5   | Patrok | 3          |

**Query:**

```sql
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

✅ Output:

| employee | manager |
| -------- | ------- |
| Alice    | Carol   |
| Bob      | Carol   |
| Carol    | NULL    |
| Sam      | Bob     |
| Patrok   | Carol   |

📘 **Why it’s a trap:**  
Students forget `LEFT JOIN`, so top-level managers with ==`NULL`== manager_id disappear.

---

## 🧩 2️⃣ Employees Having the Same Manager

> “Find pairs of employees who share the same manager.”

**Query:**

```sql
SELECT e1.name AS emp1, e2.name AS emp2
FROM employees e1
JOIN employees e2
ON e1.manager_id = e2.manager_id
AND e1.id <> e2.id;
```

✅ Teaches: use of `<>` (not equal) and understanding of self-join symmetry.

---


## 🧩 4️⃣ Compare Salaries in Same Department

> “List employees who earn more than their manager.”

|id|name|salary|manager_id|
|---|---|---|---|
|1|Alice|6000|3|
|2|Bob|5500|3|
|3|Carol|5000|NULL|

**Query:**

```sql
SELECT e.name AS emp, e.salary, m.name AS manager, m.salary
FROM employees e
JOIN employees m ON e.manager_id = m.id
WHERE e.salary > m.salary;
```

✅ Tests: correct self-join condition + column aliasing.

---

## 🧩 5️⃣ Find Duplicate Data Without Using GROUP BY

> “Find employees with the same salary.”

**Query:**

```sql
SELECT e1.name, e2.name, e1.salary
FROM employees e1
JOIN employees e2
ON e1.salary = e2.salary
AND e1.id <> e2.id;
```

✅ Shows same values in multiple rows — classic interview trap.

---

## 🧩 6️⃣ Find Previous / Next Record (Sequence Relation)

> “Find each employee and the next employee by ID.”

**Query:**

```sql
SELECT e1.id AS current_id, e1.name AS current_emp, e2.name AS next_emp
FROM employees e1
LEFT JOIN employees e2
ON e1.id + 1 = e2.id;
```

✅ Tricky: Self-join used to simulate “row shift”.

---

## 🧩 7️⃣ Find Students in the Same City

> “List pairs of students living in the same city.”

**Query:**

```sql
SELECT s1.name AS student1, s2.name AS student2, s1.city
FROM students s1
JOIN students s2
ON s1.city = s2.city
AND s1.id < s2.id;
```

✅ Note the use of `<` instead of `<>` to **avoid duplicate pair reversals**  
(e.g., Alice–Bob and Bob–Alice both appearing).

---

## 🧩 8️⃣ Find Customers Who Referred Others

> “Find all customers who have referred at least one other customer.”

**Table:**

|id|name|referred_by|
|---|---|---|
|1|Alice|NULL|
|2|Bob|1|
|3|Carol|2|
|4|David|1|

**Query:**

```sql
SELECT DISTINCT r.name AS referrer
FROM customers c
JOIN customers r ON c.referred_by = r.id;
```

✅ Self-join maps “referred_by” relationship.

---

## 🧩 9️⃣ Find Chain of Command (Boss → Subordinate)

> “Show all boss–subordinate pairs, even if multiple levels apart.”

💥 Slightly advanced — needs recursive CTE (but conceptually self-join repeated):

```sql
WITH RECURSIVE hierarchy AS (
  SELECT id, name, manager_id FROM employees
  UNION ALL
  SELECT e.id, e.name, h.manager_id
  FROM employees e
  JOIN hierarchy h ON e.manager_id = h.id
)
SELECT * FROM hierarchy;
```

✅ Tests understanding of recursive join logic.

---

## 🧩 🔟 Symmetric Relationship Example

> “Find pairs of friends (friendship table where each row means one direction).”

**Table:**

|id|person|friend|
|---|---|---|
|1|Alice|Bob|
|2|Bob|Alice|
|3|Alice|Carol|

**Query:**

```sql
SELECT f1.person, f1.friend
FROM friends f1
JOIN friends f2
ON f1.person = f2.friend
AND f1.friend = f2.person;
```

✅ Finds **mutual friendships** (both directions exist).  
📘 Teachers love this one because it looks simple but forces you to think about symmetry.

---

# 🧠 Summary Table

|Goal|Self-Join Condition|Trick|
|---|---|---|
|Employee → Manager|`e.manager_id = m.id`|Use LEFT JOIN to keep top managers|
|Same Manager|`e1.manager_id = e2.manager_id`|Add `e1.id <> e2.id`|
|Higher Salary|`e.manager_id = m.id AND e.salary > m.salary`|Use aliases|
|Same City|`s1.city = s2.city AND s1.id < s2.id`|Avoid duplicate pairs|
|Mutual Friends|`f1.person = f2.friend AND f1.friend = f2.person`|Symmetric relation|
|Find Duplicates|`t1.value = t2.value AND t1.id <> t2.id`|Compare same column|

---


Perfect — let’s go over **Nested Aggregation Queries** step-by-step with **examples teachers often ask** (especially in SQL exams or viva).

---

## 🔹 What is a Nested Aggregation?

A **nested aggregation** means using **an aggregate function inside another aggregate function** — often with a **subquery**.

👉 Example of aggregates: `MAX()`, `MIN()`, `AVG()`, `SUM()`, `COUNT()`

Example:

```sql
SELECT MAX(AVG(salary)) FROM employees GROUP BY department;
```

Here,

- The **inner aggregation** is `AVG(salary)` (average per department)
    
- The **outer aggregation** is `MAX(...)` — finding the **maximum average**.
    

---

## 🧮 Example 1: Highest Average Salary Among Departments

**Question:** Find the **maximum average salary** among all departments.

```sql
SELECT MAX(avg_salary)
FROM (
  SELECT AVG(salary) AS avg_salary
  FROM employees
  GROUP BY department
) AS dept_avg;
```

### ✅ Explanation:

1. Inner query calculates the average salary for each department.
    
2. Outer query finds the **maximum** of those averages.  
    So, you get the **department with the highest average salary**.
    

---

## 🧮 Example 2: Department Having Minimum Total Salary

**Question:** Find the **minimum total salary** among departments.

```sql
SELECT MIN(total_salary)
FROM (
  SELECT SUM(salary) AS total_salary
  FROM employees
  GROUP BY department
) AS dept_sum;
```

### ✅ Explanation:

- Inner query → total salary of each department
    
- Outer query → smallest of these totals
    

---

## 🧮 Example 3: Difference Between Highest and Lowest Average Salary

**Question:** Find the **difference between the highest and lowest department average salary**.

```sql
SELECT MAX(avg_salary) - MIN(avg_salary) AS salary_gap
FROM (
  SELECT AVG(salary) AS avg_salary
  FROM employees
  GROUP BY department
) AS dept_avg;
```

### ✅ Explanation:

- Inner query gives average salary per department.
    
- Outer query subtracts the smallest from the largest.
    

---

## 🧮 Example 4: Employees Earning Above Overall Average

**Question:** Find employees who earn **more than the average salary** of their department average.

```sql
SELECT name, salary
FROM employees
WHERE salary > (
  SELECT AVG(avg_salary)
  FROM (
    SELECT AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
  ) AS dept_avg
);
```

### ✅ Explanation:

- Inner-most: department-wise averages
- Middle: overall average of department averages
- Outer: select employees whose salary > that value

---

## 🧮 Example 5: Company-wide Comparison (Tricky Viva Question)

**Question:** Find the department whose **average salary is above the company’s overall average**.

```sql
SELECT department, AVG(salary) AS dept_avg
FROM employees
GROUP BY department
HAVING AVG(salary) > (
  SELECT AVG(salary) FROM employees
);
```

### ✅ Explanation:

This one is **semi-nested**, but still considered **nested aggregation**, because one aggregate (AVG) is compared with another from a subquery.

---

## 🧠 Teacher-Favorite Questions:

|Type|Common Question|Concept|
|---|---|---|
|1|Find department with highest average salary|MAX(AVG(...))|
|2|Find difference between max and min average|MAX(AVG(...)) - MIN(AVG(...))|
|3|Find lowest total salary among departments|MIN(SUM(...))|
|4|Find employees whose salary > average of department averages|AVG(AVG(...))|
|5|Find departments whose avg salary > company avg|HAVING AVG(...) > (SELECT AVG(...))|

---

Would you like me to show these **with example tables and actual numeric results (step-by-step output)** like how teachers do in exams? That’ll help you understand and remember easily.