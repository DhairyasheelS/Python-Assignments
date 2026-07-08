'''
write a program which display first 10 even numbers on screen
'''

def DisplayEven(No):

    for cnt in range(1,No):
        if(cnt % 2 == 0):
            print(cnt, end=" ")
        
        
def main():
    Value = int(input("Enter your number :\n"))

    DisplayEven(Value)


if __name__ == "__main__":
    main()