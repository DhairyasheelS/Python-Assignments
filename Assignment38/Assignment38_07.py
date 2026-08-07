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
# Q7. Scatter plot: StudyHours vs PreviousScore (colored by Pass/Fail)
# ============================================================
colors = df['FinalResult'].map({1: 'green', 0: 'red'})

plt.figure(figsize=(8, 5))
plt.scatter(df['StudyHours'], df['PreviousScore'], c=colors, alpha=0.7)
plt.title("StudyHours vs PreviousScore (Green=Pass, Red=Fail)")
plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")
plt.tight_layout()
plt.savefig("scatter_studyhours_previousscore.png")
plt.show()