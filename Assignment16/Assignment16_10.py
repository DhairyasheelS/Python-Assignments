'''
write a program which accept name from user and display length of its 
name
'''

def DisplayLength(String):

    cnt = 0

    for ch in String:
        cnt = cnt + 1

    return cnt

def main():
    Value = input("Enter your String :\n")

    Ret = DisplayLength(Value)

    print(f"Length of {Value} is :",Ret)

if __name__ == "__main__":
    main()