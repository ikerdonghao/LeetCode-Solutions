import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    full_table = pd.merge(person,address,on="personId",how="left")
    return full_table[["firstName","lastName","city","state"]]