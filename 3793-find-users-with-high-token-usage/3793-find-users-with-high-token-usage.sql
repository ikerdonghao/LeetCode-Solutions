# Write your MySQL query statement below
WITH user_summary AS
(
    select
        user_id,
        count(*) over(partition by user_id rows between unbounded preceding and unbounded following) as prompt_count,
        avg(tokens) over(partition by user_id rows between unbounded preceding and unbounded following) as avg_tokens,
        tokens-avg(tokens) over(partition by user_id rows between unbounded preceding and unbounded following) as is_more_than_average
    from prompts
)

select
    distinct user_id,prompt_count,round(avg_tokens,2) as avg_tokens
from user_summary
where prompt_count>=3
    and is_more_than_average>0
order by avg_tokens desc,user_id