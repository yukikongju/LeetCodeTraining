--  https://datalemur.com/questions/signup-confirmation-rate
select 
  round(count(t.email_id)::decimal / count(distinct e.email_id), 2) as confirm_rate
from emails as e 
left join texts as t 
on e.email_id = t.email_id
  and t.signup_action = 'Confirmed'
