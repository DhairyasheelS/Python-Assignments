"""
Marvellous Infosystems - Python Assignment 50
Breast Cancer Prediction using KNN Classifier
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
)


def LoadDataset():
    # Step 1: Load dataset using sklearn's built-in loader 
    data = load_breast_cancer()

    df = pd.DataFrame(data.data, columns=data.feature_names)
    df["target"] = data.target  # 0 = Malignant, 1 = Benign

    print("Dataset loaded successfully!!")
    print(df.head(10))

    return df


def ExploreData(df):
    print("\nMissing Values in dataset:")
    print(df.isnull().sum().sum(), "missing values found")

    print("\nSummary statistics:")
    print(df.describe())

    # Visualize correlations 
    plt.figure(figsize=(14, 10))
    sns.heatmap(df.corr(), cmap="coolwarm", annot=False)
    plt.title("Feature Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("correlation_heatmap.png")
    plt.close()
    print("\nCorrelation heatmap saved as 'correlation_heatmap.png'")


def SplitDataset(df):
    X = df.drop(columns=["target"])
    Y = df["target"]

    # Split BEFORE scaling to avoid data leakage
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42, stratify=Y
    )

    return X_train, X_test, Y_train, Y_test


def ScaleFeatures(X_train, X_test):
    scaler = StandardScaler()

    # Fit ONLY on training data, then transform both
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled


def BuildModel(X_train, Y_train):
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train, Y_train)
    return model


def EvaluateModel(model, X_test, Y_test):
    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_pred)
    precision = precision_score(Y_test, Y_pred)
    recall = recall_score(Y_test, Y_pred)
    f1 = f1_score(Y_test, Y_pred)
    cm = confusion_matrix(Y_test, Y_pred)

    print("\n--- Model Evaluation ---")
    print(f"Accuracy  : {accuracy * 100:.2f}%")
    print(f"Precision : {precision:.4f}")
    print(f"Recall    : {recall:.4f}")
    print(f"F1-Score  : {f1:.4f}")

    print("\nConfusion Matrix:")
    print(cm)

    print("\nClassification Report:")
    print(classification_report(Y_test, Y_pred, target_names=["Malignant", "Benign"]))

    # Plot confusion matrix
    plt.figure(figsize=(6, 5))
    sns.heatmap(
        cm, annot=True, fmt="d", cmap="Blues",
        xticklabels=["Malignant", "Benign"],
        yticklabels=["Malignant", "Benign"],
    )
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.tight_layout()
    plt.savefig("confusion_matrix.png")
    plt.close()
    print("Confusion matrix plot saved as 'confusion_matrix.png'")

    return accuracy, precision, recall, f1


def PrintObservations(accuracy, precision, recall, f1):
    print("\n--- Observations & Conclusions ---")
    print(f"The KNN classifier (k=5) achieved an accuracy of {accuracy * 100:.2f}% "
          f"on the test set.")
    print(f"Precision of {precision:.4f} indicates the proportion of predicted "
          f"'Benign' cases that were actually benign.")
    print(f"Recall of {recall:.4f} indicates how many actual 'Benign' cases were "
          f"correctly identified.")
    print(f"F1-Score of {f1:.4f} balances precision and recall, showing the model "
          f"performs reliably on this dataset.")
    print("Feature scaling and correct train/test separation (no data leakage) "
          "were critical to getting a trustworthy evaluation.")


def main():
    # Step 1: Load
    df = LoadDataset()

    # Step 2: EDA
    ExploreData(df)

    # Step 3: Split (before scaling)
    X_train, X_test, Y_train, Y_test = SplitDataset(df)

    # Step 4: Scale (fit on train only)
    X_train_scaled, X_test_scaled = ScaleFeatures(X_train, X_test)

    # Step 5: Build model
    model = BuildModel(X_train_scaled, Y_train)

    # Step 6: Evaluate
    accuracy, precision, recall, f1 = EvaluateModel(model, X_test_scaled, Y_test)

    # Step 7: Observations
    PrintObservations(accuracy, precision, recall, f1)


if __name__ == "__main__":
    main()