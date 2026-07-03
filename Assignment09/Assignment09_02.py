# write a program which contains one function ChkGreater() that accepts
# two numbers and print the greater number

def ChkGreater(No1,No2):
    if(No1 > No2):
        return No1
    else:
        return No2

def main():
    
    Value1 = int(input("Enter the first number :\n"))
    Value2 = int(input("Enter the second number :\n"))

    Ret = ChkGreater(Value1,Value2)

    print(Ret,"is greater!")

if __name__ == "__main__":
    main()