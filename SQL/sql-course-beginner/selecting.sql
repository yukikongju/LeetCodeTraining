--  https://www.sqlcourse.com/beginner-course/selecting-data/

-- 1. Display the first name and age for everyone that’s in the table. 
select first, age from empinfo;

-- 2. Display the first name, last name, and city for everyone that’s not from Payson. 

select first, last, city from empinfo
where city <> 'Payson';

--  3. Display all columns for everyone that is over 40 years old.

select * from empinfo
where age > 40;

-- 4. Display the first and last names for everyone whose last name ends in an “ay”.

select first, last from empinfo 
where last like'%ay';

-- 5. Display all columns for everyone whose first name equals “Mary”.

select * from empinfo where first = 'Mary';

-- 6. Display all columns for everyone whose first name contains “Mary”. 
select * from empinfo 
where first like '%Mary%';


