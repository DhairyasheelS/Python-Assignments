# Q2 . What is difference between :
# a = 10
# b = 10
# and 
# a = [10]
# b = [10]
#Explain using ID

# In the first case, 
# a and b are both assigned the value 10. 
# Since integers are immutable in Python,
#  both a and b will point to the same memory location ,,
# where the value 10 is stored. Therefore, the ID of a and b will be the same.   

# In the second case, 
# a and b are both assigned a list containing the value 10.
# Since lists are mutable in Python, 
# a and b will point to different memory locations where their respective lists are stored. 
# Therefore, the ID of a and b will be different.