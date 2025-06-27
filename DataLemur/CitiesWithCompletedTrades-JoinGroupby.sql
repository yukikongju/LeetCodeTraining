--  https://datalemur.com/questions/completed-trades
 SELECT
  u.city, 
  count(*) as total_orders
 FROM trades t
 JOIN users u on t.user_id = u.user_id
 where t.status = 'Completed'
 GROUP BY u.city
 order by count(*) DESC
 limit 3
