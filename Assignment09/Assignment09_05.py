# write a program which accpets one number and checks wheater it is divisible by 3 and 5

# def CheckDivisible(No):
    
#     if((No % 3 == 0) and (No % 5 == 0)):
#         return True
#     else:
#         return False
CheckDivisible = lambda No : (No % 3 == 0) and (No % 5 == 0)

def main():

    Value = int(input("Enter the number :\n"))
    
    Ret = CheckDivisible(Value)

    if(Ret == True):
        print("its divisible by 3 and 5")
    else:
        print("its not divisible by 3 and 5")

if __name__ == "__main__":
    main()