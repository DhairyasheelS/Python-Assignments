'''
Q6 : use df from Q1 and sort the dataframe by 'Total' marks in desending order
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():

    data2 = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [np.nan, 76, 88],
        'Science': [91, np.nan, 85]
    }

    df2 = pd.DataFrame(data2)

    numeric_cols = ['Math', 'Science']
    df2[numeric_cols] = df2[numeric_cols].fillna(df2[numeric_cols].mean())

    print(df2)

if __name__ == "__main__":
    main()