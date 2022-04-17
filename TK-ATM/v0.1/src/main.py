from tkinter import *
from tkinter import ttk
import os
import webbrowser
import time

version = "v0.1"
username = "devcrazi"
password = "tkinteratmRX"

# ACCORDING TO THE PIN NUMBER IN THE LIST THE NUMBERS BELOW WILL BE THE NUMBERS TO GO WITH THAT PIN.
pinList = ['1234', '5678', '7890', '1987', '4321']
pinBankList = [2000, 4500, 1500, 10000, 500]
pinPocketList = [1000, 250, 100, 2500, 50]

# CREATING MY ROOT WINDOW
window = Tk()
window.geometry("800x600")
window.title("TK-ATM | v0.1 PRE-ALPHA | VIRTUAL GUI ATM MACHINE")
window.configure(bg="light blue")

# ACKNOWLEDGE WARNING SCREEN BUTTON FUNCTION
def acknowledgeWarning():
	warningScreen.destroy()

# WARNING SCREEN
warningScreen = Toplevel()
warningScreen.geometry("600x300")
warningScreen.title("WARNING! THIS IS PROGRAM IS STILL IN DEVELOPEMENT!")
warningScreen.configure(bg="light blue")
warningScreenAcknoledge = ttk.Button(warningScreen, text="Acknowledge", 
									 command=acknowledgeWarning).place(x=250, y=150, width=100, height=100)

# CHANGELOG SCREEN FROM DROPDOWN MENU
def changeLog():
	changeLogScreen = Toplevel()
	changeLogScreen.title("TK-ATM v0.1 CHANGELOG")
	changeLogScreen.geometry("800x600")
	changeLogScreen.configure(bg="light blue")
	warningScreen.destroy()
	changeLogLabel = Label(changeLogScreen, font=("Tekton Pro", 11, "bold"), 
						   text="""
v0.1.0 PRE-ALPHA CHANGELOG:
TO MAKE SURE YOU ARE UP TO DATE ON THE PROGRAM. 
PLEASE CHECK MY GITHUB PAGE FOR UPDATES TO THIS PROJECT
https://www.github.com/Crazi-RX/Projects/tree/main/TK-ATM

NEW FEATURES:
- Added Main Root Screen
- Functional Button to Login Screen
- Added Warning Screen and Changelog
- Added some color to the windows.
- Added color to the buttons
- Added a drop-down menu includes 
  (About The Developer, Changelog, Special Thanks, Force Quit, Check For Updates)
- All the features in the drop-down menu works.
- Added a force quit button in drop-down menu.
- Added username and password Label and ttk.Entry to Login Screen that is functional.
- Pin Input screen added.
- Removed time.sleep() function and replaced with new working function called ".after()" on incorrect pin 
  numbers and login attempts.
- Added Check for Updates
- Added Placeholders for Transaction Screen
CHANGELOG:
- Fixed issue when .place function didn't work on positioning buttons.
- Fixed issue when .pack side attribute didn't function.
- Removed Button on Warning Screen with a replacement
- Changed Warning Screen: Warning Screen has a button if the button has been clicked. 
  You have acknowledged that you understand this program isn't finished.
- PIN Numbers changed from separate definitions to a list.
- Solved bug when logging out from transaction screen ('5678', '7890', '1987', '4321')
COMING SOON:
- Transaction screen/features
- Updated visual graphics to windows
- Functional Buttons On Check for Updates Window.
- WHEN ABOVE IS DONE: PUBLIC RELEASE v0.2!""", 
						   bg="light blue", justify="left")
	changeLogLabel.pack()
warningLabel = Label(warningScreen, text="""
	WARNING!: This program is still in development. Most features are not 
	done and the application doesn't look polished since you're seeing the 
	pre-alpha version.This is for testing purposes only. This is meant to be used 
	currently to find bugs and glitches across the GUI. Please leave an issue 
	ticket on my GitHub page about a glitch/bug you found during testing. 
	Thank you for your cooperation.""", 
	fg="red", bg="light blue", font=("Tekton Pro", 12, "bold")).place(x=-50, y=0)

def aboutDev():
	devWindow = Toplevel()
	devWindow.geometry("600x300")
	devWindow.configure(bg="light blue")
	aboutDevLabel = Label(devWindow, text="About the Developer",
						  bg="light blue", font=("Tekton Pro", 16, "bold")).pack()
	devLabelDesc = Label(devWindow, text="""
	\n 
	My name is Jacob Rogers. You must know me by Crazi-RX. I am the developer of this program.
	TK-ATM is my first major project with Tkinter. Other Tkinter projects were meant for learning.
	Most the stuff made in this program is made from scratch. I will be trying to get minimal help from
	the internet but if I do. The names that the people that helped will be in the special thanks section.
	TK-ATM is currently in the pre-alpha stage. So something's will show in the program but might be not 
	functional or have major bugs/issues. If you find some please submit a ticket on my GitHub page. 
	TK-ATM is a GUI ATM that will be able to make transactions. With up to 5 different PIN numbers 
	to choose from with different values of money that will be in the account. There will be a login 
	screen in the pre-alpha version like my PY-ATM to make people access the program itself so you 
	agree to what is behind the screen that it might be unfinished or have major bugs.""", 
	bg="light blue", justify="center").place(x=-10, y=30)
	devLabelThanks = Label(devWindow, text="\n Thanks for reading - Crazi-RX", bg="light blue",
						   font=("Tekton Pro", 15, "bold"), justify="center").place(x=150, y=250)

def forceQuit():
	quit()
		
def specialThanks():
	thanksWindow = Toplevel()
	thanksWindow.geometry("600x300")
	thanksWindow.title("Special Thanks | TK-ATM v0.1 PRE-ALPHA | GUI ATM MACHINE")
	thanksWindow.configure(bg="light blue")
	specialLabel = Label(thanksWindow, font=("Tekton Pro", 18, "bold"), 
						 text="Special Thanks to:", justify="center", bg="light blue")
	specialLabel.pack()
	thanksLabel = Label(thanksWindow, font=("Tekton Pro", 16),
						text="""
						 Codemy.com
						 stackoverflow.com
						 Python Basics
						 tutorialspoint.com""", justify="center", bg="light blue").place(x=-370, y=65)

def versionCheck():
	versionWindow = Toplevel()
	versionWindow.geometry("600x300")
	versionWindow.title("Checking for Updates...")
	versionWindow.configure(bg="light blue")
	currentVersionLabel = Label(versionWindow, text="Your current version is:",
								font=("Tekton Pro", 18, "bold"), bg="light blue").pack()
	versionLabel = Label(versionWindow, text=f"\n\n{version}", font=("Tekton Pro", 28, "bold"),
						 bg="light blue").pack()
	if version == "v0.1":
		versionWindow.title("Your up to date on TK-ATM! | TK-ATM PRE-ALPHA")
		upToDateLabel = Label(versionWindow, text="Your version is up to date!",
			  				  font=("Tekton Pro", 16, "bold"), bg="light blue").pack(side=BOTTOM)
	elif version != "v0.1":
		notUpdatedWindow = Toplevel(versionWindow)
		notUpdatedWindow.geometry("800x600")
		versionWindow.title("Version is currently out of date. | TK-ATM PRE-ALPHA")
		notUpdatedWindow.title("VERSION IS NOT UP TO DATE! | PLEASE UPDATE IT ON MY GITHUB BELOW!")
		notUpdatedWindow.configure(bg="light blue")
		notUpdatedLabel = Label(notUpdatedWindow, text="""Your version is outdated! Please Update It ASAP!""",
								bg="light blue", font=("Tekton Pro", 17, "bold")).pack(side=TOP)
		notUpdatedLabel2 = Label(notUpdatedWindow, text="\nUpdate it from the link below!:",
								 font=("Tekton Pro", 17, "bold"), bg="light blue").pack(side=TOP)
		notUpdatedLabel3 = Label(notUpdatedWindow, text="\nhttps://www.github.com/Crazi-RX/Projects/tree/main/TK-ATM/", 
								 font=("Tekton Pro", 17, "bold"), bg="light blue").pack(side=TOP)
		notUpdatedLabel4 = Label(notUpdatedWindow, text="\nClick 'Yes, take me there.' to take you to my github page to update.", 
								 font=("Tekton Pro", 17, "bold"), bg="light blue").pack(side=TOP)
		notUpdatedLabel5 = Label(notUpdatedWindow, text="\nClick 'No, keep me here' to continue using the outdated version", 
								 font=("Tekton Pro", 17, "bold"), bg="light blue").pack(side=TOP)
		def takeMeThere():
			webbrowser.open_new("https://www.github.com/Crazi-RX/Projects/tree/main/TK-ATM")
		def noKeepMeHere():
			versionWindow.destroy()
			notUpdatedWindow.destroy()
		noKeepMe = ttk.Button(notUpdatedWindow, text="No, keep me here", command=noKeepMeHere).pack(side=BOTTOM)
		takeMeThere = ttk.Button(notUpdatedWindow, text="Yes, take me there", command=takeMeThere).pack(side=BOTTOM)

winMenu = Menu(window)
window.config(menu=winMenu)
aboutMenu = Menu(winMenu, tearoff=False)
winMenu.add_cascade(label="About", menu=aboutMenu)
aboutMenu.add_command(label="Changelog", command=changeLog)
aboutMenu.add_command(label="About the Developer", command=aboutDev)
aboutMenu.add_command(label="Special Thanks", command=specialThanks)
aboutMenu.add_separator()
aboutMenu.add_command(label="Check for Updates", command=versionCheck)
aboutMenu.add_command(label="Force Quit", command=forceQuit)

def loginScreen():
	loginWindow = Toplevel()
	def returnToMain():
		window.deiconify()
		loginWindow.destroy()
	loginWindow.geometry("800x600")
	loginWindow.title("Login Screen | TK-ATM v0.1 PRE-ALPHA")
	loginWindow.configure(bg="light blue")
	userNameLabel = Label(loginWindow, text="Username", font=("Tekton Pro", 15, "bold"),
						  bg="light blue").place(x=290, y=220)
	userNameVar = StringVar()
	userName = Entry(loginWindow, justify="center", textvariable=userNameVar, font=('Arial', 15))
	userName.place(x=290, y=250)
	passWordLabel = Label(loginWindow, text="Password", font=("Tekton Pro", 15, "bold"),
						  bg="light blue").place(x=290, y=280)
	passWordVar = StringVar()
	passWord = Entry(loginWindow, show="*", textvariable=passWordVar, justify="center", font=("Arial", 15))
	passWord.place(x=290, y=310)
	def loginCommand():
		userNameInput = userNameVar.get()
		passWordInput = passWordVar.get()
		if userNameInput == username:
			if passWordInput == password:
					loginWindow.destroy()
					pinWindow = Toplevel()
					pinWindow.geometry("800x600")
					pinWindow.title("Please put in your PIN Number | TK-ATM PRE-ALPHA v0.1")
					pinWindow.configure(bg="light blue")
					pinLabel = Label(pinWindow, text="Please put in your PIN Number then hit Enter to confirm.",
							 		 bg="light blue", font=('Tekton Pro', 16, 'bold')).pack(side=TOP)
					pinVar = StringVar()
					pinEntry = Entry(pinWindow, show="*", textvariable=pinVar, justify="center", font=("Arial", 15))
					pinEntry.place(x=290, y=280)
					def confirmPIN():
						pinInput = pinVar.get()
						def returnToPIN1():
							pinWindow.deiconify()
							pin1Window.destroy()
							pinEntry.delete(0, END)
						def returnToPIN2():
							pinWindow.deiconify()
							pin2Window.destroy()
							pinEntry.delete(0, END)
						def returnToPIN3():
							pinWindow.deiconify()
							pin3Window.destroy()
							pinEntry.delete(0, END)
						def returnToPIN4():
							pinWindow.deiconify()
							pin4Window.destroy()
							pinEntry.delete(0, END)
						def returnToPIN5():
							pinWindow.deiconify()
							pin5Window.destroy()
							pinEntry.delete(0, END)
						if pinInput == pinList[0]:
							pin1Window = Toplevel()
							pin1Window.geometry("800x600")
							pin1Window.title("Welcome User! Please Choose your form of transaction | TK-ATM v0.1 PRE-ALPHA")
							pin1Window.configure(bg="light blue")
							pinWindow.withdraw()
							pinBankListLabel = Label(pin1Window, text=f"Your bank balance is {pinBankList[0]} dollars.", 
													 font=("Tekton Pro", 8, 'bold'), bg="light blue").place(x=0,y=0)
							pinPocketListLabel = Label(pin1Window, text=f"Your wallet balance is {pinPocketList[0]} dollars.",
													   font=("Tekton Pro", 8, 'bold'), bg="light blue").place(x=600, y=0)
							logOutButton = ttk.Button(pin1Window, text="Log Out", command=returnToPIN1).place(x=370, y=575)
							chooseTransactionLabel = Label(pin1Window, text="Choose your transaction form:", bg="light blue",
														   font=("Tekton Pro", 12, 'bold')).pack(side=TOP)
						elif pinInput == pinList[1]:
							pin2Window = Toplevel()
							pin2Window.geometry("800x600")
							pin2Window.title("Welcome User! Please Choose your form of transaction | TK-ATM v0.1 PRE-ALPHA")
							pin2Window.configure(bg="light blue")
							pinWindow.withdraw()
							pinBankListLabel = Label(pin2Window, text=f"Your bank balance is {pinBankList[1]} dollars.", 
													 font=("Tekton Pro", 8, 'bold'), bg="light blue").place(x=0,y=0)
							pinPocketListLabel = Label(pin2Window, text=f"Your wallet balance is {pinPocketList[1]} dollars.",
													   font=("Tekton Pro", 8, 'bold'), bg="light blue").place(x=600, y=0)
							logOutButton = ttk.Button(pin2Window, text="Log Out", command=returnToPIN2).place(x=370, y=575)
							chooseTransactionLabel = Label(pin2Window, text="Choose your transaction form:", bg="light blue",
														   font=("Tekton Pro", 12, 'bold')).pack(side=TOP)
						elif pinInput == pinList[2]:
							pin3Window = Toplevel()
							pin3Window.geometry("800x600")
							pin3Window.title("Welcome User! Please Choose your form of transaction | TK-ATM v0.1 PRE-ALPHA")
							pin3Window.configure(bg="light blue")
							pinWindow.withdraw()
							pinBankListLabel = Label(pin3Window, text=f"Your bank balance is {pinBankList[2]} dollars.", 
													 font=("Tekton Pro", 8, 'bold'), bg="light blue").place(x=0,y=0)
							pinPocketListLabel = Label(pin3Window, text=f"Your wallet balance is {pinPocketList[2]} dollars.",
													   font=("Tekton Pro", 8, 'bold'), bg="light blue").place(x=600, y=0)
							logOutButton = ttk.Button(pin3Window, text="Log Out", command=returnToPIN3).place(x=370, y=575)
							chooseTransactionLabel = Label(pin3Window, text="Choose your transaction form:", bg="light blue",
														   font=("Tekton Pro", 12, 'bold')).pack(side=TOP)
						elif pinInput == pinList[3]:
							pin4Window = Toplevel()
							pin4Window.geometry("800x600")
							pin4Window.title("Welcome User! Please Choose your form of transaction | TK-ATM v0.1 PRE-ALPHA")
							pin4Window.configure(bg="light blue")
							pinWindow.withdraw()
							pinBankListLabel = Label(pin4Window, text=f"Your bank balance is {pinBankList[3]} dollars.", 
													 font=("Tekton Pro", 8, 'bold'), bg="light blue").place(x=0,y=0)
							pinPocketListLabel = Label(pin4Window, text=f"Your wallet balance is {pinPocketList[3]} dollars.",
													   font=("Tekton Pro", 8, 'bold'), bg="light blue").place(x=600, y=0)
							logOutButton = ttk.Button(pin4Window, text="Log Out", command=returnToPIN4).place(x=370, y=575)
							chooseTransactionLabel = Label(pin4Window, text="Choose your transaction form:", bg="light blue",
														   font=("Tekton Pro", 12, 'bold')).pack(side=TOP)
						elif pinInput == pinList[4]:
							pin5Window = Toplevel()
							pin5Window.geometry("800x600")
							pin5Window.title("Welcome User! Please Choose your form of transaction | TK-ATM v0.1 PRE-ALPHA")
							pin5Window.configure(bg="light blue")
							pinWindow.withdraw()
							pinBankListLabel = Label(pin5Window, text=f"Your bank balance is {pinBankList[4]} dollars.", 
													 font=("Tekton Pro", 8, 'bold'), bg="light blue").place(x=0,y=0)
							pinPocketListLabel = Label(pin5Window, text=f"Your wallet balance is {pinPocketList[4]} dollars.",
													   font=("Tekton Pro", 8, 'bold'), bg="light blue").place(x=600, y=0)
							logOutButton = ttk.Button(pin5Window, text="Log Out", command=returnToPIN5).place(x=370, y=575)
							chooseTransactionLabel = Label(pin5Window, text="Choose your transaction form:", bg="light blue",
														   font=("Tekton Pro", 12, 'bold')).pack(side=TOP)
						else:
							def destroyWrongPinLabel():
								wrongPIN.destroy()
							wrongPIN = Label(pinWindow, text="Invalid PIN Number. Please Try Again...", bg="light blue", 
									     	 justify="center", font=("Tekton Pro", 16, 'bold'))
							wrongPIN.pack(side=BOTTOM)
							wrongPIN.after("2000", destroyWrongPinLabel)
					pinEnter = ttk.Button(pinWindow, text="Enter", command=confirmPIN).place(x=290, y=310, width=228, height=40)
			else:
				failedLabel1 = Label(loginWindow, text="Login Failed. Username/Password Incorrect.", justify="center",
									font=("Tekton Pro", 16, 'bold'), bg="light blue")
				failedLabel1.pack(side=BOTTOM)
				def destroyWrongPassword():
					failedLabel1.destroy()
				failedLabel1.after("2000", destroyWrongPassword)
		else:
			failedLabel2 = Label(loginWindow, text="Login Failed. Username/Password Incorrect.", justify="center",
								 font=("Tekton Pro", 16, 'bold'), bg="light blue")
			failedLabel2.pack(side=BOTTOM)
			def destroyWrongUsername():
				failedLabel2.destroy()
			failedLabel2.after("2000", destroyWrongUsername)
	loginButton = ttk.Button(loginWindow, text="Login", command=loginCommand).place(x=289, y=350, width=228, height=40)
	adminLabel = Label(loginWindow, text="To continue, please put in the administrator login details...", bg="light blue",
					   font=("Tekton Pro", 15, 'bold'), justify="center").pack(side=TOP)
	returnButton = ttk.Button(loginWindow, text="Return", 
							  command=returnToMain).place(x=0, y=0)
	window.withdraw()

welcomeLabel = Label(window, text="Welcome to TK-ATM!", font=("Tekton Pro", 26),
					 bg="light blue").pack()
continueLabel = Label(window, text="\n Press the continue button to enter the login screen.",
					bg="light blue", font=("Tekton Pro", 18)).pack()
continueButton = ttk.Button(window, text="Continue", 
							command=loginScreen).place(x = 350, y = 400, width=100, height=100)

mainloop()
