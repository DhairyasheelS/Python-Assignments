'''
write a program which display 10 to 1 on screen
'''
def Display():
    
    for cnt in range(10,0,-1):
        print(cnt , end=" ")
        
        
def main():
    
    Display()
if __name__ == "__main__":
    main()