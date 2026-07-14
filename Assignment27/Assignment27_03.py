'''
write python program to implement a class named demo with following
specifications

-class should contain two instance varibles : no1 and no2
-the class should contain one class variable named Value
-Define a constructor(__init__) that accepts two parameters and initializes the instance variable
-Implement two instance methods:
    Fun() - Displays the values of instances variables no1 and no2
    Gun() - Displays the values of instace variables no1 and no2
'''

class Numbers:

    def __init__(self , No):
        self.Value = No
    
    def ChkPrime(self):
        bFlag = True

        for cnt in range(2 , self.Value):
            if(self.Value % cnt == 0):
                bFlag = False
                break
        return bFlag

    def ChkPerfect(self):
        Sum = 0

        for cnt in range(1,self.Value):
            if(self.Value % cnt == 0):
                Sum = Sum + cnt
        
        return (self.Value == Sum)

    def Factors(self):

        print(f"factors of {self.Value}")
        for cnt in range(1,self.Value):
            if(self.Value % cnt == 0):
                print(cnt, end="\t")
        print()
                
    def SumFactors(self):
        Sum = 0

        for cnt in range(1,self.Value):
            if(self.Value % cnt == 0):
                Sum = Sum + cnt
        
        return Sum


def main():
    
    Value = int(input("Enter Number :\n"))

    obj1 = Numbers(Value)

    Ret = obj1.ChkPrime()
    
    if (Ret == True):
        print(f"{Value} is prime number")
    else:
        print(f"{Value} is not prime number")
    
    Ret = obj1.ChkPerfect()
    if (Ret == True):
        print(f"{Value} is Perfect number")
    else:
        print(f"{Value} is not perfect number")

    obj1.Factors()

    Ret = obj1.SumFactors()
    print(f"Sum of factors of {Value} is : {Ret}")
    
if __name__ == "__main__":
    main()
