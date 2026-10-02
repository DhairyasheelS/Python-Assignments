"""
Deep Learning Assignment - Q1: Simulate a single artificial neuron
"""
import math

# Input
x1 = 2
x2 = 3
w1 = 0.4
w2 = 0.6
bias = 0.5

# 1. Calculate weighted sum
z = (x1 * w1) + (x2 * w2) + bias
print("Weighted sum (z) =", z)

# 2. Apply sigmoid activation function
output = 1 / (1 + math.exp(-z))

# 3. Display final output
print("Final output (sigmoid) =", round(output, 4))

# 4. Explain whether output is close to 0 or 1
if output >= 0.5:
    print("The output is close to 1, so the neuron is activated (fires).")
else:
    print("The output is close to 0, so the neuron is not activated.")

print("\nExplanation: Sigmoid squashes any value into the range 0 to 1.")
print("A large positive weighted sum gives an output near 1,")
print("and a large negative weighted sum gives an output near 0.")