'''
write a program which accept number from user and return sum of digits 
that number 
'''
def SumDigit(No):

    Sum = 0
    Digit = 0

    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10
    return Sum

def main():

    Value = int(input("Enter the number \n"))

    Ret = SumDigit(Value)

    print("Sum is:",Ret)

if __name__ == "__main__":
    main()