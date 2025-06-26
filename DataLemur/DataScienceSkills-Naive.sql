with python_skills as (
  select candidate_id
  from candidates
  where skill = 'Python'
), tableau_skills as (
  select candidate_id
  from candidates
  where skill = 'Tableau'
), postgres_skills as (
  select candidate_id
  from candidates
  where skill = 'PostgreSQL'
)

select py.candidate_id 
from python_skills py 
join tableau_skills t on py.candidate_id = t.candidate_id
join postgres_skills po on py.candidate_id = po.candidate_id;
