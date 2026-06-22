# Predict The output

lst = [10,20,30]
tpl = (10,20,30)

lst[0] = 100
tpl[0] = 100

#which line will raise an error and why?
# The line `tpl[0] = 100` will raise an error.
#because tuples are immutable in Python, meaning that once a tuple is created, its elements cannot be changed.