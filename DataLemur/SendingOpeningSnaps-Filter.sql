--  https://datalemur.com/questions/time-spent-snaps
with snap_activities as (
  SELECT
    ag.age_bucket, 
    round(100.0 * sum(act.time_spent) FILTER (WHERE act.activity_type = 'open') / sum(act.time_spent), 2) as open_perc, 
    round(100.0 * sum(act.time_spent) FILTER (WHERE act.activity_type = 'send') / sum(act.time_spent), 2) as send_perc
  FROM activities as act 
  INNER JOIN age_breakdown as ag 
    on act.user_id = ag.user_id
  WHERE
    act.activity_type in ('open', 'send')
  GROUP BY ag.age_bucket
)

select * from snap_activities
