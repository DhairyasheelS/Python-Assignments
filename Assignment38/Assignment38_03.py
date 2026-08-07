'''
write a program to:
    Average StudyHours
    Average Attendence
    Maximum PreviousScore
    Minimum SleepHours
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

print("Average StudyHours:")
print(df["StudyHours"].mean())

print("Average Attendance:")
print(df["Attendance"].mean())

print("Average PreviousScore:")
print(df["PreviousScore"].mean())

print("Average PreviousScore:")
print(df["PreviousScore"].mean())

print("Average SleepHours:")
print(df["SleepHours"].mean())