Largest = lambda a, b, c: a if (a > b and a > c) else (b if b > c else c)

Ret = Largest(10, 25, 15)
print("Largest number is : ", Ret)