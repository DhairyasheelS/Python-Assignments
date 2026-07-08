'''
create one module named as Arithmatic which contains 4 functions as Add() for Addition
Sub() for substraction , Mul() for multiplication and Div() for division. All functions accepts
two parameters as number and perform the operation. write on python program which call all 
the functions from arithmatic module by accepting the paramerts from user
'''

import Arithmatic

def main():
    Value1 = int(input("Enter your first number :\n"))
    Value2 = int(input("Enter your second number :\n"))

    Ret1 = Arithmatic.Add(Value1,Value2)
    Ret2 = Arithmatic.Sub(Value1,Value2)
    Ret3 = Arithmatic.Mul(Value1,Value2)
    Ret4 = Arithmatic.Div(Value1,Value2)

    print(f"Addition of {Value1} and {Value2} are : {Ret1}")
    print(f"Substraction of {Value1} and {Value2} are : {Ret2}") 
    print(f"Multiplication of {Value1} and {Value2} are : {Ret3}") 
    print(f"Division of {Value1} and {Value2} are : {Ret4}")  

if __name__ == "__main__":
    main()