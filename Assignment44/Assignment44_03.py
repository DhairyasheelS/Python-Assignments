'''
Q3 : use df from Q1 and add new colunm total and add sum of all sub marks
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

    print(df)

if __name__ == "__main__":
    main()