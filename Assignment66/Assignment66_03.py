"""
Deep Learning Assignment - Q3: Calculate loss manually
"""
import math

# 3. Take actual and predicted values
# Regression example (for MSE)
actual_reg = [3.0, 5.0, 2.5, 7.0]
predicted_reg = [2.5, 5.0, 4.0, 8.0]

# Classification example (for Binary Cross Entropy)
actual_cls = [1, 0, 1, 1, 0]
predicted_cls = [0.9, 0.2, 0.8, 0.6, 0.1]


# 1. Mean Squared Error
def mean_squared_error(actual, predicted):
    n = len(actual)
    total = 0
    for a, p in zip(actual, predicted):
        total += (a - p) ** 2
    return total / n


# 2. Binary Cross Entropy
def binary_cross_entropy(actual, predicted):
    eps = 1e-15  # avoid log(0)
    n = len(actual)
    total = 0
    for a, p in zip(actual, predicted):
        p = min(max(p, eps), 1 - eps)
        total += a * math.log(p) + (1 - a) * math.log(1 - p)
    return -total / n


# 4. Display the calculated loss
print("Actual (regression)   :", actual_reg)
print("Predicted (regression):", predicted_reg)
print("Mean Squared Error    :", round(mean_squared_error(actual_reg, predicted_reg), 4))

print("\nActual (classification)   :", actual_cls)
print("Predicted (classification):", predicted_cls)
print("Binary Cross Entropy      :", round(binary_cross_entropy(actual_cls, predicted_cls), 4))

# 5. Explanation
print("\nMean Squared Error is used for REGRESSION (predicting continuous values like price).")
print("Binary Cross Entropy is used for CLASSIFICATION (predicting 0/1 classes like spam or not spam).")