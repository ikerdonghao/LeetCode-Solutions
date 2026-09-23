# Write your MySQL query statement below
WITH first_half_agg AS
(SELECT
    driver_id,
    AVG(distance_km/fuel_consumed) as first_half_avg
    FROM trips
    WHERE month(trip_date) <= 6
    GROUP BY 1
)

, second_half_agg AS
(SELECT
    driver_id,
    AVG(distance_km/fuel_consumed) as second_half_avg
    FROM trips
    WHERE month(trip_date) > 6
    GROUP BY 1
)

SELECT
    fa.driver_id,
    driver_name,
    round(first_half_avg,2) as first_half_avg,
    round(second_half_avg,2) as second_half_avg,
    round(second_half_avg-first_half_avg,2) as efficiency_improvement
FROM first_half_agg fa
    JOIN second_half_agg sa ON fa.driver_id = sa.driver_id
    LEFT JOIN drivers ON fa.driver_id = drivers.driver_id
WHERE second_half_avg > first_half_avg
ORDER BY efficiency_improvement DESC,driver_name