'''
Q6 : use df from Q1 and sort the dataframe by 'Total' marks in desending order
'''
import pandas as pd
import matplotlib.pyplot as plt

def main():

    data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82]
    }

    df = pd.DataFrame(data)
    df["Total"] = df[['Math', 'Science','English']].sum(axis=1)

    #Visulisation

    plt.bar(
        x=df["Name"],
        height=df["Total"],
        color="skyblue"
    )

    plt.title("Student Names vs Total Marks")
    plt.xlabel("Students")
    plt.ylabel("Total Marks")

    plt.show()

if __name__ == "__main__":
    main()