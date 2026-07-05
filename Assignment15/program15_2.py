#Write a lambda fun using filter()which accepts a list of numbers and returns a list of even numbers

Nums = [ 1,2,3,4,5,6,7,8,9]
Even = list(filter(lambda x : x  % 2 == 0,Nums))

print("List of Even numbers are :",Even)