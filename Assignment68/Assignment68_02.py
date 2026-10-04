import numpy as np

def ReLU(z):
    return np.maximum(0, z)

def max_pool(x, size=2, stride=2):
    rows, cols = x.shape
    out_r = (rows - size) // stride + 1
    out_c = (cols - size) // stride + 1
    out = np.zeros((out_r, out_c), dtype=x.dtype)
    for i in range(out_r):
        for j in range(out_c):
            window = x[i*stride:i*stride+size, j*stride:j*stride+size]
            out[i, j] = window.max()
    return out

feature_map = np.array([
    [3, 3, 3],
    [0, 0, 0],
    [-3, -3, -3]
])

print("Input feature map:\n", feature_map, "\n")

relu_output = ReLU(feature_map)
print("After ReLU:\n", relu_output, "\n")

pooled = max_pool(relu_output, size=2, stride=1)
print("After 2x2 max pooling:\n", pooled)
print("\nShape:", relu_output.shape, "->", pooled.shape)

print("""
Why pooling reduces size:
Each 2x2 window is replaced by its single largest value, so 4 values become 1.
This cuts computation and memory, reduces overfitting, and keeps the strongest
features while making the result less sensitive to small shifts.
""")