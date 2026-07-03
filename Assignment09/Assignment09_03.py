# write a program which accepts one number and prints square of that number

def Square(No):
    return No * No
# Square = lambda No : No * No

def main():

    Value = int(input("Enter the number :\n"))
    
    Ret = Square(Value)

    print("Square of",Value,"is:",Ret)

if __name__ == "__main__":
    main()