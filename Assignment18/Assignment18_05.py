'''
write a program which accept N numbers from user and store it into List.
return addition of all prime numbers from that list. Main python file accepts N numbers from user
and pass each number to ChkPrime() function which is part of oour user defined module named as MarvellousNum. Name of function from 
main python file should be ListPrime()
'''
import MarvellousNum as ma

def ListPrime(List):

    PrimeL = list()
    Sum = 0

    for no in List:
        if(ma.ChkPrime(no)):
            PrimeL.append(no)
    
    for no in PrimeL:
        Sum = Sum + no
    return Sum

def main():
    Data = list()

    Value1 = int(input("Enter how many numbers do you want to store in list\n"))

    print("Enter the elements")
    for cnt in range(Value1):
        No = int(input())
        Data.append(No)

    Ret = ListPrime(Data)

    print(f"Sum of Prime numbers from list is : {Ret}")

if __name__ == "__main__":
    main()