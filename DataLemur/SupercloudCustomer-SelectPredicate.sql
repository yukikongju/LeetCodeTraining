--  https://datalemur.com/questions/supercloud-customer
with customer_product_counts as (
  select 
    c.customer_id, 
    count(distinct p.product_category) as category_count
  from customer_contracts as c 
  join products as p 
  on c.product_id = p.product_id
  group by c.customer_id
)

select 
  customer_id
from customer_product_counts
WHERE
  category_count = (
    select count(distinct product_category) from products
  )
