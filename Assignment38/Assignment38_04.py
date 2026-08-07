'''
write a program to:
    Use value_counts() to analyze the distribution of FinalResult. 
    Calculate the percentage of pass and fail students.
    is the dataset balanced 
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

print("\n----- FinalResult value counts -----")
counts = df['FinalResult'].value_counts()
print(counts)

print("\n----- Percentage distribution -----")
percentages = df['FinalResult'].value_counts(normalize=True) * 100
print(percentages)

pass_pct = percentages.get(1, 0)
fail_pct = percentages.get(0, 0)

print(f"\nPass %: {pass_pct:.2f}%")
print(f"Fail %: {fail_pct:.2f}%")

if abs(pass_pct - fail_pct) <= 10:
    print("Observation: The dataset is fairly BALANCED "
          "(Pass and Fail percentages are close to each other).")
else:
    print("Observation: The dataset is IMBALANCED "
          "(one class dominates the other significantly).")