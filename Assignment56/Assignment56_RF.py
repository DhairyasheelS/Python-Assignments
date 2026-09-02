import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from sklearn.preprocessing import StandardScaler

#step 1 : load Dataset
df = pd.read_csv("Fraudulent_Transaction_Detection.csv")

print("Dataset Loaded Successfully!!")

print("First Few Entries :")
print(df.head())

#step 2 : Preprocess data 

print("Null Values in Dataset :")
print(df.isnull().sum())

#step 3 : seprate the dependent and independent variables

X = df.drop("Fraud",axis=1)
Y = df["Fraud"]


# step 4 : split the dataset

X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
    )

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

# step 5 : Train the model
model = RandomForestClassifier(n_estimators=100)

model = model.fit(X_train_scaled,Y_train)

# step 6 : test the model
Y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(Y_test,Y_pred)

print("Accuracy of Model is  : ",accuracy*100)