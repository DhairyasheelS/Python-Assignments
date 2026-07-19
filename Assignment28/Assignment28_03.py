'''
Display File Line by Line :
    write a program which accepts a name of file name from user and counts how many
    words are present in the file
'''
import os

def DisplayFile(fName):
    try:
        if(os.path.exists(fName)):
            fobj = open(fName,"r") 
            
            Data = fobj.readlines()
            print(Data)
            
            fobj.close()
        

    except Exception as eobj:
        print(eobj)

def main():
    
    File_Name = input("Enter name of file:\n")

    DisplayFile(File_Name)


if __name__ == "__main__":
    main()