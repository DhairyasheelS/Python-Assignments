# write program which accepts one number and prints that many numbers starting from 1

def DisplayNumbers(No):
    
    print("Numbers :")
    for cnt in range(1,No+1):
        print(cnt)

def main():
    
    Value = int(input("Enter Your Number :\n"))
    
    DisplayNumbers(Value)


if __name__ == "__main__":
    main()