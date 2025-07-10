with company_average as (
  select 
    payment_date, 
    avg(amount) as co_avg_salary
  from salary 
  group by payment_date
), department_average as (
  select 
    e.department_id, s.payment_date, 
    avg(amount) as dept_avg_salary
  from salary as s 
  left join employee as e 
  on s.employee_id = e.employee_id
  group by 
    s.payment_date, e.department_id
)

select 
  d.department_id, 
  to_char(d.payment_date, 'MM-YYYY') as payment_date, 
  -- d.dept_avg_salary, c.co_avg_salary,
  case 
    when d.dept_avg_salary < c.co_avg_salary then 'lower'
    when d.dept_avg_salary > c.co_avg_salary then 'higher'
    else 'same'
  end as comparison
from department_average as d 
inner join company_average as c 
on d.payment_date = c.payment_date
where 
  d.payment_date = '03/31/2024 00:00:00'

