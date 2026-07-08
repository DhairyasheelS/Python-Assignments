'''
write a program which accept one number and display below pattern
'''
def Display(No):

    for cnt in range(No):
        print("* "*No ,end="\n")

def main():
    Display(5)

if __name__ == "__main__":
    main()