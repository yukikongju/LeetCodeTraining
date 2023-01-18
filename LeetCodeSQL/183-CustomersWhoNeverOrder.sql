--  https://leetcode.com/problems/customers-who-never-order/submissions/880318672/

select C.name as 'Customers' 
from Customers C
where C.id not in (
    select customerId from Orders
);
