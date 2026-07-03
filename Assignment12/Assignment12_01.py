# write program which accepts one character and cheks whether it is vowel or consonant

def ChkVowel(Ch):
    
    if(Ch == 'A' or Ch == 'E' or Ch == 'I' or Ch == 'O' or Ch == 'U' or 
       Ch == 'a' or Ch == 'e' or Ch == 'i' or Ch == 'o' or Ch == 'u' ) :
        return True
    else:
        return False
    
def main():
    
    Char = input("Enter your Character :\n")

    Ret = ChkVowel(Char)

    if(Ret == True):
        print("It is Vowel!!")
    else:
        print("It is Consonant!!")

if __name__ == "__main__":
    main()