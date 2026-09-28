import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery_labeled = delivery.copy()
    delivery_labeled["preference"] = "scheduled"
    delivery_labeled.loc[delivery_labeled["order_date"] == delivery_labeled["customer_pref_delivery_date"],"preference"] = "immediate"
    # print(delivery_labeled.head())

    min_order_date = delivery_labeled.groupby('customer_id')['order_date'].idxmin()
    first_order_table = delivery_labeled.loc[min_order_date]
    first_order_count = first_order_table[first_order_table["preference"] == "immediate"].shape[0]
    rate = 100.0*first_order_count / first_order_table.shape[0]
    print(rate)
    output = pd.DataFrame({"immediate_percentage":[round(rate,2)]})
    return output 