# write a program which accpets one number and prints cube of that number

def Cube(No):
    return No * No * No
# Square = lambda No : No * No * No

def main():

    Value = int(input("Enter the number :\n"))
    
    Ret = Cube(Value)

    print("Cube of",Value,"is:",Ret)

if __name__ == "__main__":
    main()