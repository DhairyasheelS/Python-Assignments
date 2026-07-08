def ChkPrime(no):
    bFlag = True

    if(no == 1 or no == 0): 
        bFlag = False
        return bFlag
    
    for cnt in range(2,no):
        if(no % cnt == 0):
            bFlag = False
            break
    return bFlag