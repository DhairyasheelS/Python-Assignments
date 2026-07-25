'''
write a python program that schedules the following tasks

PrintLunch Time ! every day at 1 pm
PrintWrap up work every day at 6 pm
'''
import schedule
import time

def ScheduleTask():

    print("Namskar kar...!")

def main():
    Border = "-"*60

    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)

    schedule.every().day.at("09:00").do(ScheduleTask)
    
    while (True):
        schedule.run_pending()
        time.sleep()

if __name__ == "__main__":
    main()