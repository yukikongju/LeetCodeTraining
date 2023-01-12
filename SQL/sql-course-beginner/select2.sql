select * from items_ordered;

--  From the items_ordered table, select a list of all items purchased for customerid 10449. Display the customerid, item, and price for this customer.

select customerid, item, price 
from items_ordered
where customerid = 10449;

--  Select all columns from the items_ordered table for whoever purchased a Tent.

select * from items_ordered 
where item = 'Tent';

--  Select the customerid, order_date, and item values from the items_ordered table for any items in the item column that start with the letter “S”.

select customerid, order_date, price 
from items_ordered 
where item like 'S%';

--  Select the distinct items in the items_ordered table. In other words, display a listing of each of the unique items from the items_ordered table.

select distinct item from items_ordered;
