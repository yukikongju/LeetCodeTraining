--  https://datalemur.com/questions/international-call-percentage
with phone_calls_info as (
  select 
    calls.caller_id, 
    calls.receiver_id, 
    caller.country_id as caller_country, 
    receiver.country_id as receiver_country
  from phone_calls as calls 
  left join phone_info as caller 
    on calls.caller_id = caller.caller_id 
  left join phone_info as receiver 
    on calls.receiver_id = receiver.caller_id
)

select
  round(100.0 * count(*) filter (where caller_country <> receiver_country) / count(*), 1) as international_calls_pct
from phone_calls_info
