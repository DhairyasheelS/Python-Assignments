ChkNum = lambda Num: True if Num % 2 == 0 else False
    
Ret = ChkNum(10)

if Ret:
    print("Number is even")
else:
    print("Number is odd")