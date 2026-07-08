'''
write a program which accept N numbers from user and
store it into list. return addition of all elements from that list
'''

def SumList(List):
    Sum = 0

    for no in List:
        Sum = Sum + no
    return Sum

def main():
    Data = list()

    Value = int(input("Enter how many numbers do you want to store in list\n"))

    print("Enter the elements")
    for cnt in range(Value):
        No = int(input())
        Data.append(No)

    Ret = SumList(Data)

    print(f"Addition of {Data} list is : {Ret}")

if __name__ == "__main__":
    main()