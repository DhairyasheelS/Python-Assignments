# Q5 : Predict the Output : 
# a = 10
# b = 10
# print(id(a) == id(b))

# Explain why this happens.

a = 10
b = 10
print(id(a) == id(b))

# The output of the code will be True.
# This happens because in Python, small integers (typically between -5 and 256) are cached and reused by the interpreter.
# When you assign the value 10 to both a and b, they both point to the same memory location where the value 10 is stored.
# Therefore, the id() function will return the same memory address for both a and b, resulting in the output True.