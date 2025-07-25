use sample_database

CREATE TABLE Accounts (
    account_id INT PRIMARY KEY,
    account_name VARCHAR(50),
    balance DECIMAL(10, 2)
);

create table account_insertion_details (
   accountid int,
   account_log varchar(100)
   );

CREATE TRIGGER trigger_for_insertion
ON Accounts
AFTER INSERT
AS
BEGIN
    INSERT INTO account_insertion_details (accountid, account_log)
    SELECT account_id, 'inserted' FROM INSERTED;
END;

-- Inserting sample account records
INSERT INTO Accounts (account_id, account_name, balance)
VALUES
(101, 'Ravi Kumar', 25000.50),
(102, 'Priya Sharma', 18000.00),
(103, 'John Abraham', 32000.75),
(104, 'Divya Singh', 4500.00),
(105, 'Amit Patel', 9800.25);

select * from account_insertion_details;


-- creating account log for delete

create table deletetabledetails(
account_id int, account_log nvarchar(1000)
);
create trigger delete_trigger
on accounts
after delete
as
begin
  declare @id int;
  select @id = account_id from deleted;
  insert into deletetabledetails values (@id,'employee with id = ' + cast(@id as nvarchar(5)) + ' is deleted at ' + cast(getdate() as nvarchar(20))
    );
end;

delete from accounts where account_id=103;

select * from deletetabledetails;

--using instead of 

create trigger insert_insteadoftrigger on Accounts
instead of insert
as
begin
print 'the insertion option is curretly denied for this Table'
end

insert into accounts values (105, 'Amit Patel', 9800.25);


-- creating the update 

create table account_update_audit (
    audit_msg nvarchar(2000)
);
drop table account_update_audit;
drop trigger update_trigger_table;
create trigger update_trigger_table
on accounts
for update
as
begin
    declare @auditstring nvarchar(2000);
    declare @id int;
    declare @oldaccount_name varchar(50), @newaccount_name varchar(50);
    declare @oldbalance decimal(10,2), @newbalance decimal(10,2);

    select * into #TempTable from inserted;

    while exists (select account_id from #TempTable)
    begin
        set @auditstring = '';
        set @id = null;

        select top 1 
            @id = account_id,
            @newaccount_name = account_name,
            @newbalance = balance
        from #TempTable;

        select 
            @oldaccount_name = account_name,
            @oldbalance = balance
        from deleted where account_id = @id;

        set @auditstring = 'Account with ID = ' + cast(@id as nvarchar(5)) + ' updated:';

        if @oldaccount_name <> @newaccount_name
            set @auditstring = @auditstring + ' NAME changed from ' + @oldaccount_name + ' to ' + @newaccount_name + '.';

        if @oldbalance <> @newbalance
            set @auditstring = @auditstring + ' BALANCE changed from ' + cast(@oldbalance as nvarchar(20)) + ' to ' + cast(@newbalance as nvarchar(20)) + '.';

        insert into account_update_audit values(@auditstring);

        delete from #TempTable where account_id = @id;
    end
end; 

update accounts set account_name='Santosh' where account_id=104;

select * from account_update_audit;

-- creating commit and rollback transaction

create table student_example
(id int primary key,name varchar(40),age int,department varchar(40));

INSERT INTO student_example (id, name, age, department) VALUES
(1, 'Arun Kumar', 20, 'Computer Science'),
(2, 'Priya Sharma', 21, 'Electronics'),
(3, 'Rahul Verma', 22, 'Mechanical'),
(4, 'Sneha Reddy', 20, 'Information Technology'),
(5, 'Vikram Singh', 23, 'Civil');

begin transaction
insert into student_example values (6,'Mani',25,'civi');
insert into student_example valu
es (6,'Mani',25,'civi');
commit transaction

DELETE FROM student_example WHERE id = 6 OR id = 7;

-- using try caatch block

begin try
   begin transaction
   insert into student_example values (8,'Mani',25,'civi');
   insert into student_example values (8,'Kani',25,'civi');
   delete from student_example where id=3;
   commit  TRANSACTION
end try
begin catch
     rollback transaction
     print 'Error occured' + ERROR_MESSAGE()
end catch

SELECT * FROM student_example

--creating the implicit tranction on 

set implicit_transactions on;

insert into student_example values (9, 'arun kumar', 20, 'computer science');
insert into student_example values (10, 'priya sharma', 21, 'electronics');

commit transaction;

select * from student_example;

insert into student_example values (11, 'rahul verma', 22, 'mechanical');
update student_example set department = 'it' where id = 2;

rollback transaction;
  
select * from student_example;



