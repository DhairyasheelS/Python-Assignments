from functools import reduce

def listmaker(n):
    arr=list()
    for i in range (1,n+1):
        value=int(input(f"Enter Value {i} :"))
        arr.append(value)

    return arr

def filterx(n):
        if n % 2 == 0 :
            return n
        
square = lambda n : n**2
addition = lambda n,m : n+m

def main():
    no_elements=int(input("Enter number of elements to insert in list : "))
    listx=listmaker(no_elements)
    FData = list(filter(filterx,listx))
    MData = list(map(square,FData))
    RData = reduce(addition,list(MData))

    print(f"The list is : {listx}")
    print(f"The Even numbers is list are : {FData}")
    print(f"The Addition of list is : {RData}")

if __name__=="__main__":
    main()