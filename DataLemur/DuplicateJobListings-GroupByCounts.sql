with duplicates_job_listings as (
  select 
    company_id
  from job_listings
  group by company_id, title
  having count(*) > 1
)

select count(distinct company_id) from duplicates_job_listings
