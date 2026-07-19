'''
Count Lines in file :
    write a program which accepts a name of file name from user and counts how many
    lines are present in the file
'''
import os

def CountLines(fName):
    try:
        if(os.path.exists(fName)):
            fobj = open(fName,"r") 
            
            line_cnt = len(fobj.readlines())
    
            fobj.close()
        return line_cnt

    except Exception as eobj:
        print(eobj)

def main():
    
    File_Name = input("Enter name of file:\n")

    Ret = CountLines(File_Name)

    print("The number of lines in file is :",Ret)


if __name__ == "__main__":
    main()