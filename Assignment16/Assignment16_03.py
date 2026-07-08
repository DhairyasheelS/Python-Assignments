'''
write a program which contains one function named as Add()
which accepts two numbers from user and return addition of that two numbers
'''

Add = lambda No1 , No2 : No1 + No2
    
def main():
    
    Value1 = int(input("Enter first number :\n"))

    Value2 = int(input("Enter second number :\n"))

    Ret = Add(Value1 , Value2)

    print("Addition is :",Ret)
    
if __name__ == "__main__":
    main()