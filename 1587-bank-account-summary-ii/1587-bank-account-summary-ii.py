import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    user_summary = transactions.groupby("account").agg(balance=("amount","sum"))
    # print(user_summary.head())
    filtered_user = user_summary[user_summary["balance"]>10000]
    output = pd.merge(filtered_user,users,on="account",how="left")
    return output[["name","balance"]]