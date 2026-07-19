'''
Copy File contents into another file :
    write a program which accepts two files names from user
        First file is an existing file
        second file is a new file
'''
import os

def CopyFiles(fName1 , fName2):
    try:
        if(os.path.exists(fName1)):
            fobj1 = open(fName1,"r") 
            
            fobj2 = open(fName2, "w")
            
            for line in fobj1:
                fobj2.write(line)
        
    except Exception as eobj:
        print(eobj)

def main():
    
    File_Name1 = input("Enter First name of file:\n")
    File_Name2 = input("Enter Second name of file:\n")

    CopyFiles(File_Name1 , File_Name2)


if __name__ == "__main__":
    main()