--  https://datalemur.com/questions/sql-highest-grossing
with product_ranking as (
  select 
    category, product, 
    sum(spend) as total_spend, 
    row_number() over (partition by category order by sum(spend) desc) as rn 
  from product_spend
  where 
    extract(year from transaction_date) = 2022
  group by category, product
)

select 
  category, product, total_spend
from product_ranking 
where rn <= 2
order by category, total_spend desc


