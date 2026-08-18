'''
Q2 : use df from Q1 and print descriptive statastics
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

    print("Statistics of Dataset :")
    print(df.describe())

if __name__ == "__main__":
    main()