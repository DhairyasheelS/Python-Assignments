'''
write a program which accept one number and display below pattern
'''
def Display(No):

    for icnt in range(1,No+1):
        for jcnt in range(1,No+1):
            print(jcnt,end=" ")
        print()

def main():
    Display(5)

if __name__ == "__main__":
    main()