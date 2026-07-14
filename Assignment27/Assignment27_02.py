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

class BankAccount:
    ROI = 10.5

    def __init__(self , AccName , CurrBalance):
        self.Name = AccName
        self.Balance = CurrBalance
        
    def Display(self):
        print(f"Account Holder Name : {self.Name} \n{self.Name}'s Account Balance is : {self.Balance}")
    
    def Deposit(self , amount):
        self.Balance = self.Balance + amount
        print(f"Updated Balance is {self.Balance}")
    
    def Withdraw(self , withdrwAmount):
        if(self.Balance < withdrwAmount):
            print("Insufficient Balance")
        else:
            self.Balance = self.Balance - withdrwAmount
            print(f"{withdrwAmount} is debited from your account")
    
    def CalculateInterest(self):
        Interest = (self.Balance * BankAccount.ROI) / 100
        return Interest
    
def main():
    
    obj1 = BankAccount("Dhairyasheel Shinde" , 1000)
    obj1.Display()
    obj1.Deposit(1000)
    obj1.Withdraw(5000)
    
    Ret = obj1.CalculateInterest()
    print(f"Interest is : {Ret}")

    obj2 = BankAccount("Aditya Parit" , 50000)
    obj2.Display()
    obj2.Deposit(1000)
    obj2.Withdraw(5000)
    
    Ret = obj2.CalculateInterest()
    print(f"Interest is : {Ret}")

    
if __name__ == "__main__":
    main()
