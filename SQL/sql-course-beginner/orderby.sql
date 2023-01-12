-- 1. Select the lastname, firstname, and city for all customers in the customers table. Display the results in Ascending Order based on the lastname.

select lastname, firstname, city 
from customers
order by lastname asc;

-- 2. Same thing as exercise #1, but display the results in Descending order.


-- 3. Select the item and price for all of the items in the items_ordered table that the price is greater than 10.00. Display the results in Ascending order based on the price.

select item, price 
from items_ordered
where price > 10.00
order by price asc;
