# Write your MySQL query statement below
WITH session_summary AS
(
    SELECT
        book_id,
        count(session_id) as session_count,
        min(session_rating) as min_rating,
        max(session_rating) as max_rating,
        max(session_rating) - min(session_rating) as rating_spread,
        sum(case when session_rating <= 2 or session_rating >= 4 then 1 else 0 end)/count(session_id) as polarization_score
    FROM reading_sessions
    group by 1
)

select
    book_id,
    title,
    author,
    genre,
    pages,
    rating_spread,
    round(polarization_score,2) as polarization_score
from books
    left join session_summary using (book_id)
where polarization_score>=0.6
    and session_count>=5
    and min_rating <= 2 and max_rating >= 4
order by polarization_score desc,title desc