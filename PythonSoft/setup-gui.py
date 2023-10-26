"""Instructions for Okmeque1 : 
1 : Use IDE-0 when wanting to boot from harddrive if not rebooting from GUI SETUP
2 : have the ISO or CD and mount the CDROM with the image first for convenience
3 : have PSUTIL


                                                """

import os
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import filedialog
import psutil
import random
from tkinter import font
from tkinter import simpledialog
global oemsetupdetectharddriveformattedornot
oemsetupdetectharddriveformattedornot = False
global hdpart
hdpart = {"partition":True}
def cdrom():
    partitions = psutil.disk_partitions(all=True)
    for partition in partitions:
        if 'cdrom' in partition.opts:
            return partition.device
    return False
def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    return
def boot(bootdevice):
    clear()
    if bootdevice == "HDD0":
        windows.withdraw()
    print("BIOS Version 2.7.18 - © Okmeque1 Corporation 1981-2079")
    print("Model No : SDESK 300VS")
    print("64144KB OK")
    print("CPU : intel Pentium(R) III 1.00 GhZ")
    print("Detecting IDE-0...",end="\r")
    time.sleep(0.5)
    print("Detecting IDE-0...HGST IC25N030ATCS04-0 30GB")
    print("Detecting IDE-1...",end="\r")
    if cdrom() != False:
        time.sleep(0.31)
        print("Detecting IDE-1...Logitec LDR-E4242AK")
    else:
        time.sleep(5)
        print("Detecting IDE-1...Not found.")
    print("Initializing devices...Done")
    bios = input("Press any key then ENTER to enter BIOS or B for BOOT Menu, else press enter")
    if bios == "B" or bios == "b":
        clear()
        print("Okmeque1 Computers Inc - © Okmeque1 Corporation 1981-2079")
        print("BOOT MENU")
        print("=========================================================")
        print("[1] -> Legacy diskette A: WINVERIFY")
        print("[2] -> Legacy diskette B: (unknown)")
        print("[3] -> IDE-0 HGST IC25N030ATCS04-0 30GB")
        if cdrom() != False:
            print("[4] -> IDE-1 Logitec LDR-E4242AK")
        else:
            print("[4] -> IDE-1 (unknown)")
        print("[5] -> ROM BIOS")
        boots = int(input("Please choose an option : "))
        if boots == 1:
            boot("FDD0")
        elif boots == 2:
            print("Searching for boot record on Legacy diskette B:...",end='\r')
            time.sleep(10)
            print("Searching for boot record on Legacy diskette B:...Not found.",end='\r')
            print("Boot failure")
            print("Insert system disk in A:")
            input("Press ENTER when ready")
            boot("FDD0")
    if bootdevice == "CDROM":
        nevermind()
    elif bootdevice == "DEBUG":
        realsetup()
    elif bootdevice == "Hackintosh HD":
        wininit()
    elif bootdevice == "HDD0" or bootdevice == "IDE-0":
        hdboot()
def dosnocdrom():
    while True:
        prompt = input("A:>")
        prompt = prompt.lower()
        if prompt == "dir":
            print("Directory of A:")
            print("")
            print("AUTOEXEC BAT   462")
            print("CONFIG   SYS   389")
            print("TPCD     SYS 15232")
            print("EXTRACT  EXE 93242")
            print("HIMEM    SYS 33191")
            print("FDISK    EXE 63916")
            print("FINDCD   EXE  8009")
            print("SCSICD   SYS 33612")
            print("JO       SYS  2048")
            print("9 File(s) 250101 Bytes")
            print("         1226507B Free")
            print("Disk is write protected.")
        elif "autoexec" in prompt:
            print("Okmeque1 Computers ™ - IDE CD-ROM Drivers")
            print("Initializing CD-ROM, please wait...",end="\r")
            fdcd = False
            res = cdrom()
            if res != False:
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
            if fdcd == True:
                pass #doswithcdrom()
            else:
                clear()
                print("The Windows 98 Setup Files were not found.")
        elif prompt == "extract" or prompt == "extract.exe":
            print("Microsoft Extraction Utility V1.00")
            print("Cabinet name not specified.")
            print("/E - Extract from cabinet - Usage - extract.exe /E C:\DIR")
            print("/C - Compress to cabinet ")
            print("No cabinets on A: - Program disabled.")
        elif "findcd" in prompt or "findcd.exe" in prompt:
            pass
        elif prompt == 'fdisk' or prompt == 'fdisk.exe':
            trueagain = True
            clear()
            while trueagain == True:
                global hdpart
                print("        Microsoft Windows 98          ")
                print("      Fixed Disk Setup Program        ")
                print("(C)Copyright Microsoft Corp. 1983-1999")
                print("")
                print("       FDISK Options")
                print("Current number of fixed disks : 1")
                print("\nChoose one of the following\n")
                print("1 : Create DOS partition or logical DOS drive")
                print("2 : Set active partition")
                print("3 : Delete partition or logical DOS drive")
                print("4 : Display partition information")
                fdiskinput = int(input("Enter choice[any other option to abort] : "))
                if fdiskinput == 1:
                    clear()
                    print("      Create DOS partition or Logical drive")
                    print("Curent Fixed Disk Drives : 1")
                    print("1 : Create Primary DOS partition")
                    print("2 : Create extended DOS partition")
                    print("3 : Create logical drive")
                    dinput = int(input("Enter Choice : "))
                    if dinput == 1:
                        clear()
                        print("         Create DOS partition or Logical Drive")
                        if hdpart["partition"] == True:
                                print("Current Fixed Disk 1:")
                                print("Partition    Status    Type    Volume Label    Mbytes    System    Usage")
                                print("C:  1        Active    PRI DOS HGST-WIN98SE    32767     FAT32     UNKNOWN")
                                print("\n\n\n\n")
                                print("Primary DOS partition already exists!")
                                input("Press ENTER to continue")
                                clear()
                        else:
                            clear()
                            print("System will now restart.\nInsert DOS diskette in drive A")
                            input("Press ENTER to continue")
                            hdpart["partition"] = True
                            trueagain = False
                            clear()
                            boot("CDROM")
                elif fdiskinput == 2:
                    clear()
                    if hdpart["partition"] == True:
                        print("             Set Active Partition")
                        print("Partition    Status    Type    Volume Label    Mbytes    System    Usage")
                        print("C:  1        Active    PRI DOS HGST-WIN98SE    32767     FAT32     UNKNOWN")
                        print("\n\n\nThe only startable partition on this disk is already set as active")
                        input("Press ENTER to continue")
                        clear()
                    else:
                        print("            Set Active Partiiton")
                        print("\n\n\nNo partitions defined\nNo partitions to make active")
                        input("Press ENTER to continue")
                        clear()
def wininit():
    global windows
    windows = Tk()
    windows.geometry("800x680")
    windows.title("Windows 98 Setup")
    windows.configure(bg="#016699")
    hdboot()
def hdboot():
    clear()
    global windows
    if hdpart["partition"] != True:
        input("Invalid system disk\nReplace the disk and strike enter key when ready.")
        boot("CDROM")
    windows.deiconify()
    badchar = "¬!£$%^&*(){@}~#'[]\|,./<>?"
    askpcname = simpledialog.askstring("Setup","Enter a valid computer name(Only characters and digits as well as '-','_','=','+' are allowed)")
    if askpcname == None:
        hdboot()
    chars = "1234567890QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm-=_+"
    for char in askpcname:
        for badchars in badchar:
            if badchars == char:
                x = messagebox.showerror("Windows Setup Message SU530C","Your computer name has an invalid character. Please try again.")
                hdboot()
    username = simpledialog.askstring("Setup","Enter a username : ")
    try:
        fstring ="C:\\User"
        users = "Users"
        os.mkdir(fstring)
        os.chdir(fstring)
        os.mkdir(users)
        os.chdir(users)
        os.mkdir(username)
    except PermissionError:
        x = messagebox.showerror("Fatal Error","Access violation at address 0x000001E82DFC3E20 in module SETUP.EXE. Read of address 0FFFFFFF")
        x = messagebox.showerror("Setup","A critical error has prevented SETUP from creating the required files. Please disable ANY and ALL anti-viruses as they may be interfering with the SETUP process.\nMake sure to also disable BIOS settings that restrics access to the BOOTLOADER.\n\nSetup will now exit to DOS.")
    except BaseException:
        x = messagebox.showerror("Fatal Error","Setup failed to create the user folder and cannot continue. Click on OK to terminate the SETUP. Your computer will restart")
        boot("CDROM")
    while True:
        winkey = "ZF3R0-FHED2-M80TY-8QYGC-NPKYF"
        askkey = simpledialog.askstring("Setup","Enter your Windows Product Key. It is a 25 character long code located at the back of the CD-ROM case or on a special boot floppy disk. The format must be 'XXXXX-XXXXX-XXXXX-XXXXX-XXXXX'.")
        askkey = askkey.upper()
        if askkey == winkey:
            break
        else:
            x = messagebox.showerror("Setup","The Product Key you entered is not valid.")

def nevermind():
    clear()
    print("Microsoft Windows 98 Startup Menu")
    print("=================================")
    print("1 : Boot from hard disk")
    print("2 : Boot from CD-ROM")
    a = int(input("Please select : "))
    valid = [1,2]
    if a == 1:
        boot("IDE-0")
    elif a == 2:
        clear(); setupstart()
    else:
        nevermind()
def setupstart():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    valid = [1,2,3]
    print("Microsoft Windows 98 Startup Menu")
    print("==================================")
    print("1 : Start SETUP from CD-ROM")
    print("2 : Start computer with CD-ROM support")
    print("3 : Start computer into DOS shell")
    sch = int(input("Please select : "))
    if sch == 3:
        dosnocdrom()
    elif sch == 1 or sch == 2:
        print("Okmeque1 Computers ™ - IDE CD-ROM Drivers")
        print("Initializing CD-ROM, please wait...",end="\r")
        fdcd = False
        res = cdrom()
        if res != False:
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
        if sch == 1 and res != False:
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
        clear()
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

def restart():
    l1 = Label(windows,text="SETUP has just copied the files to your computer. In order for the computer to see them, we must restart.\n Whenever you're ready, press RESTART or wait until the progressbar reaches the end.",bg="#016699")
    l1.pack()
    b1 = Button(windows,text="Restart Now",command=lambda: boot("HDD0"),bg="aqua")
    b1.pack()
    pval = IntVar()
    pbar = Progressbar(maximum=100,length=450,variable=pval)
    pbar.pack()
    def update_progress(i):
        pval.set(i)
        if i < 100:
            windows.after(100, update_progress, i + 1)
        else:
            windows.withdraw()
            clear()
            boot("HDD0")
    update_progress(0)
def copyfiles(directory,fromm):
    global windows
    confirm = messagebox.askyesno("Windows 98 Setup - Caution Notice","You are about to irreversibly change your computer. If you have important files on your hard drive, press NO and back them up. Otherwise press YES",icon=messagebox.WARNING)
    if confirm == True:
            for wi in windows.winfo_children():
                wi.destroy()
            def update_progress(i):
                    tim = 100
                    global l1
                    tosets = ["Welcome to the World of Windows\n\nThank you for choosing Windows 98\nCongratulations for choosing Windows 98, the software that makes your computer more   powerful, reliable, manageable and entertaining.\nWith Windows 98, you can connect to the Internet quickly and easily. And, Windows 98 is easier to use than Windows 95","With Okmeque1 Computers, you can get a fast experience with your computer. The          software that comes with your computer is made for you and for ease of use.","Windows 98 has added hardware improvement and is lightweight so that most Windows   95 computers can run it.\n Plug and play support makes it even easier for you to use your computer as you don't      need to install any software from a CD-ROM.\nJust plug the device in and refresh and your new hardware will be detected","USB Support has now been added so that you can use new USB devices with your          computer. Install the driver from the manufacturer CD-ROM and your device should work.","Thank you for choosing Windows 98 and Okmeque1 Computers.\n\nPlease register your copy."]
                    if i < 20:
                        l1.config(state="normal")
                        l1.delete("1.0",END)
                        l1.insert(END,tosets[0])
                        l1.config(state="disabled")
                        prgval.set(i)
                        if i < 100:
                            windows.after(tim, update_progress, i + 1)
                    elif i < 40:
                        l1.config(state="normal")
                        l1.delete("1.0",END)
                        l1.insert(END,tosets[1])
                        l1.config(state="disabled")
                        prgval.set(i)
                        if i < 100:
                            windows.after(tim, update_progress, i + 1)
                    elif i < 60:
                        l1.config(state="normal")
                        l1.delete("1.0",END)
                        l1.insert(END,tosets[2])
                        l1.config(state="disabled")
                        prgval.set(i)
                        if i < 100:
                            windows.after(tim, update_progress, i + 1)
                    elif i < 80:
                        l1.config(state="normal")
                        l1.delete("1.0",END)
                        l1.insert(END,tosets[3])
                        l1.config(state="disabled")
                        prgval.set(i)
                        if i < 100:
                            windows.after(tim, update_progress, i + 1)
                    elif i < 99:
                        l1.config(state="normal")
                        l1.delete("1.0",END)
                        l1.insert(END,tosets[4])
                        l1.config(state="disabled")
                        prgval.set(i)
                        if i < 100:
                            windows.after(tim, update_progress, i + 1)
                    elif i == 100:
                        for wi in windows.winfo_children():
                            wi.destroy()
                        restart()
                    else:
                        windows.after(tim,update_progress,i + 1)
            prgval = IntVar()
            toset = ""
            global l1
            l1 = Text(windows,height=20,width=90,bg="#016699",state="disabled",font=("Arial", 15))
            l1.pack()
            prgbar = Progressbar(variable=prgval,length=450)
            prgbar.pack()
            copyyay = Label(windows,text="Copying files. This will be slower if you have a low-end computer",bg="#016699")
            copyyay.pack()
            try:
                os.mkdir(directory)
            except FileExistsError:
                pass
            try:
                firstcmd = fromm + os.sep + "UNPACK"
                print(firstcmd)
                lastcmd = "xcopy *.* " + directory + "/E /I /Q /Y"
                os.chdir(firstcmd)
                os.system(lastcmd)
                a = os.listdir(firstcmd)
                prgbar["maximum"] = 100
                update_progress(0)
            except FileNotFoundError:
                x = messagebox.askretrycancel("Windows 98 Setup - Okmeque1 Computers","Please insert the correct CD-ROM and press RETRY or press CANCEL to download the image file.",icon=messagebox.ERROR)
                

def setupclean(wherefrom):
    global windows
    for wi in windows.winfo_children():
        wi.destroy()
    l3 = Label(windows,text="Windows must select a directory to install to. You can choose \Win or other as you wish. To select, press the according button.",bg="#016699")
    l3.pack()
    b4 = Button(windows,text="I want to use the \Win directory.",command=lambda: copyfiles("C:\WIN",wherefrom),bg="aqua")
    b4.pack()
    b5 = Button(windows,text="I want to use another directory.",bg="#30D5C8")
    b5.pack()
def realsetup():
    global oemsetupdetectharddriveformattedornot
    global windows
    windows = Tk()
    windows.title("Windows 98 Setup - Okmeque1 Computer OEM Recovery CD")
    windows.geometry("800x680")
    windows.configure(bg="#016699")
    if os.name != "nt":
        x = messagebox.showerror("Windows 98 Setup - Recovery","Your computer is not compatible and/or does not meet the minimum system requirements. Change your hardware and try again. If you have an anti-virus on your computer, you may want to disable it before running SETUP")
    while True:
        os.chdir(cdrom())
        if os.path.exists("UNPACK") == False:
            wrongcddetect = messagebox.askyesno("Windows 98 Setup","SETUP has detected that you have the wrong CD-ROM in the drive. To continue with the existing drive, please insert the CORRECT CD in the drive and press YES or press NO to install from another location",icon=messagebox.INFO)
            if wrongcddetect == True:
                pass
            else:
                try:
                    otherloc = filedialog.askdirectory()
                    os.chdir(otherloc)
                    if os.path.exists("UNPACK") == False:
                        pass
                    break
                except OSError:
                    x = messagebox.showerror("Windows 98 Setup","The folder that you have selected is not readable, is invalid or is corrupted. Please choose another folder.")
                    pass
                except BaseException:
                    x = messagebox.showerror("Windows 98 Setup","An error has occured. Please try again")
                    pass
        else:
            otherloc = cdrom()
            break
    windows.deiconify()
    ft = font.Font(family="Consolas",size=3)
    l1 = Label(windows,text="Windows 98 Setup - Recovery",bg="#016699")
    l1.pack()
    l2 = Label(windows,text="Welcome to the Okmeque1 Computer Recovery CD. To start, press an option.",bg="#016699")
    l2.pack()
    b1 = Button(windows,text="Install Windows 98 Clean",width=40,background="aqua",activebackground="#016699",command=lambda: setupclean(otherloc))
    b1.pack()
    b2 = Button(windows,text="Install Windows 98 WITHOUT modifying files")
    b2.pack()
    b3 = Button(windows,text="Quit setup.",command=exit)
    b3.pack()
    windows.mainloop()
boot("Hackintosh HD")
