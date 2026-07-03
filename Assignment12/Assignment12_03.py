# write program which accepts two numbers and prints Add,Sub,Mul,Div

def Calculation(No1 , No2):
    Add = No1 + No2
    Sub = No1 - No2
    Mul = No1 * No2
    Div = No1 // No2

    return Add , Sub , Mul , Div

def main():
    
    Value1 = int(input("Enter First Number :\n"))
    Value2 = int(input("Enter Second Number :\n"))

    Ret1 , Ret2 , Ret3, Ret4, = Calculation(Value1,Value2)

    print("Addition is :",Ret1)
    print("Substraction is :",Ret2)
    print("Multiplication is :",Ret3)
    print("Division is :",Ret4)

if __name__ == "__main__":
    main()