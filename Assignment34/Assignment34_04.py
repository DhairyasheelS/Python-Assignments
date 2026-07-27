'''
Design automation script which accept directory name and mail id from user and create
log file in that directory which contains information of running processes as its name, PID, username.
After creating log files send that log file to specified mail
'''

import psutil
import sys
import os
import time
import schedule

import smtplib
from email.message import EmailMessage
import mimetypes
import platform

def send_mail(sender, app_password, receiver, subject, body, html_body, AttachmentPath):

    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    msg.set_content(body)
    msg.add_alternative(html_body, subtype="html")

    with open(AttachmentPath, "rb") as f:
        file_data = f.read()

    mime_type, _ = mimetypes.guess_type(AttachmentPath)

    if mime_type:
        maintype, subtype = mime_type.split("/")
    else:
        maintype, subtype = "application", "octet-stream"

    msg.add_attachment(file_data,
                       maintype=maintype,
                       subtype=subtype,
                       filename=os.path.basename(AttachmentPath))

    try:
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

        smtp.login(sender, app_password)

        smtp.send_message(msg)

        smtp.quit()

        print("Email Sent Successfully!")

    except Exception as eobj:
        print("Email Sent unsucessful!")
        print(eobj)

def ProcessScan():
    listprocess = list()

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid", "name", "username"])
        listprocess.append(info)

    return listprocess

def PlatformSurvillence(DirectoryName, sender, app_password, receiver, subject):
    Border = "-"*50

    Ret = os.path.exists(DirectoryName)

    if(Ret == True):
        Ret = os.path.isdir(DirectoryName)

        if(Ret == False):
            print("Unable to proceed as directory name exists but its not a directory")
            return
    else:
        os.mkdir(DirectoryName)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(DirectoryName, "Marvellous_%s.log" % timestamp)

    fobj = open(FileName, "w")

    fobj.write(Border+"\n")
    fobj.write("----- Marvellous Running Process Report Script -----\n")
    fobj.write(f"Log File gets created at : {timestamp}\n")
    fobj.write(Border+"\n\n")

    fobj.write("----------- System Report ------------\n")

    # Process Log
    Data = ProcessScan()

    for info in Data:
        fobj.write("PID         : %s\n" % (info.get("pid")))
        fobj.write("Name        : %s\n" % (info.get("name")))
        fobj.write("Username    : %s\n" % (info.get("username")))
        fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("---------- End of Log File -------------\n")
    fobj.write(Border+"\n")

    fobj.close()

    ReadableTime = time.strftime("%d %B %Y, %I:%M %p")
    TotalProcess = len(Data)
    MachineName  = platform.node()
    OSName       = f"{platform.system()} {platform.release()}"
    FileSizeKB   = round(os.path.getsize(FileName) / 1024, 2)

    body = f"""Marvellous Process Report

Hello,

Your scheduled system process report has been generated successfully.

Generated On   : {ReadableTime}
Machine Name   : {MachineName}
Operating System: {OSName}
Total Processes: {TotalProcess}
Log File       : {os.path.basename(FileName)} ({FileSizeKB} KB)

The complete report is attached with this mail.

This is an automated mail. Please do not reply.
Marvellous Automation Suite
"""

    html_body = f"""
<html>
  <body style="margin:0; padding:0; background-color:#f4f6f8; font-family:Segoe UI, Arial, sans-serif;">
    <table width="100%" cellpadding="0" cellspacing="0" style="background-color:#f4f6f8; padding:30px 0;">
      <tr>
        <td align="center">
          <table width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; border-radius:10px; overflow:hidden; box-shadow:0 2px 8px rgba(0,0,0,0.08);">

            <!-- Header -->
            <tr>
              <td style="background-color:#1f3c88; padding:28px 30px;" align="center">
                <h1 style="margin:0; color:#ffffff; font-size:22px; font-weight:600; letter-spacing:0.5px;">
                  Marvellous Automation Suite
                </h1>
                <p style="margin:6px 0 0 0; color:#c3d0f0; font-size:13px;">
                  Running Process Report
                </p>
              </td>
            </tr>

            <!-- Greeting -->
            <tr>
              <td style="padding:30px 30px 10px 30px;">
                <p style="margin:0 0 12px 0; color:#1f2937; font-size:16px; font-weight:600;">Hello,</p>
                <p style="margin:0; color:#4b5563; font-size:14px; line-height:22px;">
                  Your scheduled system surveillance report has been generated successfully.
                  A summary is given below and the complete log file is attached with this mail.
                </p>
              </td>
            </tr>

            <!-- Summary table -->
            <tr>
              <td style="padding:20px 30px;">
                <table width="100%" cellpadding="0" cellspacing="0" style="border:1px solid #e5e7eb; border-radius:8px;">
                  <tr>
                    <td style="padding:12px 16px; background-color:#f9fafb; color:#6b7280; font-size:13px; border-bottom:1px solid #e5e7eb; width:45%;">Generated On</td>
                    <td style="padding:12px 16px; color:#111827; font-size:13px; font-weight:600; border-bottom:1px solid #e5e7eb;">{ReadableTime}</td>
                  </tr>
                  <tr>
                    <td style="padding:12px 16px; background-color:#f9fafb; color:#6b7280; font-size:13px; border-bottom:1px solid #e5e7eb;">Machine Name</td>
                    <td style="padding:12px 16px; color:#111827; font-size:13px; font-weight:600; border-bottom:1px solid #e5e7eb;">{MachineName}</td>
                  </tr>
                  <tr>
                    <td style="padding:12px 16px; background-color:#f9fafb; color:#6b7280; font-size:13px; border-bottom:1px solid #e5e7eb;">Operating System</td>
                    <td style="padding:12px 16px; color:#111827; font-size:13px; font-weight:600; border-bottom:1px solid #e5e7eb;">{OSName}</td>
                  </tr>
                  <tr>
                    <td style="padding:12px 16px; background-color:#f9fafb; color:#6b7280; font-size:13px; border-bottom:1px solid #e5e7eb;">Total Processes</td>
                    <td style="padding:12px 16px; color:#1f3c88; font-size:13px; font-weight:700; border-bottom:1px solid #e5e7eb;">{TotalProcess}</td>
                  </tr>
                  <tr>
                    <td style="padding:12px 16px; background-color:#f9fafb; color:#6b7280; font-size:13px;">Attached Log File</td>
                    <td style="padding:12px 16px; color:#111827; font-size:13px; font-weight:600;">{os.path.basename(FileName)} &nbsp;<span style="color:#6b7280; font-weight:400;">({FileSizeKB} KB)</span></td>
                  </tr>
                </table>
              </td>
            </tr>

            <!-- Note -->
            <tr>
              <td style="padding:0 30px 25px 30px;">
                <div style="background-color:#eef2ff; border-left:4px solid #1f3c88; padding:14px 16px; border-radius:4px;">
                  <p style="margin:0; color:#374151; font-size:13px; line-height:20px;">
                    The attached log file contains the <strong>PID</strong>, <strong>Name</strong> and
                    <strong>Username</strong> of every process running on the machine at the time of the scan.
                  </p>
                </div>
              </td>
            </tr>

            <!-- Footer -->
            <tr>
              <td style="background-color:#f9fafb; padding:20px 30px; border-top:1px solid #e5e7eb;" align="center">
                <p style="margin:0 0 6px 0; color:#6b7280; font-size:12px;">
                  This is an automated mail generated by the Marvellous Automation Suite. Please do not reply.
                </p>
                <p style="margin:0; color:#9ca3af; font-size:11px;">
                  &copy; {time.strftime("%Y")} Marvellous Automation Suite
                </p>
              </td>
            </tr>

          </table>
        </td>
      </tr>
    </table>
  </body>
</html>
"""

    send_mail(sender, app_password, receiver, subject, body, html_body, FileName)

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
            print("It creates log file in given directory and")
            print("sends the process report through email periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as :")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name Receiver_Email")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Folder_Name : Name of folder for the log file creation")
            print("Receiver_Email : Email address on which report gets delivered")

        else:
            print("Unable to proceed as there is no matching argument")
            print("please use --h or --u flag for getting more details")

    # Actual project code
    elif(len(sys.argv) == 4):

        Sender = "xyz@gmail.com"
        app_password = "xxxx xxxx xxxx xxxx"
        DirectoryName = sys.argv[2]
        receiver = sys.argv[3]
        subject = "Process Report"

        print("Schedular Started Sucessfully!!")
        print("press ctrl + C to abort the automation script")

        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillence, DirectoryName, Sender, app_password, receiver, subject)

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