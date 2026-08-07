'''
write a program to:
   Histogram of StudyHours 
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# ============================================================
# Q9. AssignmentsCompleted vs FinalResult
# ============================================================
plt.figure(figsize=(8, 5))
sns.boxplot(x='FinalResult', y='AssignmentsCompleted', data=df, palette='Set2')
plt.title("AssignmentsCompleted vs FinalResult")
plt.xlabel("FinalResult (0=Fail, 1=Pass)")
plt.ylabel("AssignmentsCompleted")
plt.tight_layout()
plt.savefig("assignments_vs_result.png")
plt.show()

print("\n----- Average AssignmentsCompleted by FinalResult -----")
print(df.groupby('FinalResult')['AssignmentsCompleted'].mean())

# Observation:
# Students who completed more assignments tend to have a higher chance
# of passing, showing a positive relationship between assignment
# completion and academic outcome.