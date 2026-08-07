'''
write a python program to load the file student_performance_ml.csv using 
pandas :
    First 5 records
    last 5 records
    total number of rows and columns
    List of column names
    Data types of each column
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

print("First 5 entries from Dataset:")
print(df.head(5))

print("Last 5 entries from Dataset:")
print(df.tail(5))

print("Total number of rows and columns:")
print(df.shape)

print("List of column names:")
print(list(df.columns))

print("Data types of each column:")
print(df.dtypes)