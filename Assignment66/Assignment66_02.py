"""
Deep Learning Assignment - Q2: Demonstrate different activation functions
"""

import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


def tanh(x):
    return np.tanh(x)


# 1. Input values from -10 to 10
x = np.linspace(-10, 10, 200)

# 2. Plot all activation functions
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(x, sigmoid(x), color="blue")
plt.title("Sigmoid")
plt.grid(True)

plt.subplot(1, 3, 2)
plt.plot(x, relu(x), color="green")
plt.title("ReLU")
plt.grid(True)

plt.subplot(1, 3, 3)
plt.plot(x, tanh(x), color="red")
plt.title("Tanh")
plt.grid(True)

plt.tight_layout()
plt.show()

# 3. Use of each activation function
print("Sigmoid: Output range is 0 to 1. Used in the output layer for binary classification.")
print("ReLU   : Output is max(0, x). Most common in hidden layers; fast and reduces vanishing gradient.")
print("Tanh   : Output range is -1 to 1 and zero-centered. Used in hidden layers, especially RNNs.")