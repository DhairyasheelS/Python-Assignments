import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score

# step 1 : load Dataset
df = pd.read_csv("Customer_Loan_Approval.csv")

print("Dataset Loaded Successfully!!")
print("First Few Entries :")
print(df.head())

# step 2 : Preprocess data
print("Null Values in Dataset :")
print(df.isnull().sum())

# step 3 : separate the dependent and independent variables
X = df.drop("LoanApproved", axis=1)
Y = df["LoanApproved"]

# step 4 : split the dataset
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

# step 5 : define base models
model_lg = LogisticRegression(max_iter=1000)
model_dt = DecisionTreeClassifier(random_state=42)
model_knn = KNeighborsClassifier(n_neighbors=5)

# step 6 : train and evaluate individual models
model_lg.fit(X_train, Y_train)
acc_lg = accuracy_score(Y_test, model_lg.predict(X_test))

model_dt.fit(X_train, Y_train)
acc_dt = accuracy_score(Y_test, model_dt.predict(X_test))

model_knn.fit(X_train, Y_train)
acc_knn = accuracy_score(Y_test, model_knn.predict(X_test))

# step 7 : Hard Voting Classifier
hard_voting = VotingClassifier(
    [
        ("lg", LogisticRegression(max_iter=1000)),
        ("dt", DecisionTreeClassifier(random_state=42)),
        ("knn", KNeighborsClassifier(n_neighbors=5))
    ],
    voting="hard"
)
hard_voting.fit(X_train, Y_train)
acc_hard = accuracy_score(Y_test, hard_voting.predict(X_test))

# step 8 : Soft Voting Classifier
soft_voting = VotingClassifier(
    [
        ("lg", LogisticRegression(max_iter=1000)),
        ("dt", DecisionTreeClassifier(random_state=42)),
        ("knn", KNeighborsClassifier(n_neighbors=5))
    ],
    voting="soft"
)
soft_voting.fit(X_train, Y_train)
acc_soft = accuracy_score(Y_test, soft_voting.predict(X_test))

# step 9 : collect results
results = {
    "Logistic Regression": acc_lg * 100,
    "Decision Tree": acc_dt * 100,
    "KNN": acc_knn * 100,
    "Hard Voting": acc_hard * 100,
    "Soft Voting": acc_soft * 100
}

print("\nAccuracy Comparison Table :")
for model_name, acc in results.items():
    print(f"{model_name:20s} : {acc:.2f}%")

# step 10 : plot comparison using matplotlib
plt.figure(figsize=(8,6))
bars = plt.bar(results.keys(), results.values(), color=[
    "#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B2"
])

plt.title("Accuracy Comparison of Models - Customer Loan Approval")
plt.xlabel("Model")
plt.ylabel("Accuracy (%)")
plt.ylim(0, 100)
plt.xticks(rotation=15)

# annotate bars with accuracy values
for bar, acc in zip(bars, results.values()):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 1,
        f"{acc:.2f}%",
        ha="center",
        fontsize=9
    )

plt.tight_layout()
plt.savefig("accuracy_comparison.png", dpi=150)
plt.show()