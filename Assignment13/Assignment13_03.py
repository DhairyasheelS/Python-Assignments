# write a program which accepts one number and check whether it is perfect or not

def ChkPerfect(No):

    Sum = 0
    temp = No

    for cnt in range(1,No):
        if(No % cnt == 0):
            Sum = Sum + cnt

    return (temp == Sum) 
 
def main():

    Value1 = int(input("Enter Number:\n"))

    Ret = ChkPerfect(Value1)

    if(Ret == True):
        print("It is perfect number")
    else:
        print("It is not perfect")
    
if __name__ == "__main__":
    main()