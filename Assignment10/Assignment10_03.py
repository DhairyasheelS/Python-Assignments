#write a program which accepts one number and prints factorial of that number

def Factorial(No):
    Fact = 1

    if (No < 0):
        return -1
    
    for cnt in range(1 , No + 1):
        Fact = Fact * cnt
    return Fact
    
    
def main():
    
    Value = int(input("Enter the number :\n"))

    Ret = Factorial(Value)

    print("Factorial is :",Ret)

if __name__ == "__main__":
    main()