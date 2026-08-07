'''
write a program to:
    Analyze relationship of StudyHours & Attendance with FinalResult 
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

print("\n----- Average StudyHours grouped by FinalResult -----")
print(df.groupby('FinalResult')['StudyHours'].mean())

print("\n----- Average Attendance grouped by FinalResult -----")
print(df.groupby('FinalResult')['Attendance'].mean())

print("""
Observations :
1. Students who passed generally show higher average StudyHours than
   students who failed, indicating study time positively influences results.
2. Passed students also tend to have higher average Attendance percentage
   compared to failed students.
3. This suggests both StudyHours and Attendance are positively correlated
   with academic performance.
4. However, these are not the only factors - other variables like
   PreviousScore and AssignmentsCompleted may also play a role.
5. Correlation does not imply strict causation; some students may pass
   despite lower values due to other strengths.
""")
