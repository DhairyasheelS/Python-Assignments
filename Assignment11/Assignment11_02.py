#write a program which accepts one number and prints count of digits in that number

def CountDigit(No):
    Count = 0

    while(No != 0):
        Count = Count + 1
        No = No // 10
    return Count

def main():
    
    Value = int(input("Enter your number :\n"))

    Ret = CountDigit(Value)

    print("Count of Digits are:",Ret)

if __name__ == "__main__":
    main()