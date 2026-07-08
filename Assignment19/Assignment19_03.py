'''
write a program which contains filter() map() reduce() in it. python application which contains
one list of numbers. List contains the numbers which are accepted from user
Filter should filter out all such numbers which grater than equal to 70 and less than or equal to 90. Map function will increase each number by 10
Reduce will return product of all that numbers
'''
from functools import reduce

def listmaker(n):
    arr=list()
    for i in range(1,n+1):
        value=int(input(f"Enter value {i} :"))
        arr.append(value)
    return arr

def filterx(n):
    if n >= 70 and n <= 90 :
        return n

mapx = lambda n : n+10
reducex = lambda n,m : n*m

    
def main():
    Value1 = int(input("Enter how many numbers do you want to store in list\n"))
    listx=listmaker(Value1)
    FData = list(filter(filterx,listx))
    MData = list(map(mapx,FData))
    RData = reduce(reducex,MData)

    print(f"The list is : {listx}")
    print(f"The list after filter function is : {list(FData)}")
    print(f"The list after map function is : {(list(MData))}")
    print(f"The list after reduce function is : {RData}")

if __name__ == "__main__":
    main()