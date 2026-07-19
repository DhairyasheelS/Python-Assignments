'''
Copy File contents into another file :
    write a program which accepts two files names from user
        First file is an existing file
        second file is a new file
'''
import os
import sys

def CopyFiles(fName1 , fName2):
    bFlag = False
    try:
        if (os.path.exists(fName1) and os.path.exists(fName2) ):
            fobj1 = open(fName1,"r")

            fobj2 = open(fName2,"r")
            
            for lines in fobj1:
                if(lines == fobj2.readline()):
                    bFlag = True
                    return bFlag
                else:
                    return bFlag
        else:
            print("Files does not exist")        
        
    except Exception as eobj:
        print(eobj)

def main():

    if(len(sys.argv) == 3):
        File_Name1 = sys.argv[1]
        File_Name2 = sys.argv[2]
    else:
        print("Invalid Number of Arguments")

    Ret = CopyFiles(File_Name1 , File_Name2)

    if (Ret == True):
        print("Success!")
    else:
        print("Failure")

if __name__ == "__main__":
    main()