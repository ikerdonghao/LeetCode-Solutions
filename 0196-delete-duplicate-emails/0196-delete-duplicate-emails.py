import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # if len(person) < 1:
        # return person
    # else:
    person.sort_values(by="id",inplace=True)
    person.drop_duplicates(subset=["email"],inplace=True)