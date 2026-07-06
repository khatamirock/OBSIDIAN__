
# SQL Joins (Inner, Left, Right and Full Join)

![[sqlJoins_7.png]]



---
- GEEKFORGEEKS
## ***1. SQL INNER JOIN***

The [****INNER JOIN****](https://www.geeksforgeeks.org/sql-inner-join)  keyword selects all rows from both the tables as long as the condition is satisfied. This keyword will create the ****result-set**** by combining all rows from both the tables where the **condition satisfies*** i.e value of the common field will be the same. 

****Syntax****

> SELECT table1.column1,table1.column2,table2.column1,.... FROM table1 INNER JOIN table2 ON table1.matching_column = table2.matching_column;

****Note****: We can also write JOIN instead of INNER JOIN. JOIN is same as INNER JOIN. 

![SQL-Join](https://media.geeksforgeeks.org/wp-content/uploads/20250416165609840811/SQL-Join.png)

### Example of INNER JOIN

Consider the two tables, ****Student**** and ****StudentCourse****, which share a common column **`**ROLL_NO**`**. Using SQL JOINS, we can combine data from these tables based on their ****relationship****, allowing us to retrieve meaningful information like student details along with their ****enrolled courses****. 

### ****Student Table****

### ![student table](https://media.geeksforgeeks.org/wp-content/cdn-uploads/table1-3.png)****StudentCourse**** Table

![course table](https://media.geeksforgeeks.org/wp-content/uploads/table5.png)

Let's look at the example of ****INNER JOIN**** clause, and understand it's working. This query will show the names and age of students enrolled in different courses.  

****Query:****

SELECT StudentCourse.COURSE_ID, Student.NAME, Student.AGE FROM Student  
INNER JOIN StudentCourse  
ON Student.ROLL_NO = StudentCourse.ROLL_NO;

****Output****

![sql inner join example output](https://media.geeksforgeeks.org/wp-content/uploads/table22.png)

## ****2. SQL LEFT JOIN****

A ****LEFT JOIN**** returns ==all rows from the left table, along with matching rows== from the right table. If there is no match, NULL values are returned for columns from the right table. LEFT JOIN is also known as **LEFT OUTER JOIN****.

****Syntax****

> SELECT table1.column1,table1.column2,table2.column1,....  
> FROM table1  
> LEFT JOIN table2  
> ON table1.matching_column = table2.matching_column;

****Note****: We can also use LEFT OUTER JOIN instead of LEFT JOIN, both are the same.

![Left_Join](https://media.geeksforgeeks.org/wp-content/uploads/20240605161731/Left_Join.png)

### ****LEFT JOIN Example****

In this example, the ****LEFT JOIN**** retrieves all rows from the ****Student**** table and the matching rows from the ****StudentCourse**** table based on the **`**ROLL_NO**`** column.

****Query:****

SELECT Student.NAME,StudentCourse.COURSE_ID   
FROM Student  
LEFT JOIN StudentCourse   
ON StudentCourse.ROLL_NO = Student.ROLL_NO;

****Output****

![sql left join example output](https://media.geeksforgeeks.org/wp-content/uploads/table31.png)

## ****3. SQL RIGHT JOIN****

[****RIGHT JOIN****](https://www.geeksforgeeks.org/sql-right-join) returns all the rows of the table on the ****right side of the join**** and matching rows for the table on the left side of the join. It is very similar to ****LEFT JOIN f****or the rows for which there is no matching row on the left side, the result-set will contain ****null****. ****RIGHT JOIN**** is also known as ****RIGHT OUTER JOIN****. 

****Syntax****

SELECT table1.column1,table1.column2,table2.column1,....  
FROM table1   
RIGHT JOIN table2  
ON table1.matching_column = table2.matching_column;

****Key Terms****

- ****table1****: First table.  
    
- ****table2****: Second table  
    
- ****matching_column****: Column common to both the tables.

****Note****: We can also use ****RIGHT OUTER JOIN**** instead of RIGHT JOIN, both are the same. 

![sql right join visual representation](https://media.geeksforgeeks.org/wp-content/uploads/20220515095048/join.jpg)

### ****RIGHT JOIN Example****

In this example, the ****RIGHT JOIN**** retrieves all rows from the ****StudentCourse**** table and the matching rows from the ****Student**** table based on the `ROLL_NO` column.

****Query:****

SELECT Student.NAME,StudentCourse.COURSE_ID   
FROM Student  
RIGHT JOIN StudentCourse   
ON StudentCourse.ROLL_NO = Student.ROLL_NO;

****Output****

![right join example output](https://media.geeksforgeeks.org/wp-content/uploads/table6.png)

## ****4. SQL FULL JOIN****

[****FULL JOIN****](https://www.geeksforgeeks.org/sql-full-join) creates the result-set by combining results of both ****LEFT JOIN**** and ****RIGHT JOIN****. The result-set will contain all the rows from both tables. For the rows for which there is no matching, the result-set will contain NULL values.

![Full_Join](https://media.geeksforgeeks.org/wp-content/uploads/20240605161926/Full_Join.png)



### ****FULL JOIN Example****

This example demonstrates the use of a ****FULL JOIN****, which combines the results of both ****LEFT JOIN**** and ****RIGHT JOIN****. The query retrieves all rows from the ****Student**** and ****StudentCourse**** tables. If a record in one table does not have a matching record in the other table, the result set will include that record with **`**NULL**`** ****values**** for the missing fields

****Query:****

SELECT Student.NAME,StudentCourse.COURSE_ID   
FROM Student  
FULL JOIN StudentCourse   
ON StudentCourse.ROLL_NO = Student.ROLL_NO;

****Output**** 

|NAME|COURSE_ID|
|---|---|
|HARSH|1|
|PRATIK|2|
|RIYANKA|2|
|DEEP|3|
|SAPTARHI|1|
|DHANRAJ|NULL|
|ROHIT|NULL|
|NIRAJ|NULL|
|NULL|4|
|NULL|5|
|NULL|4|

## 5. SQL Natural Join (?)

[Natural join](https://www.geeksforgeeks.org/sql-natural-join/) can join tables based on the ****common columns**** in the tables being joined. A natural join returns all rows by matching values in common columns having same name and ****data type**** of columns and that column should be present in both tables.

- Both table must have at least one common column with same column name and same data type.  
    
- The two table are joined using ****Cross join****.  
    
- DBMS will look for a common column with same name and data type. Tuples having exactly same values in common columns are kept in result.

### Natural join Example

Look at the two tables below- ****Employee**** and ****Department****

| Employee |          |         |
| -------- | -------- | ------- |
| Emp_id   | Emp_name | Dept_id |
| 1        | Jam      | 10      |
| 2        | Jon      | 30      |
| 3        | Bob      | 50      |
| 4        | Chuch    | 30      |
| 5        | Mosh     | 10      |

| Department |           |
| ---------- | --------- |
| Dept_id    | Dept_name |
| 10         | IT        |
| 30         | HR        |
| 40         | TIS       |


****Problem****: Find all Employees and their respective departments.

****Solution Query****: (Employee) ? (Department)

| Emp_id        | Emp_name | Dept_id | Dept_id         | Dept_name |
| ------------- | -------- | ------- | --------------- | --------- |
| 1             | Jam      | 10      | 10              | IT        |
| 2             | Jon      | 30      | 30              | HR        |
| Employee data |          |         | Department data |           |

## Conclusion

****SQL joins**** are essential tools for anyone working with [relational databases](https://www.geeksforgeeks.org/relational-model-in-dbms/). Understanding the different types of joins in ****SQL****, like ****INNER JOIN****, ****LEFT OUTER JOIN****, ****RIGHT JOIN****, and ****FULL JOIN****, allows us to combine and query data effectively. With the ****examples**** and ****syntax**** covered here, we should feel confident applying these ****SQL join types**** to our data to retrieve ****meaningful observations**** and manage ****complex queries**** with ease. Use these SQL join techniques to streamline our ****data handling**** and enhance our ****SQL skills****.

---



