'''
Display File contents:
    write a program which accept a file name from user and checks
    whether that file exists in current directory or not
'''
import os

def DisplayFileContents(FName):
    
    if (os.path.exists(FName)):
        fobj = open(FName, "r")

        Data = fobj.read()

        print(Data)
    else:
        print("File not exist")
    
def main():
    
    File_Name = input("Enter File name :\n")

    DisplayFileContents(File_Name)

if __name__ == "__main__":
    main()