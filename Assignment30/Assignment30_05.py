'''
schedule a task that executes every five minutes
the task should write the current date and time into file named:
    Marvellous.txt

'''

import schedule
import time

def ScheduledTask():

    fobj = open("Marvellous.txt","a")

    
    fobj.write(f"Task Executed at :{time.ctime()}\n")

    print("Task Executed!")
    
    fobj.close()

def main():

    Border = "-"*60
    
    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)

    schedule.every(1).minute.do(ScheduledTask)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()