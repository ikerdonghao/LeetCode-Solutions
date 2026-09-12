# Write your MySQL query statement below
WITH ranked_salary AS
(
    SELECT
        id,
        salary,
        dense_rank() over(order by salary desc) as ranked
    from Employee
)

select
    CASE WHEN (SELECT COUNT(DISTINCT salary) FROM Employee) = 1 THEN NULL
        ELSE (SELECT distinct salary FROM ranked_salary where ranked = 2)  END as SecondHighestSalary 