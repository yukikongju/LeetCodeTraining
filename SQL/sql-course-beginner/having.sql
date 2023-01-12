-- 1. How many people are in each unique state in the customers table that have more than one person in the state? Select the state and display the number of how many people are in each if it’s greater than 1.

select state, count(*) 
from customers
group by state
having count(*) > 1

-- 2. From the items_ordered table, select the item, maximum price, and minimum price for each specific item in the table. Only display the results if the maximum price for one of the items is greater than 190.00.

select item, max(price), min(price) 
from items_ordered
group by item 
having max(price) > 190.00;

-- 3. How many orders did each customer make? Use the items_ordered table. Select the customerid, number of orders they made, and the sum of their orders if they purchased more than 1 item.

select customerid, count(*), sum(price) 
from items_ordered
group by customerid
having count(*) > 1;
