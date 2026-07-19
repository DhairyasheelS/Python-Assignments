'''
Search a word in File:
    write a program which accepts a file name and word from user
    and checks whether that word is present in the file or not
'''
import os

def WordExists(fName , word):
    try:
        if(os.path.exists(fName)):
            fobj = open(fName,"r")
            
            for lines in fobj:
                words = lines.split()

                for fword in words:
                    if(fword == word):
                        print("word is present")
                        return
            print("word not found")
            return
        else:
            print("File does not exist")
    except Exception as eobj:
        print(eobj)

def main():
    
    File_Name = input("Enter name of file:\n")
    Word = input("Enter the word :\n")

    WordExists(File_Name,Word)


if __name__ == "__main__":
    main()