'''
write a program which accept number from user and return digits 
in that number 
'''
def CountDigit(No):

    SumDigit = 0

    while(No != 0):
        SumDigit = SumDigit + 1
        No = No // 10
    return SumDigit

def main():

    Value = int(input("Enter the number \n"))

    Ret = CountDigit(Value)

    print(f"Length of {Value} is :",Ret)

if __name__ == "__main__":
    main()