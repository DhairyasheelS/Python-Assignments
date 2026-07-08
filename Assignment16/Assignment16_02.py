'''
write a program which contains one function named as ChkNum() which accept one
parameter as number. if number is even then it should display "Even Number" otherwise 
display "Odd Number" on console
'''

def ChkNum(No):

    if(No % 2 == 0):
        return True
    else:
        return False
    
def main():
    
    Value = int(input("Enter the number :\n"))

    Ret = ChkNum(Value)

    if(Ret == True):
        print("Even Number")
    else:
        print("Odd Number")
    
if __name__ == "__main__":
    main()