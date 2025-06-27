--  https://datalemur.com/questions/sql-top-three-salaries
with ranked_salary as (
  select 
    employee_id, name, salary, department_id,
    dense_rank() over (partition by department_id order by salary desc) as ranking
  from employee
)

select 
  d.department_name, 
  s.name, 
  s.salary
from ranked_salary as s
inner join department as d 
on s.department_id = d.department_id
where 
  ranking <= 3
order by d.department_name asc, salary desc, name asc
  
