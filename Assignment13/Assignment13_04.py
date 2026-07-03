# write a program which accepts one number and prints binary equivalent

def DisplayBinary(No):
    
    Digit = 0

    while(No != 0):
        Digit = No % 2
        print(Digit , end="")
        No = No // 2
 
def main():

    Value = int(input("Enter Number:\n"))

    DisplayBinary(Value)

if __name__ == "__main__":
    main()