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
class Demo:
    Value = 11

    def __init__(self , no1 , no2):
        self.Value1 = no1
        self.Value2 = no2
    
    def Fun(self):
        print(self.Value1)
        print(self.Value2)
    
    def Gun(self):
        print(self.Value1)
        print(self.Value2)

def main():
    dobj1 = Demo(11,21)
    dobj2 = Demo(51,101)

    dobj1.Fun() # 11 , 21
    dobj2.Fun() # 51 , 101

    dobj1.Gun()
    dobj2.Gun()

if __name__ == "__main__":
    main()
