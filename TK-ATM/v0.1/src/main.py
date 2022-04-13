from tkinter import *
from tkinter import ttk
import os
import webbrowser

version = "v0.1"
username = "devcrazi"
password = "tkinteratmRX"

window = Tk()
window.geometry("800x600")
window.title("TK-ATM | v0.1 ALPHA | VIRTUAL GUI ATM MACHINE")
window.configure(bg="light blue")

def acknowledgeWarning():
	warningScreen.destroy()

warningScreen = Toplevel()
warningScreen.geometry("600x300")
warningScreen.title("WARNING! THIS IS PROGRAM IS STILL IN DEVELOPEMENT!")
warningScreen.configure(bg="light blue")
warningScreenAcknoledge = ttk.Button(warningScreen, text="Acknowledge", 
									 command=acknowledgeWarning).place(x=250, y=150, width=100, height=100)
def changeLog():
	changeLogScreen = Toplevel()
	changeLogScreen.title("TK-ATM v0.1 CHANGELOG")
	changeLogScreen.geometry("800x600")
	changeLogScreen.configure(bg="light blue")
	warningScreen.destroy()
	changeLogLabel = Label(changeLogScreen, font=("Tekton Pro", 12, "bold"), 
						   text="""
NEW FEATURES:
- Added Main Root Screen
- Functional Button to Login Screen
- Added Warning Screen and Changelog
- Added some color to the windows.
- Added color to the buttons
- Added a dropdown menu includes (About The Developer, Changelog, Special Thanks)
- All the features in the dropdown menu works.
- Added a force quit button in dropdown menu.
- Added username and password Label and ttk.Entry to Login Screen (NOT FUNCTIONAL CURRENTLY)
CHANGELOG:
- Fixed issue when .place function didn't work on positioning buttons.
- Fixed issue when .pack side attribute didn't function.
- Removed Button on Warning Screen with a replacement
- Changed Warning Screen: Warning Screen has a button if the button has been clicked.
  You have acknowledged that you understand this program isn't finished.
COMING SOON:
- Functional Login Screen
- Pin input screen
- Transaction screen/features
- Updated visual graphics to windows
- Version check menu to dropdown menu.
- WHEN ABOVE IS DONE: PUBLIC RELEASE v0.2!""", 
						   bg="light blue", justify="left")
	changeLogLabel.pack()
warningLabel = Label(warningScreen, text="""
	WARNING!: This program is still in developement. Most features are not 
	done and the application doesn't look polished since you're seeing the 
	alpha version.This is for testing purposes only. This is meant to be used 
	currently to find bugs and glitches across the GUI. Please leave an issue 
	ticket on my GitHub page about a glitch/bug you found during testing. 
	Thank you for your cooporation.""", 
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
	TK-ATM is currently in the alpha stage. So something's will show in the program but might be not 
	functional or have major bugs/issues. If you find some please submit a ticket on my GitHub page. 
	TK-ATM is a GUI ATM that will be able to make transactions. With up to 10 different PIN numbers 
	to choose from with different values of money that will be in the account. There will be a login 
	screen in the alpha version like my PY-ATM to make people access the program itself so you 
	agree to what is behind the screen that it might be unfinished or have major bugs.""", 
	bg="light blue", justify="center").place(x=-10, y=30)
	devLabelThanks = Label(devWindow, text="\n Thanks for reading - Crazi-RX", bg="light blue",
						   font=("Tekton Pro", 15, "bold"), justify="center").place(x=150, y=250)

def forceQuit():
	window.destroy()
		
def specialThanks():
	thanksWindow = Toplevel()
	thanksWindow.geometry("600x300")
	thanksWindow.title("Special Thanks | TK-ATM v0.1 ALPHA | GUI ATM MACHINE")
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
	versionLabel = Label(versionWindow, text="\n\nv0.1", font=("Tekton Pro", 28, "bold"),
						 bg="light blue").pack()
	if version == "v0.1":
		versionWindow.title("Your up to date on TK-ATM! | TK-ATM ALPHA")
		upToDateLabel = Label(versionWindow, text="\n\nYour version is up to date!",
			  font=("Tekton Pro", 16, "bold"), bg="light blue").pack()
	elif version != "v0.1":
		notUpdatedWindow = Toplevel(versionWindow)
		notUpdatedWindow.geometry("800x600")
		versionWindow.title("Version is currently out of date. | TK-ATM ALPHA")
		notUpdatedWindow.title("VERSION IS NOT UP TO DATE! | PLEASE UPDATE IT ON MY GITHUB BELOW!")
		notUpdatedWindow.configure(bg="light blue")
		notUpdatedLabel = Label(notUpdatedWindow, text="""Your version is outdated! Please Update It ASAP!""",
								bg="light blue", font=("Tekton Pro", 17, "bold")).pack(side=TOP)
		notUpdatedLabel2 = Label(notUpdatedWindow, text="\nUpdate it from the link below!:", 
								 font=("Tekton Pro", 17, "bold"), bg="light blue").pack(side=TOP)
		notUpdatedLabel3 = Label(notUpdatedWindow, text="\nhttps://www.github.com/Crazi-RX/Projects/TK-ATM/", 
								 font=("Tekton Pro", 17, "bold"), bg="light blue").pack(side=TOP)
		notUpdatedLabel4 = Label(notUpdatedWindow, text="\nClick 'Yes, take me there.' to take you to my github page to update.", 
								 font=("Tekton Pro", 17, "bold"), bg="light blue").pack(side=TOP)
		notUpdatedLabel5 = Label(notUpdatedWindow, text="\nClick 'No, keep me here' to continue using the outdated version", 
								 font=("Tekton Pro", 17, "bold"), bg="light blue").pack(side=TOP)
		takeMeThere = ttk.Button(notUpdatedWindow, text="Yes, take me there").pack(side=BOTTOM)
		noKeepMe = ttk.Button(notUpdatedWindow, text="No, keep me here").pack(side=BOTTOM)

winMenu = Menu(window)
window.config(menu=winMenu)
aboutMenu = Menu(winMenu, tearoff=False)
winMenu.add_cascade(label="About", menu=aboutMenu)
aboutMenu.add_command(label="Changelog", command=changeLog)
aboutMenu.add_command(label="About the Developer", command=aboutDev)
aboutMenu.add_command(label="Special Thanks", command=specialThanks)
aboutMenu.add_command(label="Check for Updates", command=versionCheck)
aboutMenu.add_command(label="Force Quit", command=forceQuit)

def loginScreen():
	loginWindow = Toplevel()
	def returnToMain():
		window.deiconify()
		loginWindow.destroy()
	loginWindow.geometry("800x600")
	loginWindow.title("Login Screen | TK-ATM v0.1 ALPHA")
	loginWindow.configure(bg="light blue")
	def loginInput():
		userNameInput = userName.get("1.0", "end-1c")
		passWordInput = passWord.get("1.0", "end-1c")
	userNameLabel = Label(loginWindow, text="Username", font=("Tekton Pro", 15, "bold"),
						  bg="light blue").place(x=290, y=220)
	userName = ttk.Entry(loginWindow, justify="center", font=('Arial', 15)).place(x=290, y=250)
	passWordLabel = Label(loginWindow, text="Password", font=("Tekton Pro", 15, "bold"),
						  bg="light blue").place(x=290, y=280)
	passWord = ttk.Entry(loginWindow, show="*", justify="center", font=("Arial", 15)).place(x=290, y=310)
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
