#Write a lambda fun using filter()which accepts a list of numbers and returns a list of odd numbers

Nums = [ 1,2,3,4,5,6,7,8,9]
Odd = list(filter(lambda x : x  % 2 != 0,Nums))

print("List of Odd numbers are :",Odd)