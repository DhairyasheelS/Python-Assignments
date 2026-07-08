'''
write a program which accept number from user and returns true if number 
is divisible by 5 otherwise return false
'''
def ChkDivisible(No):
    bFlag = False

    if(No % 5 == 0):
        bFlag = True
        return bFlag
    
    return bFlag
        
        
def main():
    Value = int(input("Enter your number :\n"))

    Ret = ChkDivisible(Value)

    if(Ret == True):
        print(f"{Value} is divisible by 5")
    else:
        print(f"{Value} is not divisible by 5")

if __name__ == "__main__":
    main()