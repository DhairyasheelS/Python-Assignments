'''
write a program to:
    Display total number of students in the dataset
    Count how many students Passed(Final Result = 1)
    Count how many students Failed(Final Result = 0)
'''
import pandas as pd

Border = "-"*50
############################################
# Step 1 : Load the Dataset
############################################
print(Border)
print("Step 1 : Load the Dataset")
print(Border)

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)
print("Dataset loaded Successfully!!")

############################################
# Step 2 : Data Analysis(EDA)
############################################
print(Border)
print("Step 2 : Data Analysis (EDA)")
print(Border)

print("Display total number of students in the dataset:")
print(len(df))

print("Count how many students Passed(Final Result = 1)")
print((df["FinalResult"] == 1).sum())

print("Count how many students Failed(Final Result = 0)")
print((df["FinalResult"] == 0).sum())