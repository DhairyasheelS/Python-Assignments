# write a program which accepts Radius of circle and prints area of circle

def AreaCircle(Radius, PI = 3.14):
    
    return PI * Radius * Radius

def main():
    Value1 = int(input("Enter Radius:\n"))

    Ret = AreaCircle(Value1)

    print("Area of Circle is :",Ret)
    
if __name__ == "__main__":
    main()