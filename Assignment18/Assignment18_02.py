'''
write a program which accept N numbers from user and
store it into list. return maximum of all elements from that list
'''

def MaxList(List):
    
    Max = List[0]

    for no in List:
        if(Max < no):
            Max = no

    return Max

def main():
    Data = list()

    Value = int(input("Enter how many numbers do you want to store in list\n"))

    print("Enter the elements")
    for cnt in range(Value):
        No = int(input())
        Data.append(No)

    Ret = MaxList(Data)

    print(f"Maximum from {Data} list is : {Ret}")

if __name__ == "__main__":
    main()