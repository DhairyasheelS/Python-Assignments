'''
write a program which accept N numbers from user and
store it into list. accept one another number from user and return frequency of that number
'''

def FrequencyCount(List,FreqElement):
    
    cnt = 0
    for no in List:
        if(no == FreqElement):
            cnt = cnt + 1
        
    return cnt
    

def main():
    Data = list()

    Value1 = int(input("Enter how many numbers do you want to store in list\n"))

    print("Enter the elements")
    for cnt in range(Value1):
        No = int(input())
        Data.append(No)

    Value2 = int(input("Element to search :\n"))

    Ret = FrequencyCount(Data,Value2)

    print(f"Frequency of {Value2} in {Data} list is : {Ret}")

if __name__ == "__main__":
    main()