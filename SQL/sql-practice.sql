-- Solving questions from https://www.sql-practice.com/

-------------------------------  EASY


-- Q1: Show first name, last name, and gender of patients who's gender is 'M'

SELECT 
  first_name, 
  last_name, 
  gender
FROM patients 
WHERE gender = 'M';


-- Q2: Show first name and last name of patients who does not have allergies (null).

SELECT
  first_name,
  last_name
FROM patients
WHERE allergies IS NULL;


-- Q3: Show first name of patients that start with the letter 'C'

SELECT
  first_name
FROM patients
WHERE first_name LIKE 'C%';


-- Q4: Show first name and last name of patients that weight within the range of 100 to 120 (inclusive)

SELECT
  first_name,
  last_name
FROM patients
WHERE weight BETWEEN 100 AND 120;


-- Q5: Update the patients table for the allergies column. If the patient's allergies is null then replace it with 'NKA'

UPDATE patients
SET allergies = 'NKA'
WHERE allergies IS NULL;


-- Q6: Show first name and last name concatinated into one column to show their full name.

SELECT
  CONCAT(first_name, ' ', last_name) AS full_name
FROM patients;

-- Q7: Show first name, last name, and the full province name of each patient.

SELECT
  first_name,
  last_name,
  province_name
FROM patients
  JOIN provinces ON provinces.province_id = patients.province_id;


-- Q8: Show how many patients have a birth_date with 2010 as the birth year.

SELECT COUNT(*) AS total_patients
FROM patients
WHERE YEAR(birth_date) = 2010;

-- Q9: Show the first_name, last_name, and height of the patient with the greatest height.

SELECT
  first_name,
  last_name,
  MAX(height) AS height
FROM patients;

SELECT
  first_name,
  last_name,
  height
FROM patients
WHERE height = (
    SELECT max(height)
    FROM patients
  )


-- Q10: Show all columns for patients who have one of the following patient_ids: 1,45,534,879,1000

SELECT *
FROM patients
WHERE
  patient_id IN (1, 45, 534, 879, 1000);


-- Q11: Show the total number of admissions

SELECT COUNT(*) AS total_admissions
FROM admissions;

-- Q12: Show all the columns from admissions where the patient was admitted and discharged on the same day.

SELECT *
FROM admissions
WHERE admission_date = discharge_date;

-- Q13: Show the total number of admissions for patient_id 573.

SELECT
  patient_id,
  COUNT(*) AS total_admissions
FROM admissions
WHERE patient_id = 573;


-------------------------------  MEDIUM



-- Q14: Show unique birth years from patients and order them by ascending.

SELECT
  DISTINCT YEAR(birth_date) AS birth_year
FROM patients
ORDER BY birth_year;

-- Q15: Show unique first names from the patients table which only occurs once in the list.

SELECT first_name
FROM patients
GROUP BY first_name
HAVING COUNT(*) = 1


-- Q16: Show patient_id and first_name from patients where their first_name start and ends with 's' and is at least 6 characters long.

SELECT
  patient_id,
  first_name
FROM patients
WHERE first_name LIKE 's____%s';

SELECT
  patient_id,
  first_name
FROM patients
WHERE
  first_name LIKE 's%s'
  AND len(first_name) >= 6;

-- Q17: Show patient_id, first_name, last_name from patients whos primary_diagnosis is 'Dementia'.

SELECT
  patients.patient_id,
  first_name,
  last_name
FROM patients
  JOIN admissions ON admissions.patient_id = patients.patient_id
WHERE primary_diagnosis = 'Dementia';


-- Q18: Show patient_id, first_name, last_name from the patients table.  Order the rows by the first_name ascending and then by the last_name descending.

SELECT
  patient_id,
  first_name,
  last_name
FROM patients
ORDER BY
  first_name ASC,
  last_name DESC;


-- Q19: Show the total amount of male patients and the total amount of female patients in the patients table

SELECT 
  (SELECT count(*) FROM patients WHERE gender='M') AS male_count, 
  (SELECT count(*) FROM patients WHERE gender='F') AS female_count;


-- Q20: Show first and last name, allergies from patients which have allergies to either 'Penicillin' or 'Morphine'. Show results ordered ascending by allergies then by first_name then by last_name.

SELECT
  first_name,
  last_name,
  allergies
FROM patients
WHERE
  allergies IN ('Penicillin', 'Morphine')
ORDER BY
  allergies,
  first_name,
  last_name;


-- Q21: Show patient_id, primary_diagnosis from admissions. Find patients admitted multiple times for the same primary_diagnosis.

SELECT
  patient_id,
  primary_diagnosis
FROM admissions
GROUP BY
  patient_id,
  primary_diagnosis
HAVING COUNT(*) > 1;

-- Q22: Show the city and the total number of patients in the city in the order from most to least patients.

SELECT
  city,
  COUNT(*) AS num_patients
FROM patients
GROUP BY city
ORDER BY num_patients DESC;

-- Q23: Show first name, last name and role of every person that is either patient or physician.  The roles are either "Patient" or "Physician"

SELECT first_name, last_name, "Patient" as "Role" FROM patients
    UNION
SELECT first_name, last_name, "Physician" FROM physicians;


-- Q24: Show all allergies ordered by popularity. Remove 'NKA' and NULL values from query.

SELECT
  allergies,
  count(allergies) AS total_diagnosis
FROM patients
GROUP BY allergies
HAVING
  allergies IS NOT NULL
  AND allergies IS NOT 'NKA'
ORDER BY total_diagnosis DESC

SELECT
  allergies,
  count(*)
FROM patients
WHERE allergies NOT IN ('NKA', 'NULL')
GROUP BY allergies
ORDER BY count(*) DESC


-- Q25: Show all patient's first_name, last_name, and birth_date who were born in the 1970s decade. Sort the list starting from the earliest birth_date.

SELECT
  first_name,
  last_name,
  birth_date
FROM patients
WHERE
  YEAR(birth_date) BETWEEN 1970 AND 1979
ORDER BY birth_date ASC;


-- Q26: We want to display each patient's full name in a single column. Their last_name in all upper letters must appear first, then first_name in all lower case letters. Separate the last_name and first_name with a comma. Order the list by the first_name in decending order EX: SMITH,jane

SELECT
  CONCAT(UPPER(last_name), ',', LOWER(first_name)) AS new_name_format
FROM patients
ORDER BY first_name DESC;


-- Q27: Show the province_id(s), sum of height; where the total sum of its patient's height is greater than or equal to 7,000.

SELECT
  province_id,
  SUM(height) AS sum_height
FROM patients
GROUP BY province_id
HAVING sum_height >= 7000

-- Q28: Show the difference between the largest weight and smallest weight for patients with the last name 'Maroni'

SELECT
  (MAX(weight) - MIN(weight)) AS weight_delta
FROM patients
WHERE last_name = 'Maroni';


-- Q29: Based on the cities that our patients live in, show unique cities that are in province_id 'NS'?

SELECT DISTINCT(city) AS unique_cities
FROM patients
WHERE province_id = 'NS';


-- Q30: Show all of the month's day numbers and how many admission_dates occurred on that number. Sort by the day with most admissions to least admissions.

SELECT
  DAY(admission_date) AS day_number,
  COUNT(*) AS number_of_admissions
FROM admissions
GROUP BY day_number
ORDER BY number_of_admissions DESC


-- Q31: Show the patient_id, nursing_unit_id, room, and bed for patient_id 542's most recent admission_date.

SELECT
  patient_id,
  nursing_unit_id,
  room,
  bed
FROM admissions
WHERE patient_id = 542
GROUP BY patient_id
HAVING
  admission_date = MAX(admission_date);

SELECT
  patient_id,
  nursing_unit_id,
  room,
  bed
FROM admissions
WHERE
  patient_id = '542'
  AND admission_date = (
    SELECT MAX(admission_date)
    FROM admissions
    WHERE patient_id = '542'
  )


SELECT
  patient_id,
  nursing_unit_id,
  room,
  bed
FROM admissions
WHERE patient_id = 542
ORDER BY admission_date DESC
LIMIT 1

SELECT
  patient_id,
  nursing_unit_id,
  room,
  bed
FROM admissions
GROUP BY patient_id
HAVING
  patient_id = 542
  AND max(admission_date)

-- Q32: Show the nursing_unit_id and count of admissions for each nursing_unit_id. Exclude the following nursing_unit_ids: 'CCU', 'OR', 'ICU', 'ER'.

SELECT
  nursing_unit_id,
  COUNT(*) AS total_admissions
FROM admissions
WHERE
  nursing_unit_id NOT IN ('CCU', 'OR', 'ICU', 'ER')
GROUP BY nursing_unit_id;


-- Q33: Show patient_id, attending_physician_id, and primary_diagnosis for admissions that match one of the two criteria: 1. patient_id is an odd number and attending_physician_id is either 1, 5, or 19.  2. attending_physician_id contains a 2 and the length of patient_id is 3 characters.

SELECT
  patient_id,
  attending_physician_id,
  primary_diagnosis
FROM admissions
WHERE
  (
    attending_physician_id IN (1, 5, 19)
    AND patient_id % 2 != 0
  )
  OR 
  (
    attending_physician_id LIKE '%2%'
    AND len(patient_id) = 3
  )


-------------------------------  HARD


-- Q34:


-- Q35:


-- Q36:



-- Q37:


-- Q38:




