-- 1. Select the maximum price of any item ordered in the items_ordered table. Hint: Select the maximum price only.

select max(price) from items_ordered;

-- 2. Select the average price of all of the items ordered that were purchased in the month of Dec.

select avg(price) from items_ordered 
where order_date like '%Dec%';

-- 3. What are the total number of rows in the items_ordered table?

select count(*) from items_ordered;

-- 4. For all of the tents that were ordered in the items_ordered table, what is the price of the lowest tent? Hint: Your query should return the price only.

select min(price) from items_ordered 
where item = 'Tent';
