import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    BaggingClassifier,
    RandomForestClassifier,
    AdaBoostClassifier,
    VotingClassifier
)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# step 1 : load Dataset
# NOTE: change the filename below if your CSV has a different name
df = pd.read_csv("Fraudulent_Transaction_Detection.csv")

print("Dataset Loaded Successfully!!")
print("First Few Entries :")
print(df.head())

# step 2 : Preprocess data
print("Null Values in Dataset :")
print(df.isnull().sum())

# step 3 : separate the dependent and independent variables
X = df.drop("Fraud", axis=1)
Y = df["Fraud"]

# step 4 : split the dataset
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

# step 5 : define all models to compare
models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Bagging": BaggingClassifier(
        estimator=DecisionTreeClassifier(random_state=42),
        n_estimators=50,
        random_state=42
    ),
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ),
    "AdaBoost": AdaBoostClassifier(
        n_estimators=100,
        random_state=42
    ),
    "Voting": VotingClassifier(
        [
            ("lg", LogisticRegression(max_iter=1000)),
            ("dt", DecisionTreeClassifier(random_state=42)),
            ("rf", RandomForestClassifier(n_estimators=100, random_state=42))
        ],
        voting="soft"
    )
}

# step 6 : train, predict, evaluate each model
results = {}
conf_matrices = {}

for name, model in models.items():
    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)

    acc = accuracy_score(Y_test, Y_pred)
    prec = precision_score(Y_test, Y_pred, zero_division=0)
    rec = recall_score(Y_test, Y_pred, zero_division=0)
    f1 = f1_score(Y_test, Y_pred, zero_division=0)
    cm = confusion_matrix(Y_test, Y_pred)

    results[name] = {
        "Accuracy": acc * 100,
        "Precision": prec * 100,
        "Recall": rec * 100,
        "F1": f1 * 100
    }
    conf_matrices[name] = cm

# step 7 : print comparison table
results_df = pd.DataFrame(results).T
print("\nFinal Comparison Table :")
print(results_df.round(2))

# step 8 : plot grouped bar chart comparing metrics
metrics = ["Accuracy", "Precision", "Recall", "F1"]
model_names = list(models.keys())

x = np.arange(len(model_names))
width = 0.2

plt.figure(figsize=(12, 6))
for i, metric in enumerate(metrics):
    values = [results[name][metric] for name in model_names]
    plt.bar(x + i * width, values, width, label=metric)

plt.title("Model Comparison - Fraudulent Transaction Detection")
plt.xlabel("Model")
plt.ylabel("Score (%)")
plt.xticks(x + width * 1.5, model_names, rotation=15)
plt.ylim(0, 100)
plt.legend()
plt.tight_layout()
plt.savefig("fraud_model_comparison.png", dpi=150)
plt.show()

# step 9 : plot confusion matrices for all models in a grid
fig, axes = plt.subplots(2, 3, figsize=(15, 9))
axes = axes.flatten()

for ax, (name, cm) in zip(axes, conf_matrices.items()):
    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["Normal (0)", "Fraud (1)"]
    )
    disp.plot(ax=ax, colorbar=False, cmap="Blues")
    ax.set_title(name)

# hide any unused subplot
for ax in axes[len(conf_matrices):]:
    ax.axis("off")

plt.suptitle("Confusion Matrices for All Models")
plt.tight_layout()
plt.savefig("fraud_confusion_matrices.png", dpi=150)
plt.show()

# step 10 : recommend best model based on F1 score (good for imbalanced fraud data)
best_model = results_df["F1"].idxmax()
print(f"\nRecommended model based on F1 Score: {best_model}")
print(results_df.loc[best_model])