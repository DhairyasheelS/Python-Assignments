'''
write a python program that prints

Jay Ganesh...
every two seconds
'''
import schedule
import time

def Display():

    print("Jay Ganesh...")

def main():
    Border = "-"*60

    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)

    schedule.every(2).seconds.do(Display)
    
    while (True):
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()