#write a program which accepts one number and check is it palindrome or not

def ChkPalindrome(No):
    Rev = 0
    Digit = 0
    Temp = No

    while(No != 0):
        Digit = No % 10
        Rev = (Rev * 10) + Digit
        No = No // 10
    return (Temp == Rev)

def main():
    
    Value = int(input("Enter your number :\n"))

    Ret = ChkPalindrome(Value)

    if(Ret == True):
        print("Its Palindrome!!")
    else:
        print("Its Not Palindrome!!")

if __name__ == "__main__":
    main()