'''
write a program which accept one number from user and Check wether it is 
prime or not
'''

def ChkPrime(No):
    bFlag = True

    if(No == 0 or No == 1):
        bFlag = False
        return bFlag

    for cnt in range(2,No):
        if(No % cnt == 0):
            bFlag = False
            break

    return bFlag

def main():

    Value = int(input("Enter Number :\n"))

    Ret = ChkPrime(Value)

    if(Ret == True):
        print("It is prime number")
    else:
        print("It is not prime number")

if __name__ == "__main__":
    main()