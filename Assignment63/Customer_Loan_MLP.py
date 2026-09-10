"""
Marvellous Infosystems : Python - Automation & Machine Learning
Deep Learning Assignment - Loan Default Prediction using MLPClassifier
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score,
)
from imblearn.over_sampling import SMOTE

# --------------------------------------
# step 1 : load the dataset
# --------------------------------------
df = pd.read_csv("Loan_Default.csv")

print("Dataset loaded successfully!!")
print("First few records")
print(df.head())

# --------------------------------------
# step 2 : Perform exploratory analysis (EDA)
# --------------------------------------
print("\nShape of Dataset :")
print(df.shape)

print("\nInfo :")
print(df.info())

print("\nStatistical summary :")
print(df.describe())

# --------------------------------------
# step 3 : Find missing values
# --------------------------------------
print("\nMissing values in dataset :")
print(df.isnull().sum())

# Simple handling: drop rows with missing target, fill numeric NaNs with median,
# categorical NaNs with mode. Adjust to your actual dataset if needed.
df = df.dropna(subset=["Default"])
for col in df.columns:
    if df[col].dtype in [np.float64, np.int64]:
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

# --------------------------------------
# step 4 : Check whether the target classes are balanced
# --------------------------------------
print("\nTarget class distribution (before balancing) :")
counts = df["Default"].value_counts()
print(counts)
print("Class ratio:", counts / counts.sum())

# --------------------------------------
# step 5 : Encode categorical variables
# --------------------------------------
categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()
if "Default" in categorical_cols:
    categorical_cols.remove("Default")

print("\nCategorical columns found:", categorical_cols)

label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    label_encoders[col] = le

# --------------------------------------
# step 6 : Separate X and y
# --------------------------------------
X = df.drop("Default", axis=1)
y = df["Default"]

# --------------------------------------
# step 7 : Split the dataset into training and testing data
# --------------------------------------
# --------------------------------------
# step 8 : Should stratified splitting be used?
# --------------------------------------
# Yes - stratify=y is used because the target classes are imbalanced
# (far more non-defaulters than defaulters, typically). Stratified splitting
# preserves the same class ratio in both train and test sets, so the model
# is evaluated on a test set that reflects the real-world class distribution
# rather than one that happens to be skewed by random chance.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("\nTrain shape:", X_train.shape, " Test shape:", X_test.shape)

# Balance ONLY the training data with SMOTE (never touch the test set,
# otherwise synthetic samples leak information into evaluation).
print("\nClass distribution in y_train before SMOTE:")
print(y_train.value_counts())

smote = SMOTE(random_state=42)
X_train, y_train = smote.fit_resample(X_train, y_train)

print("\nClass distribution in y_train after SMOTE:")
print(y_train.value_counts())

# --------------------------------------
# step 9 : Scale the features
# --------------------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# --------------------------------------
# step 10 : Create an MLPClassifier
# --------------------------------------
mlp = MLPClassifier(
    hidden_layer_sizes=(32, 16),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42,
)

# --------------------------------------
# step 11 : Train the model
# --------------------------------------
mlp.fit(X_train_scaled, y_train)

# --------------------------------------
# step 12 : Calculate accuracy
# --------------------------------------
y_pred = mlp.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy :", accuracy)

# --------------------------------------
# step 13 : Generate the confusion matrix
# --------------------------------------
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix :")
print(cm)

# --------------------------------------
# step 14 : Generate the classification report
# --------------------------------------
print("\nClassification Report :")
print(classification_report(y_test, y_pred))

# --------------------------------------
# step 15 : Calculate precision, recall and F1-score
# --------------------------------------
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
print(f"\nPrecision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1-score  : {f1:.4f}")

# --------------------------------------
# step 16 : Plot training loss
# --------------------------------------
plt.figure(figsize=(8, 5))
plt.plot(mlp.loss_curve_)
plt.title("Training Loss Curve - MLPClassifier")
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.grid(True)
plt.savefig("training_loss_curve.png")
plt.show()

# --------------------------------------
# step 17 : Test the model on new loan applicants
# --------------------------------------
# Replace these sample values with real new-applicant records.
# Column order MUST match X.columns exactly.
new_applicants = pd.DataFrame(
    [X.iloc[0].to_dict(), X.iloc[1].to_dict()]  # placeholder examples
)
new_applicants_scaled = scaler.transform(new_applicants)
new_predictions = mlp.predict(new_applicants_scaled)
new_probabilities = mlp.predict_proba(new_applicants_scaled)

print("\nPredictions on new applicants (0 = Low risk, 1 = High risk):")
for i, (pred, prob) in enumerate(zip(new_predictions, new_probabilities)):
    print(f"Applicant {i+1}: Prediction = {pred}, Probability = {prob}")


# =====================================================================
# HYPERPARAMETER EXPERIMENTS
# Change ONE parameter at a time, keep everything else fixed.
# =====================================================================

def run_experiment(label, **mlp_kwargs):
    """Train an MLPClassifier with given kwargs and report accuracy/F1."""
    model = MLPClassifier(random_state=42, max_iter=1000, **mlp_kwargs)
    model.fit(X_train_scaled, y_train)
    preds = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, preds)
    f1_ = f1_score(y_test, preds)
    print(f"{label:35s} | Accuracy: {acc:.4f} | F1: {f1_:.4f}")
    return model


print("\n--- Experiment 1: Activation Function ---")
for act in ["identity", "logistic", "tanh", "relu"]:
    run_experiment(f"activation={act}", hidden_layer_sizes=(32, 16), activation=act, solver="adam")

print("\n--- Experiment 2: Hidden Layer Sizes ---")
for layers in [(10,), (20, 10), (50, 25), (100, 50, 25)]:
    run_experiment(f"hidden_layer_sizes={layers}", hidden_layer_sizes=layers, activation="relu", solver="adam")

print("\n--- Experiment 3: Learning Rate Init ---")
for lr in [0.0001, 0.001, 0.01, 0.1]:
    run_experiment(f"learning_rate_init={lr}", hidden_layer_sizes=(32, 16), activation="relu",
                   solver="adam", learning_rate_init=lr)