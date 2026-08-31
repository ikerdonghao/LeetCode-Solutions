# Write your MySQL query statement below
WITH student_summary AS
(
    SELECT
        distinct
        student_id,
        subject,
        first_value(score) over(partition by student_id,subject order by exam_date rows between unbounded preceding and unbounded following) as first_score,
        last_value(score) over(partition by student_id,subject order by exam_date rows between unbounded preceding and unbounded following) as latest_score ,
        count(*) over (partition by student_id,subject rows between unbounded preceding and unbounded following) as test_count
    FROM Scores
)

select
    student_id,
    subject,
    first_score,
    latest_score 
from student_summary
where test_count >= 2
    and first_score<latest_score 
order by student_id,subject