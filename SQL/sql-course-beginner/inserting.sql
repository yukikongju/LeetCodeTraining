

create table employee 
(first varchar(30), 
 last varchar(30), 
 title varchar(30), 
 age number(3),
 salary number(8, 2));

insert into employee 
(first, last, title, age, salary) 
values ('Jonie', 'Weber', 'Secretary', 28, 19500.00);

insert into employee 
(first, last, title, age, salary) 
values ('Potsy', 'Weber', 'Programmer', 32, 45300.00);

insert into employee 
(first, last, title, age, salary) 
values ('Dirk', 'Smith', 'Programmer II', 45, 72020.00);

-- 1. Select all columns for everyone in your employee table.
select * from employee;

-- 2. Select all columns for everyone with a salary over 30000.
select * from employee 
where salary > 30000;

-- 3. Select first and last names for everyone that’s under 30 years old.
select first, last from employee 
where age < 30;

-- 4. Select first name, last name, and salary for anyone with “Programmer” in their title.

select first, last, salary from employee 
where title like '%Programmer%';

-- 5. Select all columns for everyone whose last name contains “ebe”.

select * from employee 
where last like '%ebe';

-- 6. Select the first name for everyone whose first name equals “Potsy”.

select * from employee 
where first = 'Potsy';

-- 7. Select all columns for everyone over 80 years old.

select * from employee 
where age > 80;

-- 8. Select all columns for everyone whose last name ends in “ith”.

select * from employee where last like '%ith';
