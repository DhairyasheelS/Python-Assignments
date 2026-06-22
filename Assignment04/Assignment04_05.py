#predict the output

s = "python"
print(id(s))

s = s + "3"
print(id(s))

# it will return memory address of s and when we add s = s + 3 its memory address gets changes
# we get different results for both s print