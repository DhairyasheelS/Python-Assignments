'''
write a program which accept one number from user and return 
addition of its factors
'''

def AddFact(No):
    Sum = 0

    for cnt in range(1,No):
        if(No % cnt == 0):
            Sum = Sum + cnt
    return Sum

def main():

    Value = int(input("Enter Number :\n"))

    Ret = AddFact(Value)

    print(f"Addition of factors of {Value} are : {Ret}")

if __name__ == "__main__":
    main()