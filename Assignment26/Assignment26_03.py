'''
write python program to implement a class named Arithmatic with following
charcteristics

- the class should contain two instance variables: Value1 and Value2
- define constructor that initializes all instance varibles to 0

Implement the following instance methods:
    Accept() - accepts values for Value1 and Value2 from user
    Addition() - returns the addition of value1 and value2
    Substraction() - returns the substraction of value1 and value2
    Multiplication() - returns the multiplication of value1 and value2
    Division() - returns the division of value1 and value2 (handle division by zero properly)
'''

class Arithmatic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self , Value1 , Value2):
        self.Value1 = Value1
        self.Value2 = Value2
    
    def Addition(self):
        return self.Value1 + self.Value2
    
    def Substraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        try:
            Div = self.Value1 / self.Value2
            return Div
        except Exception as eobj:
            print(f"Can't divide by zero {eobj}")
    

def main():

    Value1 = int(input("Enter First Number :\n"))
    Value2 = int(input("Enter Second Number :\n"))

    aobj = Arithmatic()

    aobj.Accept(Value1,Value2)

    Ret = aobj.Addition()
    print("Addition is :",Ret)

    Ret = aobj.Substraction()
    print("substraction is :",Ret) 

    Ret = aobj.Multiplication()
    print("Multiplication is :",Ret)  

    Ret = aobj.Division()
    print("Division is :",Ret)

if __name__ == "__main__":
    main()
