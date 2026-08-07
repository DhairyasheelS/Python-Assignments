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
# Q8. Boxplot for Attendance + Outlier check
# ============================================================
plt.figure(figsize=(6, 5))
sns.boxplot(y=df['Attendance'], color='lightblue')
plt.title("Boxplot of Attendance")
plt.tight_layout()
plt.savefig("boxplot_attendance.png")
plt.show()

# Outlier detection using IQR method
Q1 = df['Attendance'].quantile(0.25)
Q3 = df['Attendance'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['Attendance'] < lower_bound) | (df['Attendance'] > upper_bound)]
print("\n----- Attendance Outliers -----")
print(outliers)
print(f"\nNumber of outliers detected: {len(outliers)}")