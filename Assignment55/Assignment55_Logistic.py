import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#step 1 : load Dataset
df = pd.read_csv("Customer_Loan_Approval.csv")

print("Dataset Loaded Successfully!!")

print("First Few Entries :")
print(df.head())

#step 2 : Preprocess data 

print("Null Values in Dataset :")
print(df.isnull().sum())

#step 3 : seprate the dependent and independent variables

X = df.drop("LoanApproved",axis=1)
Y = df["LoanApproved"]


# step 4 : split the dataset

X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
    )

# step 5 : Train the model
model = LogisticRegression(max_iter=1000)

model = model.fit(X_train,Y_train)

# step 6 : test the model
Y_pred = model.predict(X_test)

accuracy = accuracy_score(Y_test,Y_pred)

print("Accuracy of Model is  : ",accuracy*100)