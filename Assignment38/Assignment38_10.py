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
# Q10. SleepHours vs FinalResult
# ============================================================
plt.figure(figsize=(8, 5))
sns.boxplot(x='FinalResult', y='SleepHours', data=df, palette='Set3')
plt.title("SleepHours vs FinalResult")
plt.xlabel("FinalResult (0=Fail, 1=Pass)")
plt.ylabel("SleepHours")
plt.tight_layout()
plt.savefig("sleephours_vs_result.png")
plt.show()

print("\n----- Average SleepHours by FinalResult -----")
print(df.groupby('FinalResult')['SleepHours'].mean())

# Explanation:
# Sleeping more does NOT guarantee success. While adequate sleep supports
# concentration and health, the plot usually shows overlapping ranges of
# SleepHours for both Pass and Fail students. This means sleep alone is
# not a decisive factor - it must be combined with sufficient StudyHours,
# Attendance, and Assignment completion to influence FinalResult.