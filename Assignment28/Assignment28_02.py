'''
Count words in file :
    write a program which accepts a name of file name from user and counts how many
    words are present in the file
'''
import os

def CountWords(fName):
    try:
        if(os.path.exists(fName)):
            fobj = open(fName,"r") 
            
            line_cnt = len(fobj.read().split(" "))
    
            fobj.close()
        return line_cnt

    except Exception as eobj:
        print(eobj)

def main():
    
    File_Name = input("Enter name of file:\n")

    Ret = CountWords(File_Name)

    print("The number of words in file is :",Ret)


if __name__ == "__main__":
    main()