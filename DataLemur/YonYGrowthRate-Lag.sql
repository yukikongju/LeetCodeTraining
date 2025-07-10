with transactions_by_year as (
  select 
    extract(year from transaction_date) as year, 
    product_id, 
    sum(spend) as curr_year_spend, 
    lag(sum(spend)) over (partition by product_id order by product_id, extract(year from transaction_date) asc) as prev_year_spend
  from user_transactions
  group by extract(year from transaction_date), product_id
)

select 
  year, 
  product_id,
  curr_year_spend, 
  prev_year_spend, 
  round((curr_year_spend - prev_year_spend) / prev_year_spend * 100, 2) as yoy_rate
from transactions_by_year


