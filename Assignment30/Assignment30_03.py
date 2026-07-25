'''
write a python program that schedules a function to print

'''
import schedule
import time

def Display():

    print("Coding Kar...!")

def main():
    Border = "-"*60

    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)

    schedule.every(30).minute.do(Display)
    
    while (True):
        schedule.run_pending()
        time.sleep(10)


if __name__ == "__main__":
    main()