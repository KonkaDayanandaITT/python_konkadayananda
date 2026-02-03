## Sql joins
* Join 
* left join
* right join
* cross join

'''
select e.emp_name, e.emp_id, d.dept_name
from employees e
join departments d on e.dept_id = d.dept_id;

select e.emp_name, e.emp_id, d.dept_name
from employees e
left join departments d on e.dept_id = d.dept_id;

select e.emp_name, e.emp_id, d.dept_name
from employees e
right departments d on e.dept_id = d.dept_id;

select e.emp_name, e.emp_id, d.dept_name
from employees e
cross join departments d;
'''

## Unions
* union
* union all

## subqueries

'''
select emp_name,salary
from employee
where salary > (
	select avg(salary)
    from employee
);

also using where, in, not in, select, from etc.
'''

## Aggregate Functions
'''
select count(*) as total_employees
from employee

select sum(salary) as total_salary
from employee

select avg(salary) as avg_salary
from employee

select min(salary) as min_salary
from employee

select max(salary) as max_salary
from employee
'''

## Group by, where, Having
'''
select dept, sum(salary) as total_salary
from employee
group by dept;

select dept, avg(salary) as avg_salary
from employee
where salary > 50000
group by dept;

select dept, avg(salary) as avg_salary
from employee
group by dept
having avg(salary) > 50000;
'''