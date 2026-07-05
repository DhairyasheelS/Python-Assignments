#Write a lambda fun using reduce()which accepts a list of numbers and returns addition of all elements

from functools import reduce


Nums = [ 1,2,3,4,5,6,7,8]
Addtion = reduce(lambda x , y: x + y ,Nums)

print("Addition of the all elements of the list is  :",Addtion)