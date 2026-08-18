'''
Q1 : Create DataFrame for students marks and print
basic information like shape , colunms , and data types
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

    print("Shape of Dataset : ")
    print(df.shape)
    print("Colunms of Dataset :")
    print(df.columns)
    print("Datatype of dataset")
    print(df.dtypes)

if __name__ == "__main__":
    main()