#Write a lambda fun using filter()which accepts a list of numbers and returns a list of numbers which are divisible by both 3 and 5

Nums = [ 1, 2 ,3, 5 , 6 , 9 ,10,15,20]
data = list(filter(lambda x : x  % 3  and  x % 5 == 0,Nums))

print("List of numbers which is divisible by 3 and 5 are :",data)