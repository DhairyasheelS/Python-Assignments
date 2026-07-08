'''
write a program which contains one lambda function which accepts one parameter
and return power of two
'''
Power = lambda No: No ** 2

def main():

    Value = int(input("Enter Number \n"))

    Ret = Power(Value)

    print(f"Power of two of {Value} is : {Ret}")

if __name__ == "__main__":
    main()