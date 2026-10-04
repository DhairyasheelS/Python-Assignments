import numpy as np

image = np.array([
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,1,1,1,1],
    [0,0,0,0,0],
    [0,0,0,0,0]
])

kernel = np.array([
    [-1,-1,-1],
    [0,0,0],
    [1,1,1]
])

feature_map = np.zeros((3,3))

for i in range(3):
    for j in range(3):

        # Extract 3x3 region
        region = image[i:i+3, j:j+3]

        # Multiply and Sum
        result = np.sum(region * kernel)

        # Store result
        feature_map[i][j] = result

# ------------------------------------------------------
# Step 4 : Show Feature Map
# ------------------------------------------------------
print("\nFeature Map (Detected Edges)")
print(feature_map)