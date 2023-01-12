select * from employee;

-- 1. Jonie Weber just got married to Bob Williams. She has requested that her last name be updated to Weber-Williams.

update employee 
set last = 'Weber-Williams' 
where first = 'Jonie' and last = 'Weber';

-- 2. Dirk Smith’s birthday is today, add 1 to his age.

update employee 
set age=age+1 
where first='Dirk' and last='Smith';

-- 3. All secretaries are now called “Administrative Assistant”. Update all titles accordingly.

update employee 
set title = 'Administrative Assistant' 
where title = 'Secretary';

-- 4. Everyone that’s making under 30000 are to receive a 3500 a year raise.

update employee 
set salary=salary+3500 
where salary < 30000; 

-- 5. Everyone that’s making over 33500 are to receive a 4500 a year raise.

update employee 
set salary=salary+4500 
where salary > 33500; 

-- 6. All “Programmer II” titles are now promoted to “Programmer III”.


-- 7. All “Programmer” titles are now promoted to “Programmer II”.
