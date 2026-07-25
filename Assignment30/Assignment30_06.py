'''
write a script that schedules the following tasks:
    PrintLunch Time! every day at 1:00 Pm

'''

import schedule
import time

def LunchTime():

    print("Lunch Time!")

def WrapUp():

    print("Wrap up work!")

def main():
    
    Border = "-"*60
    
    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)

    schedule.every().day.at("13:00").do(LunchTime)
    schedule.every().day.at("18:00").do(WrapUp)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()