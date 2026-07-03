# write program which accepts one character and prints factor

def DisplayFactors(No):

    for cnt in range(1,No+1):
        if(No % cnt == 0):
            print(cnt)
    
def main():
    
    Value = int(input("Enter your number :\n"))

    DisplayFactors(Value)

if __name__ == "__main__":
    main()