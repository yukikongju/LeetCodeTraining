--- EXISTS

select 
  extract(month from event_date) as month, 
  count(distinct current_month.user_id) as monthly_active_users
from user_actions as current_month
where   
  extract(month from event_date) =  7
  and extract(year from event_date) = 2022
  and EXISTS (
    select 
      distinct last_month.user_id
    from user_actions as last_month
    where  
      last_month.user_id = current_month.user_id
      and extract(month from last_month.event_date) = extract(month from current_month.event_date - interval '1 MONTH')
  )
group by extract(month from event_date)

---- NAIVE

-- with previous_month as (
--   select distinct user_id from user_actions
--   where 
--     extract(month from event_date) = 6 and 
--     extract(year from event_date) = 2022
-- ), current_month as (
--   select distinct user_id from user_actions
--   where 
--     extract(month from event_date) = 7 and 
--     extract(year from event_date) = 2022
-- )

-- select 
--   count(*)
-- from previous_month as p 
-- inner join current_month as c 
-- on c.user_id = p.user_id



