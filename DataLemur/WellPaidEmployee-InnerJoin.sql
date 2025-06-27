select 
  e.employee_id, e.name as employee_name
from employee e 
inner join employee mng on e.manager_id = mng.employee_id
where mng.salary < e.salary
order by employee_id
