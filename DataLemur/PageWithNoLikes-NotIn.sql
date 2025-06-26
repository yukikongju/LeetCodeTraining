select 
  page_id
from pages
where 
  page_id not in (
    select page_id from page_likes where page_id not null
  )
order by page_id;
