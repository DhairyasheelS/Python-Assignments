'''
write a program which accept one number from user and return its factorial
'''

def Fact(No):
    Fact = 1

    for cnt in range(1,No+1):
        Fact = Fact * cnt
    return Fact

def main():

    Value = int(input("Enter Number :\n"))

    Ret = Fact(Value)

    print(f"Factorial of {Value} is : {Ret}")

if __name__ == "__main__":
    main()