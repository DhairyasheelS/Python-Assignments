'''
write a program to:
   Histogram of StudyHours 
'''
import pandas as pd
import matplotlib.pyplot as plt

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
# Q6. Histogram of StudyHours
# ============================================================
plt.figure(figsize=(8, 5))
plt.hist(df['StudyHours'], bins=10, color='skyblue', edgecolor='black')
plt.title("Distribution of StudyHours")
plt.xlabel("StudyHours")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram_studyhours.png")
plt.show()

# Explanation:
# The histogram shows how study hours are spread across students.
# If it is roughly bell-shaped, most students study a moderate number
# of hours, with fewer students studying very little or very much
# (a normal-like distribution). If skewed, it indicates most students
# cluster around low or high study hours.
