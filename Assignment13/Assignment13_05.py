# write a program which accepts marks and displays grade

def DisplayGrade(Marks):
    
    if(Marks >= 75):
        print("Distinction")
    elif(Marks >= 60):
        print("First Class")
    elif(Marks >= 50):
        print("Second Class")
    elif(Marks < 50):
        print("Fail")
    else:
        print("Invalid input")
        
def main():

    Value = int(input("Enter Your Marks :\n"))

    DisplayGrade(Value)

if __name__ == "__main__":
    main()