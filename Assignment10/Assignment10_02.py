#write a program which accepts one number and prints sum of first N Natural numbers

def SumNnumbers(No):
    Sum = 0;

    for cnt in range(No + 1):
        Sum = Sum + cnt
    return Sum
    
    
def main():
    
    Value = int(input("Enter the number :\n"))

    Ret = SumNnumbers(Value)

    print("Sum is :",Ret)

if __name__ == "__main__":
    main()