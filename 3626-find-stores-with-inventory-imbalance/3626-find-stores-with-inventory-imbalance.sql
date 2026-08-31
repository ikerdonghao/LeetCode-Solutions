# Write your MySQL query statement below
WITH store_summary as
(SELECT
    DISTINCT
    store_id,

    first_value(product_name) over(partition by store_id order by price desc rows between unbounded preceding and unbounded following) as most_exp_product ,
    -- first_value(quantity) over(partition by store_id order by price desc rows between unbounded preceding and unbounded following) as expensive_product_inventory,

    first_value(product_name) over(partition by store_id order by price asc rows between unbounded preceding and unbounded following) as cheapest_product,
    -- last_value(quantity) over(partition by store_id order by price rows between unbounded preceding and unbounded following) as cheapest_product_inventory,

    first_value(quantity) over(partition by store_id order by price asc rows between unbounded preceding and unbounded following) / first_value(quantity) over(partition by store_id order by price desc rows between unbounded preceding and unbounded following) as imbalance_ratio,

    count(product_name) over(partition by store_id) as product_count
FROM inventory
order by store_id)

select
    store_id,
    store_name,
    location,
    most_exp_product,
    cheapest_product,
    round(imbalance_ratio,2) AS imbalance_ratio
from store_summary
    left join stores using (store_id) 
WHERE product_count >= 3
    AND imbalance_ratio > 1
ORDER BY imbalance_ratio DESC,store_name