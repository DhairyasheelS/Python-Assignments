#Write a lambda fun using reduce()which accepts a list of numbers and returns product of all elements

from functools import reduce


Nums = [ 1,2,3,4,5]
Product = reduce(lambda x ,y:x * y,Nums)

print("Product of the list is  :",Product)