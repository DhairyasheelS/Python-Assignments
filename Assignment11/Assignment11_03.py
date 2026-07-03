#write a program which accepts one number and prints sum of digits

def SumDigits(No):
    Sum = 0
    Digit = 0

    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10
    return Sum

def main():
    
    Value = int(input("Enter your number :\n"))

    Ret = SumDigits(Value)

    print("Sum of Digits are:",Ret)

if __name__ == "__main__":
    main()