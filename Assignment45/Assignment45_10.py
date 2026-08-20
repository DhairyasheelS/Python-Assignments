import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():

    data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82]
    }

    df = pd.DataFrame(data)

    df["Total"] = df[["Math","Science","English"]].sum(axis=1)

    df["Status"] = np.where(df['Total'] >= 250,"pass" , "fail")

    plt.figure(figsize=(5, 5))
    plt.boxplot(
        df['English'], 
        patch_artist=True, 
        boxprops=dict(facecolor='lightblue')
    )

    
    plt.ylabel('Marks')
    plt.xticks([1], ['English']) # Label the x-axis index cleanly
    plt.title('Q10: Distribution of English Marks')

    plt.show()
    
if __name__ == "__main__":
    main()