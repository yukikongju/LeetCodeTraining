--  https://datalemur.com/questions/odd-even-measurements
with measurements_order as (
  select 
    *,
    cast(measurement_time as date) as measurement_day,
    row_number() over (partition by extract(day from measurement_time) order by extract(hour from measurement_time)) as rn
  from measurements
)

select 
  measurement_day, 
  sum(measurement_value) filter(where rn % 2 != 0) as odd_sum,
  sum(measurement_value) filter(where rn % 2 = 0) as even_sum
from measurements_order
group by measurement_day
order by measurement_day asc
