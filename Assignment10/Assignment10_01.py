#write a program which accepts one number and prints multiplication table of that number
def DisplayTable(No):

    print("Table of",No,"is :")
    for cnt in range(1,11):
        print(cnt * No)
    
def main():
    
    Value = int(input("Enter the number :\n"))

    DisplayTable(Value)

if __name__ == "__main__":
    main()