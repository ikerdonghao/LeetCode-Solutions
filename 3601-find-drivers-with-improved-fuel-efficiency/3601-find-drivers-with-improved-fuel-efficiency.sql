# Write your MySQL query statement below
WITH summary as
(
    SELECT
        driver_id,
        AVG(CASE WHEN MONTH(trip_date) <= 6 then distance_km / fuel_consumed end) as first_half_avg,
        AVG(CASE WHEN MONTH(trip_date) > 6 then distance_km / fuel_consumed end) as second_half_avg
    FROM trips
    GROUP BY driver_id
)

SELECT 
    s.driver_id,
    driver_name,
    round(first_half_avg,2) as first_half_avg,
    round(second_half_avg,2) as second_half_avg,
    round(second_half_avg - first_half_avg,2) as efficiency_improvement 
FROM summary s
    LEFT JOIN drivers d ON s.driver_id = d.driver_id
WHERE first_half_avg is not null and second_half_avg is not null
    and second_half_avg > first_half_avg
ORDER BY efficiency_improvement DESC, driver_name