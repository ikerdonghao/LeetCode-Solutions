# Write your MySQL query statement below
WITH reaction_summary AS
(SELECT
    user_id,
    reaction,
    count(*) as reaction_count,
    sum(count(*)) over(partition by user_id) as user_reaction_count
FROM reactions
GROUP BY 1,2
)


SELECT 
    user_id,
    reaction as dominant_reaction,
    round(reaction_count / user_reaction_count,2) as reaction_ratio 
from reaction_summary
where user_reaction_count >= 5
    and reaction_count / user_reaction_count > 0.6
order by reaction_ratio desc, user_id