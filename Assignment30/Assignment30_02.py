'''
write a python program that Displays the current date and time
after every one minute

'''
import schedule
import time

def CurrentDateTime():

    print("Current Date and Time :",time.ctime())

def main():
    Border = "-"*60

    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)

    schedule.every(1).minute.do(CurrentDateTime)
    
    while (True):
        schedule.run_pending()
        time.sleep(10)


if __name__ == "__main__":
    main()