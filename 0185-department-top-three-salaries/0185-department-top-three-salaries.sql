# Write your MySQL query statement below
WITH salary_ranked AS
(
SELECT
    departmentId,
    salary,
    rank() over(partition by departmentId order by salary desc) as ranked
FROM (SELECT DISTINCT departmentId,salary from Employee) as a
)

SELECT 
    d.name as Department,
    Employee.name as Employee,
    Employee.salary as Salary
FROM salary_ranked 
    left join Employee USING (departmentId,salary)
    left join Department d on salary_ranked.departmentId = d.id
WHERE ranked <= 3