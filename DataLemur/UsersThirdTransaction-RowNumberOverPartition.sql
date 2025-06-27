--  https://datalemur.com/questions/sql-third-transaction
with transactions_ordered as (
  select 
    user_id, spend, transaction_date,
    row_number() over (partition by user_id order by transaction_date asc) as rn
  from transactions
)

select 
  user_id, spend, transaction_date
from transactions_ordered
where rn = 3
order by user_id

