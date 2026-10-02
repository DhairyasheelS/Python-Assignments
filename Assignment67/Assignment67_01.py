"""
Marvellous Infosystems : Python - Automation & Machine Learning
Deep Learning Assignment - Q1: Predict whether a customer will leave a service

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

# 1. Load / create dataset
# Feature meaning: [Age, Monthly Charges, Tenure, Complaints, Support Calls]
X = [
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7],
]
# Output meaning: 0 = Customer will stay, 1 = Customer will leave
y = [0, 0, 1, 1, 0, 0, 1, 1, 0, 1]

columns = ["Age", "MonthlyCharges", "Tenure", "Complaints", "SupportCalls"]
df = pd.DataFrame(X, columns=columns)
df["Churn"] = y

# 2. Clean the dataset
df = df.drop_duplicates().dropna()
X = df.drop(columns=["Churn"]).values
y = df["Churn"].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Apply StandardScaler (fit on train only)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Train FNN model
model = Sequential([
    Input(shape=(X_train.shape[1],)),
    Dense(16, activation="relu"),
    Dense(8, activation="relu"),
    Dense(1, activation="sigmoid"),
])
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
model.fit(X_train, y_train, epochs=200, batch_size=4, verbose=0)

# 5. Evaluate accuracy
_, train_acc = model.evaluate(X_train, y_train, verbose=0)
_, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f"Training Accuracy: {train_acc * 100:.2f}%")
print(f"Testing Accuracy : {test_acc * 100:.2f}%")

# Test input
new_customer = [[46, 1450, 5, 6, 9]]
new_scaled = scaler.transform(np.array(new_customer))
prob = model.predict(new_scaled, verbose=0)[0][0]

if prob >= 0.5:
    print("Prediction: Customer may leave")
else:
    print("Prediction: Customer will stay")
print(f"(Probability of leaving: {prob:.4f})")