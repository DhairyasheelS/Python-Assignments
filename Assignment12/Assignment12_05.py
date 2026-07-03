# write program which accepts one number and prints that many numbers starting from 1
# in Reverse order

def DisplayNumbers(No):
    
    print("Numbers :")
    for cnt in range(No , 0, -1):
        print(cnt)

def main():
    
    Value = int(input("Enter Your Number :\n"))
    
    DisplayNumbers(Value)


if __name__ == "__main__":
    main()