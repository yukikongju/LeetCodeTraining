--  https://datalemur.com/questions/sql-avg-review-ratings
select 
  extract(month from submit_date) as mth, 
  product_id as product, 
  round(avg(stars), 2) as stars
from reviews
group by 
  extract(month from submit_date), product_id

