'''
write a program which contains one lambda function which accepts one parameter
and return its multiplication
'''
Mul = lambda No1 , No2 : No1 * No2

def main():

    Value1 = int(input("Enter First Number \n"))
    Value2 = int(input("Enter Second Number \n"))
    
    Ret = Mul(Value1,Value2)

    print(f"Multiplication is : {Ret}")

if __name__ == "__main__":
    main()