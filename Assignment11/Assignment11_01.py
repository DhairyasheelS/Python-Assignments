#write a program which accepts one number and cheks whether it is prime or not

def CheckPrime(No):

    bFlag = False

    if(No == 1 or No == 2) : return bFlag

    for cnt in range (2 , No):
        if((No % cnt) == 0):
            bFlag = True
        
    return bFlag
    
def main():
    
    Value = int(input("Enter the number :\n"))

    Ret = CheckPrime(Value)

    if(Ret == False):
        print("Its Prime Number !!")
    else:
        print("Its Not prime number !!")

if __name__ == "__main__":
    main()