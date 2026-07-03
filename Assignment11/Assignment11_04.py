#write a program which accepts one number and prints reverse of that number

def RevDigits(No):
    Rev = 0
    Digit = 0

    while(No != 0):
        Digit = No % 10
        Rev = (Rev * 10) + Digit
        No = No // 10
    return Rev

def main():
    
    Value = int(input("Enter your number :\n"))

    Ret = RevDigits(Value)

    print("Revese of",Value,"is:",Ret)

if __name__ == "__main__":
    main()