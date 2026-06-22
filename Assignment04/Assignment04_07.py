# Predict the output

d = {
    1 : "One",
    1 : "One",
    2 : "Two"
}
print(d)

# why does this happen ?
# In a dictionary, keys must be unique. When you define a dictionary with duplicate keys, the last value assigned to that key will overwrite the previous value. In this case, the key `1` is defined twice, and the second definition (`1 : "One"`) overwrites the first one. Therefore, the dictionary will only contain one entry for the key `1`, which is `"One"`, and the entry for key `2` will be `"Two"`. The output will be `{1: 'One', 2: 'Two'}`.