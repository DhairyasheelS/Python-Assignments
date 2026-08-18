'''
Q6 : use df from Q1 and sort the dataframe by 'Total' marks in desending order
'''
import pandas as pd

def main():

    data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82]
    }

    df = pd.DataFrame(data)
    df["Total"] = df[['Math', 'Science','English']].sum(axis=1)

    print(df.sort_values(by="Total",ascending=False))

if __name__ == "__main__":
    main()