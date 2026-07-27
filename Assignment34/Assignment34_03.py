'''
Design automation script which display information of running processes as 
its name, PID, Username
'''
import psutil
import sys
import os 
import time
import schedule

def ProcessScan():
    listprocess = list()

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username"])
        listprocess.append(info)

    return listprocess

def PlatformSurvillence(DirectoryName):
    Border = "-"*50

    Ret = False

    Ret = os.path.exists(DirectoryName)

    if(Ret == True):

        Ret = os.path.isdir(DirectoryName)

        if(Ret == False):
            print("Unable to proceed as directory name exists but its not a directory")
            return

    else:
        os.mkdir(DirectoryName)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(DirectoryName,"Marvellous_%s"%timestamp)

    fobj = open(FileName, "w")

    fobj.write(Border+"\n")
    fobj.write("----- Marvellous Running Process Report Script -----\n")
    fobj.write(f"Log File gets created at : {timestamp}\n")
    fobj.write(Border+"\n\n")

    fobj.write("----------- System Report ------------\n")


    #Process Log
    Data = ProcessScan()

    for info in Data:

        fobj.write("PID         : %s\n"%(info.get("pid")))
        fobj.write("Name        : %s\n"%(info.get("name")))
        fobj.write("Username    : %s\n"%(info.get("username")))

        fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("---------- End of Log File -------------\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():
    Border = "-"*50
    print(Border)
    print("----- Marvellous Running Process Report Script -----")
    print(Border)

    #--h and --u
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("this automation script is used to perform")
            print("It fetch the information of running process")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as :")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Folder_Name : Name of folder for the log file creation")
            
        else:
            print("Unable to proceed as there is no matching argument")
            print("please use --h or --u flag for getting more details")

    # Actual project code
    elif(len(sys.argv) == 3):

        print("Schedular Started Sucessfully!!")
        print("press ctrl + C to abort the automation script")

        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillence,sys.argv[2])

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Number of arguments")
        print("Unable to proceed as arguments are not matching")
        print("please use --h or --u flag for getting more details")

    print(Border)
    print("---- Thank you for using our automation system----")
    print(Border)

if __name__ == "__main__":
    main()