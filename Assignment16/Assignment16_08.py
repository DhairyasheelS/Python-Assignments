'''
write a program which accept number from user and returns true if number 
is divisible by 5 otherwise return false
'''
def Display(No):

    for cnt in range(No):
        print("*",end=" ")
        
        
def main():
    Value = int(input("Enter your number :\n"))

    Ret = Display(Value)

    
if __name__ == "__main__":
    main()