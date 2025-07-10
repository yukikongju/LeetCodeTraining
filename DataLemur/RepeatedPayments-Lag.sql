with previous_transactions as (
  select 
    transaction_id, 
    merchant_id, 
    credit_card_id, 
    amount,
    transaction_timestamp,
    lag(transaction_timestamp) over(partition by merchant_id, credit_card_id, amount order by transaction_timestamp) as prev_transaction
  from transactions
)

select count(*) 
from previous_transactions 
where 
  transaction_timestamp - interval '10 MINUTE' <= prev_transaction

-- select * from previous_transactions


