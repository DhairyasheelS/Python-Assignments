# write a program which accepts length and width of rectangle and prints area

def AreaRect(Length, Width):
    return Length * Width

def main():
    Value1 = int(input("Enter Length of Rectangle :\n"))

    Value2 = int(input("Enter Width of Rectangle :\n"))

    Ret = AreaRect(Value1, Value2)

    print("Area of Rectangle is :",Ret)
    
if __name__ == "__main__":
    main()