#Write a lambda fun using reduce()which accepts a list of numbers and returns maximum numbers 

from functools import reduce


Nums = [ 1,2,3,4,5,6,7,8]
MAx = reduce(lambda x , y:x if x > y else y,Nums)

print("MAximum number from the list is  :",MAx)
