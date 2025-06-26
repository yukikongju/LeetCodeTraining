with user_tweets_counts as (
  select 
    user_id, count(*) as tweet_counts
  from tweets
  where extract(year from tweet_date) = 2022
  group by user_id
), tweets_bucket as (
  select 
    tweet_counts as tweet_buckets, 
    count(*) as user_nums
  from user_tweets_counts
  group by tweet_counts
)

select * from tweets_bucket

