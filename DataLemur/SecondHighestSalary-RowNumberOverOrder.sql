--  https://datalemur.com/questions/sql-second-highest-salary
with salary_ranked as (
  select 
    distinct salary,
    row_number() over (order by salary desc) as rn
  from employee
  order by salary desc
)

select salary from salary_ranked where rn = 2
