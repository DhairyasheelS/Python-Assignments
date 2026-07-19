'''
Copy File contents into another file :
    write a program which accepts two files names from user
        First file is an existing file
        second file is a new file
'''
import os
import sys

def CopyFiles(fName):
    try:
        fobj1 = open(fName,"w")

        fobj2 = open("ABC.txt","r")
        
        for line in fobj2:
            fobj1.write(line)
        
    except Exception as eobj:
        print(eobj)

def main():

    if(len(sys.argv) == 2):
        File_Name = sys.argv[1]
    else:
        print("Invalid Number of Arguments")

    CopyFiles(File_Name)


if __name__ == "__main__":
    main()