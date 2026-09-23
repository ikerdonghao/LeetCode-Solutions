# Write your MySQL query statement below
WITH email_count_table AS
(SELECT
    email,
    count(*) as email_count
    FROM Person
    GROUP BY 1)

SELECT
    email
from email_count_table
where email_count > 1