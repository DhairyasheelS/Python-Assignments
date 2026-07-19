'''
check file exists in current directory:
    write a program which accept a file name from user and checks
    whether that file exists in current directory or not
'''
import os

def CheckExists(FName):
    bFlag = False

    if (os.path.exists(FName)):
        bFlag = True
        return bFlag
    
    return bFlag
    
def main():
    
    File_Name = input("Enter File name :\n")

    Ret = CheckExists(File_Name) 

    if(Ret == True):
        print("File in present")
    else:
        print("File is not present")

if __name__ == "__main__":
    main()