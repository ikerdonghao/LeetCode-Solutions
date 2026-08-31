import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee["rank"] = employee["salary"].rank(method = "dense",ascending=False)
    if N > max(employee["rank"])  or N <= 0:
        return pd.DataFrame({"getNthHighestSalary({0})".format(N): [None]})
    return employee[employee["rank"] == N][["salary"]].rename(columns={"salary":"getNthHighestSalary({0})".format(N)}).drop_duplicates()