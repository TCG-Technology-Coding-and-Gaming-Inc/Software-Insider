import os
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
import tkinter.ttk
import psutil
import random
from tkinter import font
#import sound
global oemsetupdetectharddriveformattedornot
oemsetupdetectharddriveformattedornot = False
def cdrom():
    partitions = psutil.disk_partitions(all=True)
    for partition in partitions:
        if 'cdrom' in partition.opts:
            return True
    return False
def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    return
def boot(bootdevice):
    print("BIOS Version 2.7.18 - © Okmeque1 Corporation 1981-2079")
    print("Model No : SDESK 300VS")
    print("64144KB OK")
    print("CPU : intel Pentium(R) III 1.00 GhZ")
    print("Detecting IDE-0...",end="\r")
    time.sleep(0.5)
    print("Detecting IDE-0...HGST IC25N030ATCS04-0 30GB")
    print("Detecting IDE-1...",end="\r")
    if cdrom() == True:
        time.sleep(0.31)
        print("Detecting IDE-1...Logitec LDR-E4242AK")
    else:
        time.sleep(5)
        print("Detecting IDE-1...Not found.")
    print("Initializing devices...Done")
    bios = input("Press ENTER to enter BIOS or B for BOOT Menu, else hit any key and press enter")
    if bootdevice == "CDROM":
        setupstart()
    if bootdevice == "DEBUG":
        realsetup()
def setupstart():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    print("Microsoft Windows 98 Startup Menu")
    print("==================================")
    print("1 : Start SETUP from CD-ROM")
    print("2 : Start computer with CD-ROM support")
    print("3 : Start computer into DOS shell")
    sch = int(input("Please select : "))
    if sch == 3:
        pass
    #elif sch != 1 or sch != 2 or sch != 3:
        #setupstart()
    elif sch == 1 or sch == 2:
        print("Okmeque1 Computers ™ - IDE CD-ROM Drivers")
        print("Initializing CD-ROM, please wait...",end="\r")
        fdcd = False
        res = cdrom()
        if res == True:
            time.sleep(3)
            fdcd = True
            print("Initializing CD-ROM, please wait...Done!")
            print("Device name : CDS310-OKCD001")
            print("Interface : Programmed I/O")
            print("Drive Letter : D:")
        else:
            time.sleep(7)
            print("Initializing CD-ROM, please wait...Failed")
            print("No CD-ROM Found. Attempting to load the SCSI driver, please wait...")
        time.sleep(0.31)
        print("Okmeque1 Computers ™ - SCSI Drivers")
        if fdcd == True:
            print("CD-ROM Driver previously loaded. Aborting...")
            time.sleep(0.5)
        else:
            print("Attempting to load a SCSI CD-ROM Device. If you have an external drive, make sure that its cable is terminated properly.")
            time.sleep(7)
            print("No CD-ROM found. Installation will now abort...")
        print("Scanning PCI Bus using Mechanism #1",end="\r")
        time.sleep(0.1)
        print("Scanning PCI Bus using Mechanism #2",end="\r")
        time.sleep(0.1)   
        print("PCI Bus scan complete.                                     ")  
        print("Loading additional VIDEO and MOUSE Drivers. This may take up to a couple of minutes...")
        time.sleep(9)
        if sch == 1 and res == True:
            oemsetup()
def oemsetup():
    global oemsetupdetectharddriveformattedornot
    if oemsetupdetectharddriveformattedornot == True:
        clear()
        print("Okmeque1 Computers ™ - Windows 98 SETUP")
        print("=======================================")
        input("Setup must now check your hard drive for data errors and integrity.Whenever you're ready, press ENTER")
        for x in range(101):
            print("Checking drive : " + str(x) + "% Complete.",end="\r")
            time.sleep(0.24)
        input("Setup has completed the disk check and is now ready going to setup. Whenever you're ready, press ENTER")
        realsetup()
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    print("Okmeque1 Computers ™ - Windows 98 SETUP")
    print("=======================================")    
    print("To SETUP your computer NOW, press ENTER")
    print("For more information, press 1 and press ENTER")
    print("To exit, hit any key and press ENTER")
    optionoemsetup = input("Choice : ")
    if optionoemsetup == "":
        clear()
        print("Okmeque1 Computers ™ - Windows 98 SETUP")
        print("=======================================")
        print("Setup has detected that your hard drive is not formatted nor partitioned. Setup can do both of those thing. You must FORMAT and PARTITION the hard drive before being able to use it.")
        formatornot = input("Would you like to format your hard drive[Y/any other to exit]? ")
        if formatornot == "Y":
                    print("Partitioning hard drive...Done!")
                    clear()
                    print("Okmeque1 Computers ™ - Windows 98 SETUP")
                    print("=======================================")
                    print("SETUP is now formatting your hard drive...")
                    for x in range(101):
                        print("Formatting : " + str(x) + "% Complete.",end="\r")
                        time.sleep(random.uniform(0.31,3))
                    oemsetupdetectharddriveformattedornot = True
                    input("Setup needs to restart your computer for all partitioning changes to be visible to the computer. Whenever you're ready, press ENTER")
                    clear()
                    boot("CDROM")
def copyfiles(directory):
    global windows
    confirm = messagebox.askyesno("Windows 98 Setup - Caution Notice","You are about to irreversibly change your computer. If you have important files on your hard drive, press NO and back them up. Otherwise press YES",icon=messagebox.WARNING)
    if confirm == True:
            def update_progress(i):
                prgval.set(i)
                if i < 100:
                    windows.after(5000, update_progress, i + 1)
            prgval = IntVar()
            print(1)
            copyyay = Label(windows,text="Copying files. This will be slower if you have a low-end computer",bg="#016699")
            print(2)
            copyyay.place(x=220,y=510)
            print(3)
            prgbar = Progressbar(variable=prgval,length=450)
            print(4)
            prgbar.place(x=185,y=530)
            print(5)
            prgbar["maximum"] = 100
            update_progress(0)

def setupclean():
    global windows
    for wi in windows.winfo_children():
        wi.destroy()
    l3 = Label(windows,text="Windows must select a directory to install to. You can choose \Win or other as you wish. To select, press the according button.",bg="#016699")
    l3.pack()
    b4 = Button(windows,text="I want to use the \Win directory.",command=lambda: copyfiles(""),bg="aqua")
    b4.pack()
    b5 = Button(windows,text="I want to use another directory.",bg="#30D5C8")
    b5.pack()
def realsetup():
    global oemsetupdetectharddriveformattedornot
    global windows
    windows = Tk()
    windows.title("Windows 98 Setup - Okmeque1 Computer OEM Recovery disc")
    windows.geometry("800x680")
    windows.configure(bg="#016699")
    windows.deiconify()
    ft = font.Font(family="Consolas",size=3)
    l1 = Label(windows,text="Windows 98 Setup - Recovery",bg="#016699")
    l1.pack()
    l2 = Label(windows,text="Welcome to the Okmeque1 Computer recovery CD. To start, press an option.",bg="#016699")
    l2.pack()
    b1 = Button(windows,text="Install Windows 98 Clean",width=40,background="aqua",activebackground="#016699",command=setupclean)
    b1.pack()
    b2 = Button(windows,text="Install Windows 98 WITHOUT modifying files")
    b2.pack()
    b3 = Button(windows,text="Quit setup.")
    windows.mainloop()
boot("DEBUG")