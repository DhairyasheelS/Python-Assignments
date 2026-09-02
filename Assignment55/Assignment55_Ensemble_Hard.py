import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

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
model_lg = LogisticRegression(max_iter=1000)
model_knn = KNeighborsClassifier(n_neighbors=5)
model_dt = DecisionTreeClassifier(random_state=42)


model = VotingClassifier(
    [
     ("lg",model_lg),
     ("knn",model_knn),
     ("dt",model_dt)   
    ],
    voting="hard"
)

model = model.fit(X_train,Y_train)

# step 6 : test the model
Y_pred = model.predict(X_test)

accuracy = accuracy_score(Y_test,Y_pred)

print("Accuracy of Model is  : ",accuracy*100)