import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    pivot_table = pd.pivot(department,index="id",columns="month",values="revenue")
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    pivot_table = pivot_table.reindex(columns=months)
    pivot_table.columns = [f"{m}_Revenue" for m in pivot_table.columns]
    return pivot_table.reset_index()