#write a program which accepts one number and prints all even numbers till that

def PrintEven(No):
    
    print("Even Numbers till",No,"are:")
    for cnt in range(1,No):
        if(cnt % 2 == 0):
            print(cnt)
       
def main():
    
    Value = int(input("Enter the number :\n"))

    PrintEven(Value)

if __name__ == "__main__":
    main()