SELECT
  page_id
from pages
where not exists (
  select page_id 
  from page_likes as likes 
  where likes.page_id = pages.page_id
)
order by page_id;
