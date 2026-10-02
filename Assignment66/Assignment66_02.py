"""
Marvellous Infosystems : Python - Automation & Machine Learning
Deep Learning Assignment - Q2: Predict loan approval

"""

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

np.random.seed(42)
tf.random.set_seed(42)

# Dataset
# Feature meaning: [Income, Credit Score, Loan Amount, Existing EMI, Employment Status]
# Employment Status: 0 = Not Stable, 1 = Stable
X = [
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000, 8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 10000, 1],
    [35000, 650, 250000, 9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1],
]
# Output meaning: 0 = Loan rejected, 1 = Loan approved
y = [0, 1, 1, 0, 1, 1, 0, 1, 0, 1]

columns = ["Income", "CreditScore", "LoanAmount", "ExistingEMI", "EmploymentStatus"]
df = pd.DataFrame(X, columns=columns)
df["LoanApproved"] = y

# 1. Preprocess categorical values
# Employment status is already encoded (0/1). If it were text, we would do:
# df["EmploymentStatus"] = df["EmploymentStatus"].map({"Not Stable": 0, "Stable": 1})
df = df.drop_duplicates().dropna()

X = df.drop(columns=["LoanApproved"]).values
y = df["LoanApproved"].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 2. Apply scaling (fit on train only)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 3. Train FNN model
model = Sequential([
    Input(shape=(X_train.shape[1],)),
    Dense(16, activation="relu"),
    Dense(8, activation="relu"),
    Dense(1, activation="sigmoid"),
])
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
model.fit(X_train, y_train, epochs=200, batch_size=4, verbose=0)

# 4. Evaluate model
_, train_acc = model.evaluate(X_train, y_train, verbose=0)
_, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f"Training Accuracy: {train_acc * 100:.2f}%")
print(f"Testing Accuracy : {test_acc * 100:.2f}%")

# 5. Predict approval for new applicant
new_applicant = [[55000, 720, 400000, 10000, 1]]
new_scaled = scaler.transform(np.array(new_applicant))
prob = model.predict(new_scaled, verbose=0)[0][0]

if prob >= 0.5:
    print("Prediction: Loan Approved")
else:
    print("Prediction: Loan Rejected")
print(f"(Probability of approval: {prob:.4f})")