from sklearn.preprocessing import OneHotEncoder
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

    sagar_data = df[df["Name"] == "Sagar"].iloc[0]

    subjects = ["Math","Science","English"]

    marks = [sagar_data["Math"],sagar_data["Science"],sagar_data["English"]]

    #pie

    plt.figure(figsize=(8,8))
    plt.pie(
        marks,
        labels=subjects,
        autopct="%1.1f%%",
        startangle=140,
        colors=['#ff9999', '#66b3ff', '#99ff99']
    ) 
    plt.title("Sagar's subject marks breakdown")
    plt.show()   
    

if __name__ == "__main__":
    main()