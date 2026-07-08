'''
write a program which accept number from user and check whether that number
is positive or negative or zero
'''
def ChkNumber(No):
    
    if(No > 0):
        return 1
    elif(No < 0):
        return -1
    else:
        return 0
        
        
def main():
    Value = int(input("Enter your number :\n"))

    Ret = ChkNumber(Value)

    if(Ret == 0):
        print(f"{Value} is Zero")
    elif(Ret == 1):
        print(f"{Value} is Positive")
    else:
        print(f"{Value} is Negative")
        
if __name__ == "__main__":
    main()