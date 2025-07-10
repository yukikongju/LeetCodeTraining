with total_order_count as (
  select count(distinct order_id) as total_order_count from orders
)

SELECT
  case 
    when order_id = total_order_count then order_id
    when order_id % 2 = 0 then order_id - 1
    when order_id % 2 = 1 then order_id + 1
  end as order_id, 
  o.item
FROM orders o
CROSS JOIN total_order_count t
order by order_id

-- select * from total_order_count
