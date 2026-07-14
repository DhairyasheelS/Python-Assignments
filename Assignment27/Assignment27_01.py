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

class BookStore:
    NoOfBooks = 0

    def __init__(self , BookName , BookAuthor):
        self.Name = BookName
        self.Author = BookAuthor
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(f"{self.Name} by {self.Author} . No of books : {BookStore.NoOfBooks}")
    
def main():
    
    obj1 = BookStore("Linux System Programming", "Robert Love")
    obj1.Display()

    obj2 = BookStore("C Programming" , "Dennis Ritchie")
    obj2.Display()


if __name__ == "__main__":
    main()
