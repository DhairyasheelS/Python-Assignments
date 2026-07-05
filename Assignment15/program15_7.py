#Write a lambda fun using filter()which accepts a list of strings and returns a list of strings having length greater than 5

Names = ["Richa", "Prachi", "Siya", "Ridhant", "Dhairyasheel"]

Ret = list(filter(lambda x: len(x) > 5, Names))

print("Names from the string are  : ", Ret)