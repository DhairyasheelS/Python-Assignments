#write a program which accepts one number and prints all odd numbers till that number

def PrintOdd(No):
    
    print("Odd Numbers till",No,"are:")
    for cnt in range(1,No+1):
        if(cnt % 2 != 0):
            print(cnt)
       
def main():
    
    Value = int(input("Enter the number :\n"))

    PrintOdd(Value)

if __name__ == "__main__":
    main()