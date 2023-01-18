--  https://leetcode.com/problems/department-highest-salary/description/

select 
    D.name as 'Department', 
    E.name as 'Employee', 
    E.salary as 'Salary'
from Employee E 
inner join Department D on (E.departmentId = D.id)
where (E.departmentId, E.salary) in (
    select E.departmentId, max(E.salary)
    from Employee E
    group by E.departmentId
);
