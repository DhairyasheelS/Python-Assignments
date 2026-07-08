'''
Design a python application that creates two seprate threads named
Even and Odd.
'''

import threading as th

def DisplayEven(No):
    print("Even Numbers :")
    for cnt in range(2,No+1,2):
        print(cnt)

def DisplayOdd(No):
    print("Odd Numbers :")
    for cnt in range(1,No,2):
        print(cnt)

def main():
    
   t1 = th.Thread(target=DisplayEven, args=(20,))
   t2 = th.Thread(target=DisplayOdd , args=(20,))

   t1.start()
   t2.start()
 
   t1.join()
   t2.join() 

if __name__ == "__main__":
    main()