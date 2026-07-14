'''
write python program to implement a class named Circle with following
requirements

- the class should contain three instance variables: radius , area , and circumference
- the class should contain one class varible named PI , initialized to 3.14
- define constructor that initializes all instance varibles to 0.0

Implement the following instance methods:
    Accept() - accepts the radius of the circle from user
    CalculateArea() - calculates the area of the circle and stores it in the area variable
    CalculateCircumference() - calculates the circumference of circle and stores it in the circumference variable
'''

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0
        self.Area = 0
        self.Circumference = 0

    def Accept(self):
        self.Radius = int(input("Enter Your Radius : \n"))
    
    def CalculateArea(self):
        self.Area = self.PI * (self.Radius **2)
        return self.Area

    def CalculateCircumference(self):
        self.Circumference = 2 * self.PI * self.Radius
        return self.Circumference

def main():
    cobj = Circle()

    cobj.Accept()

    Ret1 = cobj.CalculateArea()
    Ret2 = cobj.CalculateCircumference()

    print(f"Area of Circle is : {Ret1} ")
    print(f"Circumference of circle is : {Ret2}")

if __name__ == "__main__":
    main()
