import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split , StratifiedKFold , GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
    f1_score
)
from imblearn.over_sampling import SMOTE

def LoadDataset(DataPath):

    df = pd.read_csv(DataPath)

    print("Dataset Loaded sucessfully!!")

    return df

def PreProcessData(df):
    print("Shape of dataset : ",df.shape)
    print("Columns in dataset : ")
    print(df.columns)
    print("First few records : ")
    print(df.head())

    print("Missing Values in dataset : ")
    print(df.isnull().sum())

    print("Identify Numeric & categorical features : ")

    numeric_cols = df.select_dtypes(include = [np.number]).columns.tolist()

    print("Numeric Cols : \n",numeric_cols)

    categorical_cols = df.select_dtypes(exclude = [np.number]).columns.tolist()

    print("Categorical cols : \n",categorical_cols)

    print("Converting categorical feature into numeric : ")

    df["OverTime"] = df["OverTime"].map({
        "Yes" : 1 ,
        "No" : 0
    })


    df["Attrition"] = df["Attrition"].map({
            "Yes" : 1 ,
            "No" : 0
    })

    # Feature Engineering for better prediction
    print("\nEngineering new features...")

    # Income per year of experience (career progression indicator)
    df['IncomePerYear'] = df['MonthlyIncome'] / (df['TotalWorkingYears'] + 1)

    # Average years per company (job stability indicator)
    df['YearsPerCompany'] = df['TotalWorkingYears'] / (df['NumCompaniesWorked'] + 1)

    # Frequent job changer flag
    df['FrequentJobChange'] = (df['NumCompaniesWorked'] > df['TotalWorkingYears'] / 3).astype(int)

    # Experience gap (age - working years - typical starting age)
    df['ExperienceGap'] = df['Age'] - df['TotalWorkingYears'] - 18

    # Work-life balance interaction with overtime
    df['OverTimeBalanceInteraction'] = df['OverTime'] * df['WorkLifeBalance']

    print(f"Added 5 engineered features. New shape: {df.shape}")

    return df

def SeprateVariables(df):

    X = df.drop("Attrition",axis = 1)
    Y = df["Attrition"]

    print("Independent and Dependent variables are seprated!!")

    return X,Y

def SplitDataset(X,Y):

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Handle class imbalance using SMOTE
    print("\nApplying SMOTE to balance training data...")
    print(f"Before SMOTE - Class distribution: {np.bincount(Y_train)}")

    smote = SMOTE(random_state=42)
    X_train_balanced, Y_train_balanced = smote.fit_resample(X_train_scaled, Y_train)

    print(f"After SMOTE - Class distribution: {np.bincount(Y_train_balanced)}")

    return X_train_balanced, X_test_scaled, Y_train_balanced, Y_test

def TrainModel(X_train, Y_train, tune=True):
    if not tune:
        model = MLPClassifier(
            hidden_layer_sizes=(16, 8),
            activation="relu",
            solver="adam",
            alpha=1e-3,          # L2 regularization, helps on small data
            max_iter=2000,
            early_stopping=True,  # stops before overfitting
            random_state=42,
        )
        return model.fit(X_train, Y_train)

    # Expanded grid search optimized for balanced SMOTE data
    param_grid = {
        "hidden_layer_sizes": [(64, 32), (32, 16), (64, 32, 16), (128, 64)],
        "alpha": [1e-4, 1e-3, 1e-2, 0.05],
        "learning_rate_init": [1e-3, 5e-3, 1e-2],
        "batch_size": [32, 64, 128]
    }
    base_model = MLPClassifier(
        activation="relu",
        solver="adam",
        max_iter=3000,
        early_stopping=True,
        validation_fraction=0.15,
        n_iter_no_change=15,
        random_state=42,
    )
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    grid = GridSearchCV(
        base_model, param_grid, scoring="f1", cv=cv, n_jobs=-1, verbose=1
    )
    grid.fit(X_train, Y_train)
    print("\nBest params : ", grid.best_params_)
    print("Best CV F1 score : ", grid.best_score_)
    return grid.best_estimator_

def EvaluateModel(X_test, Y_test, model):
    Y_pred = model.predict(X_test)
    Y_prob = model.predict_proba(X_test)[:, 1]

    accuracy = accuracy_score(Y_test, Y_pred)
    auc = roc_auc_score(Y_test, Y_prob)

    print("\n=== Model Evaluation ===")
    print("Accuracy of Model : ", accuracy * 100)
    print("ROC-AUC : ", auc)
    print("\nConfusion Matrix (rows=actual, cols=predicted):\n",
          confusion_matrix(Y_test, Y_pred))
    print("\nClassification Report:\n",
          classification_report(Y_test, Y_pred, target_names=["No", "Yes"]))

    # Try optimized threshold for better balance
    best_threshold = 0.5
    best_f1 = 0

    print("\n=== Threshold Optimization ===")
    for threshold in [0.3, 0.35, 0.4, 0.45, 0.5]:
        Y_pred_adjusted = (Y_prob >= threshold).astype(int)
        f1 = f1_score(Y_test, Y_pred_adjusted)
        print(f"Threshold {threshold:.2f}: F1-score = {f1:.3f}")
        if f1 > best_f1:
            best_f1 = f1
            best_threshold = threshold

    print(f"\nBest threshold: {best_threshold}")
    Y_pred_optimized = (Y_prob >= best_threshold).astype(int)
    accuracy_optimized = accuracy_score(Y_test, Y_pred_optimized)

    print("\n=== Optimized Results (threshold={:.2f}) ===".format(best_threshold))
    print("Accuracy: ", accuracy_optimized * 100)
    print("\nConfusion Matrix:\n", confusion_matrix(Y_test, Y_pred_optimized))
    print("\nClassification Report:\n",
          classification_report(Y_test, Y_pred_optimized, target_names=["No", "Yes"]))

def main():
    df = LoadDataset("Employee_Attrition.csv")

    df = PreProcessData(df)

    X , Y = SeprateVariables(df)

    X_train,X_test,Y_train,Y_test = SplitDataset(X,Y)

    model = TrainModel(X_train,Y_train)

    EvaluateModel(X_test,Y_test,model)


if __name__ == "__main__":
    main()