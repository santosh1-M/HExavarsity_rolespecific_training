create database sample_database

create table Student(
      Id int primary key Identity(1,1),
      name varchar(50),
      age int,
      gender varchar(20)
      );

INSERT INTO Student (name, age, gender) VALUES 
('Rohit Sharma', 20, 'Male'),
('Anjali', 21, 'Female'),
('Karthik R', 22, 'Male'),
('Shreyas Iyer', 20, 'Female'),
('Mohammed asif', 23, 'Male'),
('Rishab Pant', 19, 'Male'),
('Pranav', 22, 'Male'),
('Pooja', 21, 'Female');

select * from Student;

-- types of creating view
-- 1.Simple View
-- 2. Complex view

--Simple view

Go
CREATE VIEW vwSamplesimpleview 
AS 
SELECT * 
FROM Student 
WHERE age > 20;

select * from vwSamplesimpleview

INSERT INTO vwSamplesimpleview (name, age, gender) 
VALUES ('Nikita Rao', 22, 'Female');

UPDATE vwSamplesimpleview
SET age = 35
WHERE Id = 3;

DELETE FROM vwSamplesimpleview
WHERE Id = 5;

CREATE TABLE Marks (
    mark_id INT PRIMARY KEY IDENTITY(1,1),
    student_id INT FOREIGN KEY REFERENCES Student(Id),
    subject VARCHAR(30),
    score INT
);

INSERT INTO Marks (student_id, subject, score) VALUES
(1, 'Math', 85),
(1, 'Science', 90),
(2, 'Math', 78),
(2, 'Science', 88),
(3, 'Math', 95);

CREATE VIEW vwStudentAvgMarks AS
SELECT s.Id AS student_id,s.name,s.gender,AVG(m.score) AS average_score
FROM Student s
JOIN Marks m ON s.Id = m.student_id GROUP BY s.Id, s.name, s.gender;

SELECT * FROM vwStudentAvgMarks;

-- creating with check option

CREATE VIEW vwStudentAbove20 AS
SELECT * FROM Student
WHERE age > 20
WITH CHECK OPTION;

select * from vwStudentAbove20;

sp_helptext 'vwStudentAbove20';

insert into vwStudentAbove20 values('kamali',21,'Female')

-- Encryption

CREATE VIEW vwStudentEncrypt
WITH ENCRYPTION
AS
SELECT name, age FROM Student;

select * from vwStudentEncrypt;

-- HELP

sp_helptext 'vwStudentEncrypt';

-- Nested View

CREATE VIEW vwStudentBasic
AS
SELECT Id, Name, Age FROM Student;

CREATE VIEW vwStudentNested
AS
SELECT Name, Age
FROM vwStudentBasic
WHERE Age > 20;

SELECT * FROM vwStudentNested; 

-- Non Aggregated function using subquery

CREATE TABLE employees (
    emp_id INT ,
    name VARCHAR(50),
    department VARCHAR(30),
    salary INT,
    joining_date DATE
);
drop table employees;
INSERT INTO employees (emp_id, name, department, salary, joining_date) VALUES
(101, 'Alice', 'HR', 50000, '2020-01-15'),
(102, 'Bob', 'IT', 70000, '2019-03-10'),
(103, 'Charlie', 'IT', 75000, '2021-07-12'),
(104, 'David', 'Sales', 60000, '2018-10-01'),
(105, 'Eve', 'HR', 52000, '2022-02-25'),
(106, 'Frank', 'Sales', 62000, '2020-08-30'),
(107, 'Grace', 'IT', 68000, '2023-01-11');

select * from employees e 
join 
(select department,max(salary) as maxsalary,min(salary) as min_salary,avg(salary) as avg_salary from employees group by department) k
on k.department=e.department;

-- creating using over methhod

select emp_id,name,department,salary,joining_date,max(salary) over (partition by department) as max_salary,
min(salary) over (partition by department) as min_salary,avg(salary) over (partition by department) as avg_salary  
from employees;

-- CTE

with deptsalary as (
    select department, sum(salary) as total_salary
    from employees
    group by department
)

select e.emp_id, e.name, e.department, e.salary, d.total_salary
from employees e
join deptsalary d on e.department = d.department;

-- row number 

SELECT emp_id, name,salary,department,
       ROW_NUMBER() OVER (partition by department ORDER BY salary DESC) AS row_num
FROM employees;

SELECT emp_id, name,salary,department,
       ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
FROM employees;

insert into employees values(102,'Bob','IT',70000,'2019-03-10');
select * from employees;

with dltedupl as (
SELECT *,
       ROW_NUMBER() OVER (partition by emp_id ORDER BY emp_id ) AS row_num
FROM employees
) 
delete  from dltedupl where row_num>1
select * from dltedupl


-- rank

SELECT *,
       RANK() OVER (PARTITION BY DEPARTMENT ORDER BY salary DESC) AS rank_number
FROM employees;

SELECT *,
       RANK() OVER ( ORDER BY salary DESC) AS rank_number
FROM employees;

-- dense rank

SELECT *,
       DENSE_RANK() OVER (PARTITION BY DEPARTMENT ORDER BY salary DESC) AS rank_number
FROM employees;

SELECT *,
       Dense_RANK() OVER (ORDER BY salary DESC) AS rank_number
FROM employees;

select name, salary,
       rank() over (order by salary desc) as rank,
       dense_rank() over (order by salary desc) as dense_rank
from employees;

WITH Emplosal AS (
    SELECT Salary, RANK() OVER (ORDER BY Salary DESC) AS Rank_Salry
    FROM Employees
)
SELECT TOP 1 Salary FROM Emplosal WHERE Rank_Salry = 2;

WITH Emplosal AS (
    SELECT Salary, Dense_RANK() OVER (ORDER BY Salary DESC) AS Rank_Salry
    FROM Employees
)
SELECT TOP 1 Salary FROM Emplosal WHERE Rank_Salry = 4;