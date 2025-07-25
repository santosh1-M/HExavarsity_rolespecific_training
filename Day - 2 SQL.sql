select * from Employees;

-- creating Procedure

create proc usp_selectingalltable
as
Begin
select * from employees
End

Exec usp_selectingalltable

-- creating procedure for two columns

create proc usp_selectingtwocolumns
as
Begin
select name,department from employees
End

exec usp_selectingtwocolumns

-- creating procedure for getting values based on input

create proc usp_selectingbasedoninput
(@dept varchar(20))
as
Begin
select * from employees where department=@dept
End

exec usp_selectingbasedoninput 'HR'

create proc usp_selectingbasedoninputname
(@nam varchar(20))
as
Begin
select * from employees where name=@nam
End

exec usp_selectingbasedoninputname 'Alice'

-- Altering Stored procedure

alter proc usp_selectingbasedoninput
(@sal int)
as
Begin
select * from employees where salary=@sal
End

exec usp_selectingbasedoninput 50000

-- getting ouput based on ouput variable

create proc usp_returnvalue
(@num1 int,@num2 int,@product1 int out)
as
Begin
set @product1=@num1*@num2
End

declare @productresult int
exec usp_returnvalue 2,3,@productresult  out 
print @productresult

-- getting value in output from table

create proc usp_selectingfromtable
(@dept varchar(20),@CountResult int out)
as
Begin
select @countresult=count(emp_id) from employees where department=@dept
End

declare @Countresult1 int 
exec usp_selectingfromtable 'HR',@Countresult1 out
print @Countresult1

declare @Countresult2 int 
exec usp_selectingfromtable 'IT',@Countresult2 out
print @Countresult2

sp_helptext usp_selectingfromtable

--creating function for scalar types

create function fn(@num1 int)
returns int
as 
begin
return @num1*@num1*@num1
end

select dbo.fn(5);


--creating inline function

select * from employees

create function fn_getdepartmentbyname(@nam varchar(20))
returns table 
as
return (select * from employees where department = @nam)

select * from dbo.fn_getdepartmentbyname('IT')

-- perfoming multivalued 

create function fn_multivalued()
returns @mytable Table(sal int)
as
begin
insert into @mytable select salary from employees
return
end

select * from fn_multivalued()

CREATE TABLE tbl_Employee
(
Id INT,
Name VARCHAR(50),
Salary INT,
Gender VARCHAR(10),
City VARCHAR(50),
Dept VARCHAR(50)
)
GO
INSERT INTO tbl_Employee VALUES (3,'Pranaya', 4500, 'Male', 'New York', 'IT')
INSERT INTO tbl_Employee VALUES (1,'Anurag', 2500, 'Male', 'London', 'IT')
INSERT INTO tbl_Employee VALUES (4,'Priyanka', 5500, 'Female', 'Tokiyo', 'HR')
INSERT INTO tbl_Employee VALUES (5,'Sambit', 3000, 'Male', 'Toronto', 'IT')
INSERT INTO tbl_Employee VALUES (7,'Preety', 6500, 'Female', 'Mumbai', 'HR')
INSERT INTO tbl_Employee VALUES (6,'Tarun', 4000, 'Male', 'Delhi', 'IT')
INSERT INTO tbl_Employee VALUES (2,'Hina', 500, 'Female', 'Sydney', 'HR')
INSERT INTO tbl_Employee VALUES (8,'John', 6500, 'Male', 'Mumbai', 'HR')
INSERT INTO tbl_Employee VALUES (10,'Pam', 4000, 'Female', 'Delhi', 'IT')
INSERT INTO tbl_Employee VALUES (9,'Sara', 500, 'Female', 'London', 'IT')


select * from tbl_employee

create clustered index ind_clus on tbl_employee(id)

-- Droping index

drop index ind_clus on tbl_employee

INSERT INTO tbl_Employee VALUES (19,'Pam', 4000, 'Female', 'Delhi', 'IT')
INSERT INTO tbl_Employee VALUES (11,'Sara', 500, 'Female', 'London', 'IT')
INSERT INTO tbl_Employee VALUES (15,'Pam', 4000, 'Female', 'Delhi', 'IT')

create unique index ind_unique on tbl_employee(id)

select * from tbl_employee

-- try to insert duplicate value

INSERT INTO tbl_Employee VALUES (15,'Pam', 4000, 'Female', 'Delhi', 'IT')


-- display likes this when we run query :Msg 2601, Level 14, State 1, Line 161
--Cannot insert duplicate key row in object 'dbo.tbl_Employee' with unique index 'ind_unique'. The duplicate key value is (15).
--The statement has been terminated.

-- creating loop

CREATE Table tblOrder
(Id INT,
CustomerId INT,
ProductID varchar(50),
ProductName varchar(50)
)

DECLARE @i int=1
WHILE @i<4000
BEGIN
SET @i=@i+1
	IF(@i<1000)
	BEGIN
	INSERT INTO tblOrder values (@i,1,'Product-101','iPad Air')
	END
	ELSE IF(@i<2000)
	BEGIN
	INSERT INTO tblOrder values (@i,3,'Product-3001','Lenova Think Pad')
	END
	ELSE IF(@i<3000)
	BEGIN
	INSERT INTO tblOrder values (@i,2,'Product-100','Wireless Keyboard')
	END
	ELSE IF(@i<4000)
	BEGIN
	INSERT INTO tblOrder values (@i,1,'Product-300','Tablet')
	END
END

select count(*) from tblOrder


SELECT * FROM tblOrder WHERE ProductID='Product-3001' AND CustomerId=3

CREATE NONCLUSTERED INDEX idx_tblOrder_pid
ON tblOrder(ProductId)
INCLUDE([Id],[CustomerId],[ProductName])

SELECT * FROM tblOrder WHERE ProductID='Product-100'