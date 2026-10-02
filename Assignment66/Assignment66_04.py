"""
Deep Learning Assignment - Q4: Show how weights are updated in an ANN
(single neuron, gradient descent)
"""

# 1. Take input, weight, bias, target output and learning rate
x = 2.0
weight = 0.5
bias = 0.1
target = 4.0
learning_rate = 0.1

old_weight = weight
old_bias = bias

# 2. Calculate prediction
prediction = weight * x + bias
print("Prediction:", round(prediction, 4))

# 3. Calculate error
error = prediction - target
loss = 0.5 * error ** 2
print("Error     :", round(error, 4))
print("Loss      :", round(loss, 4))

# 4. Update weight using gradient descent logic
# loss = 1/2 * (prediction - target)^2
# d(loss)/d(weight) = error * x
# d(loss)/d(bias)   = error
grad_w = error * x
grad_b = error

weight = weight - learning_rate * grad_w
bias = bias - learning_rate * grad_b

# 5. Display old weight and updated weight
print("\nOld weight    :", old_weight)
print("Updated weight:", round(weight, 4))
print("Old bias      :", old_bias)
print("Updated bias  :", round(bias, 4))

new_prediction = weight * x + bias
print("\nNew prediction:", round(new_prediction, 4), "(closer to target", target, ")")