## Indexes
* single column 
* multi column
* unique

* Removing an index

'''
create index index_emp_name on employee (emp_name);

create index index_emp_name_id on employee (emp_name, emp_id);

select * from employee where emp_name = "Alice"

create index idx_salary ON employee(salary);

select * from employee where salary > 60000;
'''

## Execution plans

* Accessing
* Index Scan
* Estimated cost
'''
explain select* from employee where emp_name = "Charlie" 
explain analyze select* from employee where emp_name = "Charlie";
'''

## Transactions

* Transactions in SQL are group of operations that are executed as one unit
* ACID prperties(Automicity, Consistency, Isolation, Durability)
* Starting
* commiting 
* Rollbacking
