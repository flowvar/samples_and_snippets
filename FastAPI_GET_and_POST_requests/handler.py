import pandas as pd


# sum up values
def sum_up(df: pd.DataFrame):
    # calculate sum of first row
    sum_first_row = df.sum(axis=1)[0]
    return str(sum_first_row)


