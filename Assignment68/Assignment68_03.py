import numpy as np

# Step 1: 2D matrix
matrix = np.array([
    [6, 4],
    [8, 6]
])
print("Input matrix:\n", matrix, "\n")

# Step 2: flatten into a 1D vector
flatten_output = matrix.flatten()
print("Flatten output:", flatten_output)          # [6 4 8 6]
print("Shape:", matrix.shape, "->", flatten_output.shape, "\n")

# Step 3: fully connected layer (1 neuron)
weights = np.array([0.1, 0.2, 0.3, 0.4])
bias = 0.5

output = np.dot(flatten_output, weights) + bias   # y = w.x + b
print("Fully connected output:", round(output, 2))

# Step 4: manual calculation
# y = (6*0.1) + (4*0.2) + (8*0.3) + (6*0.4) + 0.5
#   = 0.6 + 0.8 + 2.4 + 2.4 + 0.5
#   = 6.7
print("""
Manual calculation:
y = (6*0.1) + (4*0.2) + (8*0.3) + (6*0.4) + 0.5
  = 0.6 + 0.8 + 2.4 + 2.4 + 0.5
  = 6.7
""")

# Step 5: explanation
print("""Role of the flatten layer in a CNN:
Convolution and pooling layers produce 2D (or 3D) feature maps, but a fully
connected layer expects a 1D vector as input. Flatten reshapes the feature
maps into one long vector without changing any values, so it acts as the
bridge between the feature-extraction part of the CNN and the classification
part. It has no learnable parameters.""")