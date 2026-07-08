'''
write a program which accept N numbers from user and
store it into list. return minimum of all elements from that list
'''

def MinList(List):
    
    Min = List[0]

    for no in List:
        if(Min > no):
            Min = no

    return Min

def main():
    Data = list()

    Value = int(input("Enter how many numbers do you want to store in list\n"))

    print("Enter the elements")
    for cnt in range(Value):
        No = int(input())
        Data.append(No)

    Ret = MinList(Data)

    print(f"Minimum from {Data} list is : {Ret}")

if __name__ == "__main__":
    main()