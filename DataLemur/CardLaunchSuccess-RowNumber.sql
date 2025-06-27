--  https://datalemur.com/questions/card-launch-success
with card_issued_ranked as (
  select 
    issue_month, issue_year, card_name, issued_amount, 
    row_number() over (partition by card_name order by issue_year, issue_month) as rn 
  from monthly_cards_issued
)

select 
  card_name, 
  issued_amount
from card_issued_ranked
where rn = 1
order by issued_amount desc
