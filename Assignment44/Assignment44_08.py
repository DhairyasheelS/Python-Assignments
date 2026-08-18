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

    amit_data = df[df['Name'] == 'Amit']

    subjects = ['Math', 'Science', 'English']
    scores = [amit_data['Math'].values[0], amit_data['Science'].values[0], amit_data['English'].values[0]]

    plt.plot(subjects, scores, marker='o', color='purple', linewidth=2)
    plt.title("Amit's Marks Across Subjects")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()