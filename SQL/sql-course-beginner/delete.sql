-- 1. Jonie Weber-Williams just quit, remove her record from the table.

delete from employee 
where first = 'Jonie' and last = 'Weber-Williams';

-- 2. It’s time for budget cuts. Remove all employees who are making over 70000 dollars.

delete from employee 
where salary > 70000;
