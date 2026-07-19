'''
Frequency of string in File:
    write a program which accepts file name and one string from user and return the frequency 
    of string in the file
'''
import os
import sys

def CountFrequency(fName , fword):
    cnt = 0
    try:
        if (os.path.exists(fName)):
            fobj = open(fName , "r")

            for line in fobj:
                for word in line.split():
                    if(word == fword):
                        cnt = cnt + 1
            return cnt

        else:
            print("Files does not exist")        
        
    except Exception as eobj:
        print(eobj)

def main():

    File_Name = input("Enter name of file:\n")
    Value = input("Enter word for frequency:\n")

    Ret = CountFrequency(File_Name,Value)

    print(f"Frequency of {Value} in {File_Name} is : {Ret} ")

if __name__ == "__main__":
    main()