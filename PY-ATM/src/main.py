import time
import os
def clearWindow():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    else:
        command = 'clear'
    os.system(command)
def changeWindowName():
    command = 'gconftool-2 --set /apps/gnome-terminal/profiles/Default/title --type=string "PY-ATM v0.2 | ATM MACHINE ALPHA"'
    if os.name in ('nt', 'dos'):
        command = 'title PY-ATM v0.2 | ATM MACHINE ALPHA'
    os.system(command)
changeWindowName()
changeLog = input("Would you like to see the Changelog?: (y/n)")
if changeLog == "y":
    print("""V0.2.1 UPDATE! 
BUG FIXES:
- Fixed Bug when Limit is exceeded on Deposit or Withdraw beyond the Bank Account limit or Pocket Change Limit
- Fixed Bug when user accepts the Changelog and automatically quits the application.
- Fixed Bug when user types letters into a deposit input or withdrawal input and causes the application to quit.
- Currently working on preventing the Pocket Change and Bank Account integers from going into negatives.
- Fixed performance issues on other devices (Linux)
- Tweaked program to help with performance issues on Windows or MacOS.
CHANGELOG:
- Changed messages after transactions.
- Changed locations in the code for clearWindow() function.
- Changed idents of welcome messages, changelog, terms and conditions for sleek look.
NEW FEATURES:
- Added changeWindowName() function. If you have linux. Make sure you install gconftool. Make sure you run the command first to see if you have 
  it installed.
- Developer Mode Added! Developer mode is when you can access a menu and add money to bank balance Pocket balance. Find out how to access it and 
  have fun with Developer Features!
- Check wallet feature added to Dev Mode and Guest Mode!
- Added MacOS support to the program with clearWindow() feature.
COMING SOON:
- Installer, EXE file, seperate files for different outcomes in application.""")
    print("""
Terms and Conditions
This program will not store private info. This is a fake atm and will not store
any actual PIN numbers or usernames and passwords.""")
    
    TOS = input("Do you accept terms and conditions?: (y/n)")
    if TOS == "y":
        clearWindow()
        print("""
888       888 8888888888 888      .d8888b.   .d88888b.  888b     d888 8888888888 
888   o   888 888        888     d88P  Y88b d88P" "Y88b 8888b   d8888 888        
888  d8b  888 888        888     888    888 888     888 88888b.d88888 888        
888 d888b 888 8888888    888     888        888     888 888Y88888P888 8888888    
888d88888b888 888        888     888        888     888 888 Y888P 888 888        
88888P Y88888 888        888     888    888 888     888 888  Y8P  888 888        
8888P   Y8888 888        888     Y88b  d88P Y88b. .d88P 888   "   888 888        
888P     Y888 8888888888 88888888 "Y8888P"   "Y88888P"  888       888 8888888888                                                                                   
                                                                                         """)
        print("""
********************************************************************************
*                                                                              *
*                                 WELCOME TO                                   *
*                                   PY-ATM                                     *
*                                                                              *
********************************************************************************""")
        bankBalance = 2500
        pocketBalance = 200
        PIN1 = 1234
        PIN2 = 5678
        PIN3 = 1987
        PIN4 = 7890
        PIN5 = 5254
        print("Welcome To PY-ATM! ALPHA v0.2")
        time.sleep(3)
        print("Guest cannot access ATM in it's alpha state.")
        time.sleep(2)
        userInput = input("Please input Admin Username to Continue: ")
        if userInput == "devcrazi":
            passInput = input("Please input a password: ")
            if passInput == "pyatmdevcrazi3716":
                print("Access Granted!")
                time.sleep(1.5)
                clearWindow()
                pinInput = int(input("Insert your PIN to continue: "))
                if pinInput == PIN1:
                    print("Pin accepted")
                    time.sleep(2)
                    clearWindow()
                    while True:
                        print("1. Withdrawal")
                        print("2. Deposit")
                        print("3. Check Balance")
                        print("4. Check Wallet")
                        print("5. Sign Out")
                        time.sleep(1)
                        atmChoice = input("Input the number of your choice: ")
                        if atmChoice == "1":
                            drawalInput = int(input(f"How much do you want to withdraw? You have {bankBalance}: "))
                            if drawalInput > bankBalance:
                                print("This transaction is greater than your balance")
                            bankBalance = bankBalance - drawalInput
                            pocketBalance = pocketBalance + drawalInput
                            print(f"You have {pocketBalance} dollars in your pocket.")
                            print(f"You have {bankBalance} remaining.")
                            print("Thanks for Choosing PYATM!")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "2":
                            depositInput = int(input("How much do you want to deposit?: "))
                            if depositInput > pocketBalance:
                                print("This transaction is greater than your balance.")
                            else:
                                pocketBalance = pocketBalance - depositInput
                                bankBalance = bankBalance + depositInput
                                print(f"You now have {bankBalance} dollars.")
                                print(f"You now have {pocketBalance} in your pocket.")
                                time.sleep(2)
                                clearWindow()
                        elif atmChoice == "3":
                            print(f"You have {bankBalance} dollars in your account.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "4":
                            print(f"You throughly looked through your wallet and counted {pocketBalance} dollars.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "5":
                            print("Thanks for Choosing PYATM! See you next time!")
                            time.sleep(2)
                            print("Closing Application in...")
                            time.sleep(1)
                            print("3")
                            time.sleep(1)
                            print("2")
                            time.sleep(1)
                            print("1")
                            time.sleep(1)
                            exit()
                        elif atmChoice == "devcrazi":
                            print("DEVELOPER MODE ACCESSED!")
                            time.sleep(2)
                            clearWindow()
                            while True:
                                print("1. Withdrawal")
                                print("2. Deposit")
                                print("3. Check Balance")
                                print("4. Add Money To Pocket")
                                print("5. Add Money To Bank Account")
                                print("6. Sign Out")
                                print("7. Check Wallet")
                                time.sleep(1)
                                atmChoice = input("Input the number of your choice: ")
                                if atmChoice == "1":
                                    drawalInput = int(input(f"How much do you want to withdraw? You have {bankBalance}: "))
                                    if drawalInput > bankBalance:
                                        print("This transaction is greater than your balance")
                                    bankBalance = bankBalance - drawalInput
                                    pocketBalance = pocketBalance + drawalInput
                                    print(f"You have {pocketBalance} dollars in your pocket.")
                                    print(f"You have {bankBalance} remaining.")
                                    time.sleep(2)
                                    clearWindow()
                                elif atmChoice == "2":
                                    depositInput = int(input("How much do you want to deposit?: "))
                                    if depositInput > pocketBalance:
                                        print("This transaction is greater than your balance.")
                                    else:
                                        pocketBalance = pocketBalance - depositInput
                                        bankBalance = bankBalance + depositInput
                                        print(f"You now have {bankBalance} dollars.")
                                        print(f"You now have {pocketBalance} in your pocket.")
                                        time.sleep(2)
                                        clearWindow()
                                elif atmChoice == "3":
                                    print(f"You have {bankBalance} dollars in your account.")
                                    time.sleep(2)
                                    clearWindow()
                                elif atmChoice == "4":
                                    addMoneyPocket = int(input("How much money do you want to add?: "))
                                    pocketBalance = pocketBalance + addMoneyPocket
                                    print(f"Funds have been added to your account! Spend it wisely! You have {pocketBalance}!")
                                    time.sleep(3)
                                    clearWindow()
                                elif atmChoice == "5":
                                    addMoneyBank = int(input("How much money you want to add to bank?: "))
                                    bankBalance = bankBalance + addMoneyBank
                                    print(f"Funds have been added to your account! Spend it wisely! You have {bankBalance}!")
                                    time.sleep(3)
                                    clearWindow()
                                elif atmChoice == "6":
                                    print("Thanks for Choosing PYATM! See you next time!")
                                    time.sleep(2)
                                    print("Closing Application in...")
                                    time.sleep(1)
                                    print("3")
                                    time.sleep(1)
                                    print("2")
                                    time.sleep(1)
                                    print("1")
                                    time.sleep(1)
                                    exit()
                                elif atmChoice == "7":
                                    print(f"You opened your wallet. You count and remark {pocketBalance} dollars in your wallet.")
                                    time.sleep(2)
                                    clearWindow()
                                else:
                                    print("Invalid Input! Closing Application...")
                                    time.sleep(3)
                                    exit()
                        else:
                            print("Invalid Input! Closing Application...")
                            time.sleep(3)
                            exit()
                elif pinInput == PIN2:
                    print("Pin Accepted!")
                    time.sleep(2)
                    clearWindow()
                    while True:
                        print("1. Withdrawal")
                        print("2. Deposit")
                        print("3. Check Balance")
                        print("4. Check Wallet")
                        print("5. Sign Out")
                        time.sleep(1)
                        atmChoice = input("Input the number of your choice: ")
                        if atmChoice == "1":
                            drawalInput = int(input(f"How much do you want to withdraw? You have {bankBalance}: "))
                            if drawalInput > bankBalance:
                                print("This transaction is greater than your balance")
                            bankBalance = bankBalance - drawalInput
                            pocketBalance = pocketBalance + drawalInput
                            print(f"You have {pocketBalance} dollars in your pocket.")
                            print(f"You have {bankBalance} remaining.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "2":
                            depositInput = int(input("How much do you want to deposit?: "))
                            if depositInput > pocketBalance:
                                print("This transaction is greater than your balance.")
                            else:
                                pocketBalance = pocketBalance - depositInput
                                bankBalance = bankBalance + depositInput
                                print(f"You have {pocketBalance} dollars in your pocket.")
                                print(f"You have {bankBalance} remaining.")
                                print("Thanks for Choosing PYATM!")
                                time.sleep(2)
                                clearWindow()
                        elif atmChoice == "3":
                            print(f"You have {bankBalance} dollars in your account.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "4":
                            print(f"You throughly looked through your wallet and counted {pocketBalance} dollars.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "5":
                            print("Thanks for Choosing PYATM! See you next time!")
                            time.sleep(2)
                            print("Closing Application in...")
                            time.sleep(1)
                            print("3")
                            time.sleep(1)
                            print("2")
                            time.sleep(1)
                            print("1")
                            time.sleep(1)
                            exit()
                        elif atmChoice == "devcrazi":
                            print("DEVELOPER MODE ACCESSED!")
                            time.sleep(2)
                            clearWindow()
                            while True:
                                print("1. Withdrawal")
                                print("2. Deposit")
                                print("3. Check Balance")
                                print("4. Add Money To Pocket")
                                print("5. Add Money To Bank Account")
                                print("6. Sign Out")
                                print("7. Check Wallet")
                                time.sleep(1)
                                atmChoice = input("Input the number of your choice: ")
                                if atmChoice == "1":
                                    drawalInput = int(input(f"How much do you want to withdraw? You have {bankBalance}: "))
                                    if drawalInput > bankBalance:
                                        print("This transaction is greater than your balance")
                                    bankBalance = bankBalance - drawalInput
                                    pocketBalance = pocketBalance + drawalInput
                                    print(f"You have {pocketBalance} dollars in your pocket.")
                                    print(f"You have {bankBalance} remaining.")
                                    time.sleep(2)
                                    clearWindow()
                                elif atmChoice == "2":
                                    depositInput = int(input("How much do you want to deposit?: "))
                                    if depositInput > pocketBalance:
                                        print("This transaction is greater than your balance.")
                                    else:
                                        pocketBalance = pocketBalance - depositInput
                                        bankBalance = bankBalance + depositInput
                                        print(f"You now have {bankBalance} dollars.")
                                        print(f"You now have {pocketBalance} in your pocket.")
                                        time.sleep(2)
                                        clearWindow()
                                elif atmChoice == "3":
                                    print(f"You have {bankBalance} dollars in your account.")
                                    time.sleep(2)
                                    clearWindow()
                                elif atmChoice == "4":
                                    addMoneyPocket = int(input("How much money do you want to add?: "))
                                    pocketBalance = pocketBalance + addMoneyPocket
                                    print(f"Funds have been added to your account! Spend it wisely! You have {pocketBalance}!")
                                    time.sleep(3)
                                    clearWindow()
                                elif atmChoice == "5":
                                    addMoneyBank = int(input("How much money you want to add to bank?: "))
                                    bankBalance = bankBalance + addMoneyBank
                                    print(f"Funds have been added to your account! Spend it wisely! You have {bankBalance}!")
                                    time.sleep(3)
                                    clearWindow()
                                elif atmChoice == "6":
                                    print("Thanks for Choosing PYATM! See you next time!")
                                    time.sleep(2)
                                    print("Closing Application in...")
                                    time.sleep(1)
                                    print("3")
                                    time.sleep(1)
                                    print("2")
                                    time.sleep(1)
                                    print("1")
                                    time.sleep(1)
                                    exit()
                                elif atmChoice == "7":
                                    print(f"You opened your wallet. You count and remark {pocketBalance} dollars in your wallet.")
                                    time.sleep(2)
                                    clearWindow()
                                else:
                                    print("Invalid Input! Closing Application...")
                                    time.sleep(3)
                                    exit()
                        else:
                            print("Invalid Input! Closing Application...")
                            time.sleep(3)
                            exit()
                elif pinInput == PIN3:
                    print("Pin Accepted!")
                    time.sleep(2)
                    clearWindow()
                    while True:
                        print("1. Withdrawal")
                        print("2. Deposit")
                        print("3. Check Balance")
                        print("4. Check Wallet")
                        print("5. Sign Out")
                        time.sleep(1)
                        atmChoice = input("Input the number of your choice: ")
                        if atmChoice == "1":
                            drawalInput = int(input(f"How much do you want to withdraw? You have {bankBalance}: "))
                            if drawalInput > bankBalance:
                                print("This transaction is greater than your balance")
                            bankBalance = bankBalance - drawalInput
                            pocketBalance = pocketBalance + drawalInput
                            print(f"You have {pocketBalance} dollars in your pocket.")
                            print(f"You have {bankBalance} remaining.")
                            print("Thanks for Choosing PYATM!")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "2":
                            depositInput = int(input("How much do you want to deposit?: "))
                            if depositInput > pocketBalance:
                                print("This transaction is greater than your balance.")
                            else:
                                pocketBalance = pocketBalance - depositInput
                                bankBalance = bankBalance + depositInput
                                print(f"You now have {bankBalance} dollars.")
                                print(f"You now have {pocketBalance} in your pocket.")
                                time.sleep(2)
                                clearWindow()
                        elif atmChoice == "3":
                            print(f"You have {bankBalance} dollars in your account.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "4":
                            print(f"You throughly looked through your wallet and counted {pocketBalance} dollars.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "5":
                            print("Thanks for Choosing PYATM! See you next time!")
                            time.sleep(2)
                            print("Closing Application in...")
                            time.sleep(1)
                            print("3")
                            time.sleep(1)
                            print("2")
                            time.sleep(1)
                            print("1")
                            time.sleep(1)
                            exit()
                        elif atmChoice == "devcrazi":
                            print("DEVELOPER MODE ACCESSED!")
                            time.sleep(2)
                            clearWindow()
                            while True:
                                print("1. Withdrawal")
                                print("2. Deposit")
                                print("3. Check Balance")
                                print("4. Add Money To Pocket")
                                print("5. Add Money To Bank Account")
                                print("6. Sign Out")
                                print("7. Check Wallet")
                                time.sleep(1)
                                atmChoice = input("Input the number of your choice: ")
                                if atmChoice == "1":
                                    drawalInput = int(input(f"How much do you want to withdraw? You have {bankBalance}: "))
                                    if drawalInput > bankBalance:
                                        print("This transaction is greater than your balance")
                                    bankBalance = bankBalance - drawalInput
                                    pocketBalance = pocketBalance + drawalInput
                                    print(f"You have {pocketBalance} dollars in your pocket.")
                                    print(f"You have {bankBalance} remaining.")
                                    time.sleep(2)
                                    clearWindow()
                                elif atmChoice == "2":
                                    depositInput = int(input("How much do you want to deposit?: "))
                                    if depositInput > pocketBalance:
                                        print("This transaction is greater than your balance.")
                                    else:
                                        pocketBalance = pocketBalance - depositInput
                                        bankBalance = bankBalance + depositInput
                                        print(f"You now have {bankBalance} dollars.")
                                        print(f"You now have {pocketBalance} in your pocket.")
                                        time.sleep(2)
                                        clearWindow()
                                elif atmChoice == "3":
                                    print(f"You have {bankBalance} dollars in your account.")
                                    time.sleep(2)
                                    clearWindow()
                                elif atmChoice == "4":
                                    addMoneyPocket = int(input("How much money do you want to add?: "))
                                    pocketBalance = pocketBalance + addMoneyPocket
                                    print(f"Funds have been added to your account! Spend it wisely! You have {pocketBalance}!")
                                    time.sleep(3)
                                    clearWindow()
                                elif atmChoice == "5":
                                    addMoneyBank = int(input("How much money you want to add to bank?: "))
                                    bankBalance = bankBalance + addMoneyBank
                                    print(f"Funds have been added. Enjoy with your money! You have {bankBalance}!")
                                    time.sleep(3)
                                    clearWindow()
                                elif atmChoice == "6":
                                    print("Thanks for Choosing PYATM! See you next time!")
                                    time.sleep(2)
                                    print("Closing Application in...")
                                    time.sleep(1)
                                    print("3")
                                    time.sleep(1)
                                    print("2")
                                    time.sleep(1)
                                    print("1")
                                    time.sleep(1)
                                    exit()
                                elif atmChoice == "7":
                                    print(f"You opened your wallet. You count and remark {pocketBalance} dollars in your wallet.")
                                    time.sleep(2)
                                    clearWindow()
                                else:
                                    print("Invalid Input! Closing Application...")
                                    time.sleep(3)
                                    exit()
                        else:
                            print("Invalid Input! Closing Application...")
                            time.sleep(3)
                            exit()
                elif pinInput == PIN4:
                    print("Pin Accepted!")
                    time.sleep(2)
                    clearWindow()
                    while True:
                        print("1. Withdrawal")
                        print("2. Deposit")
                        print("3. Check Balance")
                        print("4. Check Wallet")
                        print("5. Sign Out")
                        time.sleep(1)
                        atmChoice = input("Input the number of your choice: ")
                        if atmChoice == "1":
                            drawalInput = int(input(f"How much do you want to withdraw? You have {bankBalance}: "))
                            if drawalInput > bankBalance:
                                print("This transaction is greater than your balance")
                            bankBalance = bankBalance - drawalInput
                            pocketBalance = pocketBalance + drawalInput
                            print(f"You have {pocketBalance} dollars in your pocket.")
                            print(f"You have {bankBalance} remaining.")
                            print("Thanks for Choosing PYATM!")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "2":
                            depositInput = int(input("How much do you want to deposit?: "))
                            if depositInput > pocketBalance:
                                print("This transaction is greater than your balance.")
                            else:
                                pocketBalance = pocketBalance - depositInput
                                bankBalance = bankBalance + depositInput
                                print(f"You now have {bankBalance} dollars.")
                                print(f"You now have {pocketBalance} in your pocket.")
                                time.sleep(2)
                                clearWindow()
                        elif atmChoice == "3":
                            print(f"You have {bankBalance} dollars in your account.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "4":
                            print(f"You throughly looked through your wallet and counted {pocketBalance} dollars.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "5":
                            print("Thanks for Choosing PYATM! See you next time!")
                            time.sleep(2)
                            print("Closing Application in...")
                            time.sleep(1)
                            print("3")
                            time.sleep(1)
                            print("2")
                            time.sleep(1)
                            print("1")
                            time.sleep(1)
                            exit()
                        elif atmChoice == "devcrazi":
                            print("DEVELOPER MODE ACCESSED!")
                            time.sleep(2)
                            clearWindow()
                            while True:
                                print("1. Withdrawal")
                                print("2. Deposit")
                                print("3. Check Balance")
                                print("4. Add Money To Pocket")
                                print("5. Add Money To Bank Account")
                                print("6. Sign Out")
                                print("7. Check Wallet")
                                time.sleep(1)
                                atmChoice = input("Input the number of your choice: ")
                                if atmChoice == "1":
                                    drawalInput = int(input(f"How much do you want to withdraw? You have {bankBalance}: "))
                                    if drawalInput > bankBalance:
                                        print("This transaction is greater than your balance")
                                    bankBalance = bankBalance - drawalInput
                                    pocketBalance = pocketBalance + drawalInput
                                    print(f"You have {pocketBalance} dollars in your pocket.")
                                    print(f"You have {bankBalance} remaining.")
                                    time.sleep(2)
                                    clearWindow()
                                elif atmChoice == "2":
                                    depositInput = int(input("How much do you want to deposit?: "))
                                    if depositInput > pocketBalance:
                                        print("This transaction is greater than your balance.")
                                    else:
                                        pocketBalance = pocketBalance - depositInput
                                        bankBalance = bankBalance + depositInput
                                        print(f"You now have {bankBalance} dollars.")
                                        print(f"You now have {pocketBalance} in your pocket.")
                                        time.sleep(2)
                                        clearWindow()
                                elif atmChoice == "3":
                                    print(f"You have {bankBalance} dollars in your account.")
                                    time.sleep(2)
                                    clearWindow()
                                elif atmChoice == "4":
                                    addMoneyPocket = int(input("How much money do you want to add?: "))
                                    pocketBalance = pocketBalance + addMoneyPocket
                                    print(f"Funds have been added to your account! Spend it wisely! You have {pocketBalance}!")
                                    time.sleep(3)
                                    clearWindow()
                                elif atmChoice == "5":
                                    addMoneyBank = int(input("How much money you want to add to bank?: "))
                                    bankBalance = bankBalance + addMoneyBank
                                    print(f"Funds have been added to your account! Spend it wisely! You have {bankBalance}!")
                                    time.sleep(3)
                                    clearWindow()
                                elif atmChoice == "6":
                                    print("Thanks for Choosing PYATM! See you next time!")
                                    time.sleep(2)
                                    print("Closing Application in...")
                                    time.sleep(1)
                                    print("3")
                                    time.sleep(1)
                                    print("2")
                                    time.sleep(1)
                                    print("1")
                                    time.sleep(1)
                                    exit()
                                elif atmChoice == "7":
                                    print(f"You opened your wallet. You count and remark {pocketBalance} dollars in your wallet.")
                                    time.sleep(2)
                                    clearWindow()
                                else:
                                    print("Invalid Input! Closing Application...")
                                    time.sleep(3)
                                    exit()
                    else:
                        print("Invalid Input! Closing Application...")
                        time.sleep(3)
                        exit()
                elif pinInput == PIN5:
                    print("Pin Accepted!")
                    time.sleep(2)
                    while True:
                        print("1. Withdrawal")
                        print("2. Deposit")
                        print("3. Check Balance")
                        print("4. Check Wallet")
                        print("5. Sign Out")
                        time.sleep(1)
                        atmChoice = input("Input the number of your choice: ")
                        if atmChoice == "1":
                            drawalInput = int(input(f"How much do you want to withdraw? You have {bankBalance}: "))
                            if drawalInput > bankBalance:
                                print("This transaction is greater than your balance")
                            bankBalance = bankBalance - drawalInput
                            pocketBalance = pocketBalance + drawalInput
                            print(f"You have {pocketBalance} dollars in your pocket.")
                            print(f"You have {bankBalance} remaining.")
                            print("Thanks for Choosing PYATM!")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "2":
                            depositInput = int(input("How much do you want to deposit?: "))
                            if depositInput > pocketBalance:
                                print("This transaction is greater than your balance.")
                            else:
                                pocketBalance = pocketBalance - depositInput
                                bankBalance = bankBalance + depositInput
                                print(f"You now have {bankBalance} dollars.")
                                print(f"You now have {pocketBalance} in your pocket.")
                                time.sleep(2)
                                clearWindow()
                        elif atmChoice == "3":
                            print(f"You have {bankBalance} dollars in your account.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "4":
                            print(f"You throughly looked through your wallet and counted {pocketBalance} dollars.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "5":
                            print("Thanks for Choosing PYATM! See you next time!")
                            time.sleep(2)
                            print("Closing Application in...")
                            time.sleep(1)
                            print("3")
                            time.sleep(1)
                            print("2")
                            time.sleep(1)
                            print("1")
                            time.sleep(1)
                            exit()
                        elif atmChoice == "devcrazi":
                            print("DEVELOPER MODE ACCESSED!")
                            time.sleep(2)
                            clearWindow()
                            while True:
                                print("1. Withdrawal")
                                print("2. Deposit")
                                print("3. Check Balance")
                                print("4. Add Money To Pocket")
                                print("5. Add Money To Bank Account")
                                print("6. Sign Out")
                                print("7. Check Wallet")
                                time.sleep(1)
                                atmChoice = input("Input the number of your choice: ")
                                if atmChoice == "1":
                                    drawalInput = int(input(f"How much do you want to withdraw? You have {bankBalance}: "))
                                    if drawalInput > bankBalance:
                                        print("This transaction is greater than your balance")
                                    bankBalance = bankBalance - drawalInput
                                    pocketBalance = pocketBalance + drawalInput
                                    print(f"You have {pocketBalance} dollars in your pocket.")
                                    print(f"You have {bankBalance} remaining.")
                                    time.sleep(2)
                                    clearWindow()
                                elif atmChoice == "2":
                                    depositInput = int(input("How much do you want to deposit?: "))
                                    if depositInput > pocketBalance:
                                        print("This transaction is greater than your balance.")
                                    else:
                                        pocketBalance = pocketBalance - depositInput
                                        bankBalance = bankBalance + depositInput
                                        print(f"You now have {bankBalance} dollars.")
                                        print(f"You now have {pocketBalance} in your pocket.")
                                        time.sleep(2)
                                        clearWindow()
                                elif atmChoice == "3":
                                    print(f"You have {bankBalance} dollars in your account.")
                                    time.sleep(2)
                                    clearWindow()
                                elif atmChoice == "4":
                                    addMoneyPocket = int(input("How much money do you want to add?: "))
                                    pocketBalance = pocketBalance + addMoneyPocket
                                    print(f"Funds have been added! Spend it wisely! You have {pocketBalance}!")
                                    time.sleep(3)
                                    clearWindow()
                                elif atmChoice == "5":
                                    addMoneyBank = int(input("How much money you want to add to bank?: "))
                                    bankBalance = bankBalance + addMoneyBank
                                    print(f"Funds have been added to your account! Spend it wisely! You have {bankBalance}!")
                                    time.sleep(3)
                                    clearWindow()
                                elif atmChoice == "6":
                                    print("Thanks for Choosing PYATM! See you next time!")
                                    time.sleep(2)
                                    print("Closing Application in...")
                                    time.sleep(1)
                                    print("3")
                                    time.sleep(1)
                                    print("2")
                                    time.sleep(1)
                                    print("1")
                                    time.sleep(1)
                                    exit()
                                elif atmChoice == "7":
                                    print(f"You opened your wallet. You count and remark {pocketBalance} dollars in your wallet.")
                                    time.sleep(2)
                                    clearWindow()
                                else:
                                    print("Invalid Input! Closing Application...")
                                    time.sleep(3)
                                    exit()
                        else:
                            print("Invalid Input! Closing Application...")
                            time.sleep(3)
                            exit()
                else:
                    print("PIN Invalid!")
                    exit()
        else:
            print("Incorrect Administrator Username. Quitting Application.")
            exit()
    else:
        exit()
else:
    print("""Terms and Conditions
          This program will not store private info. This is a fake atm and will not store
          any actual PIN numbers or usernames and passwords.""")
    TOS = input("Do you accept terms and conditions?: (y/n)")
    if TOS == "y":
        clearWindow()
        print("""
        888       888 8888888888 888      .d8888b.   .d88888b.  888b     d888 8888888888 
        888   o   888 888        888     d88P  Y88b d88P" "Y88b 8888b   d8888 888        
        888  d8b  888 888        888     888    888 888     888 88888b.d88888 888        
        888 d888b 888 8888888    888     888        888     888 888Y88888P888 8888888    
        888d88888b888 888        888     888        888     888 888 Y888P 888 888        
        88888P Y88888 888        888     888    888 888     888 888  Y8P  888 888        
        8888P   Y8888 888        888     Y88b  d88P Y88b. .d88P 888   "   888 888        
        888P     Y888 8888888888 88888888 "Y8888P"   "Y88888P"  888       888 8888888888 
                                                                                         """)
        print("""
        ********************************************************************************
        *                                                                              *
        *                                 WELCOME TO                                   *
        *                                   PY-ATM                                     *
        *                                                                              *
        ********************************************************************************""")
        bankBalance = 2500
        pocketBalance = 200
        PIN1 = 1234
        PIN2 = 5678
        PIN3 = 1987
        PIN4 = 7890
        PIN5 = 5254
        print("Welcome To PY-ATM! ALPHA v0.2")
        time.sleep(3)
        print("Guest cannot access ATM in it's alpha state.")
        time.sleep(2)
        userInput = input("Please input Admin Username to Continue: ")
        if userInput == "devcrazi":
            passInput = input("Please input a password: ")
            if passInput == "pyatmdevcrazi3716":
                print("Access Granted!")
                time.sleep(1.5)
                clearWindow()
                pinInput = int(input("Insert your PIN to continue: "))
                if pinInput == PIN1:
                    print("Pin accepted")
                    time.sleep(2)
                    clearWindow()
                    while True:
                        print("1. Withdrawal")
                        print("2. Deposit")
                        print("3. Check Balance")
                        print("4. Check Wallet")
                        print("5. Sign Out")
                        time.sleep(1)
                        atmChoice = input("Input the number of your choice: ")
                        if atmChoice == "1":
                            drawalInput = int(input(f"How much do you want to withdraw? You have {bankBalance}: "))
                            if drawalInput > bankBalance:
                                print("This transaction is greater than your balance")
                            bankBalance = bankBalance - drawalInput
                            pocketBalance = pocketBalance + drawalInput
                            print(f"You have {pocketBalance} dollars in your pocket.")
                            print(f"You have {bankBalance} remaining.")
                            print("Thanks for Choosing PYATM!")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "2":
                            depositInput = int(input("How much do you want to deposit?: "))
                            if depositInput > pocketBalance:
                                print("This transaction is greater than your balance.")
                            else:
                                pocketBalance = pocketBalance - depositInput
                                bankBalance = bankBalance + depositInput
                                print(f"You now have {bankBalance} dollars.")
                                print(f"You now have {pocketBalance} in your pocket.")
                                time.sleep(2)
                                clearWindow()
                        elif atmChoice == "3":
                            print(f"You have {bankBalance} dollars in your account.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "4":
                            print(f"You throughly looked through your wallet and counted {pocketBalance} dollars.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "5":
                            print("Thanks for Choosing PYATM! See you next time!")
                            time.sleep(2)
                            print("Closing Application in...")
                            time.sleep(1)
                            print("3")
                            time.sleep(1)
                            print("2")
                            time.sleep(1)
                            print("1")
                            time.sleep(1)
                            exit()
                        elif atmChoice == "devcrazi":
                            print("DEVELOPER MODE ACCESSED!")
                            time.sleep(2)
                            clearWindow()
                            while True:
                                print("1. Withdrawal")
                                print("2. Deposit")
                                print("3. Check Balance")
                                print("4. Add Money To Pocket")
                                print("5. Add Money To Bank Account")
                                print("6. Sign Out")
                                print("7. Check Wallet")
                                time.sleep(1)
                                atmChoice = input("Input the number of your choice: ")
                                if atmChoice == "1":
                                    drawalInput = int(input(f"How much do you want to withdraw? You have {bankBalance}: "))
                                    if drawalInput > bankBalance:
                                        print("This transaction is greater than your balance")
                                    bankBalance = bankBalance - drawalInput
                                    pocketBalance = pocketBalance + drawalInput
                                    print(f"You have {pocketBalance} dollars in your pocket.")
                                    print(f"You have {bankBalance} remaining.")
                                    time.sleep(2)
                                    clearWindow()
                                elif atmChoice == "2":
                                    depositInput = int(input("How much do you want to deposit?: "))
                                    if depositInput > pocketBalance:
                                        print("This transaction is greater than your balance.")
                                    else:
                                        pocketBalance = pocketBalance - depositInput
                                        bankBalance = bankBalance + depositInput
                                        print(f"You now have {bankBalance} dollars.")
                                        print(f"You now have {pocketBalance} in your pocket.")
                                        time.sleep(2)
                                        clearWindow()
                                elif atmChoice == "3":
                                    print(f"You have {bankBalance} dollars in your account.")
                                    time.sleep(2)
                                    clearWindow()
                                elif atmChoice == "4":
                                    addMoneyPocket = int(input("How much money do you want to add?: "))
                                    pocketBalance = pocketBalance + addMoneyPocket
                                    print(f"Funds have been added to your account! Spend it wisely! You have {pocketBalance}!")
                                    time.sleep(3)
                                    clearWindow()
                                elif atmChoice == "5":
                                    addMoneyBank = int(input("How much money you want to add to bank?: "))
                                    bankBalance = bankBalance + addMoneyBank
                                    print(f"Funds have been added to your account! Spend it wisely! You have {bankBalance}!")
                                    time.sleep(3)
                                    clearWindow()
                                elif atmChoice == "6":
                                    print("Thanks for Choosing PYATM! See you next time!")
                                    time.sleep(2)
                                    print("Closing Application in...")
                                    time.sleep(1)
                                    print("3")
                                    time.sleep(1)
                                    print("2")
                                    time.sleep(1)
                                    print("1")
                                    time.sleep(1)
                                    exit()
                                elif atmChoice == "7":
                                    print(f"You opened your wallet. You count and remark {pocketBalance} dollars in your wallet.")
                                    time.sleep(2)
                                    clearWindow()
                                else:
                                    print("Invalid Input! Closing Application...")
                                    time.sleep(3)
                                    exit()
                            else:
                                print("Invalid Input! Closing Application...")
                                time.sleep(3)
                                exit()
                elif pinInput == PIN2:
                    print("Pin Accepted!")
                    time.sleep(2)
                    clearWindow()
                    while True:
                        print("1. Withdrawal")
                        print("2. Deposit")
                        print("3. Check Balance")
                        print("4. Check Wallet")
                        print("5. Sign Out")
                        time.sleep(1)
                        atmChoice = input("Input the number of your choice: ")
                        if atmChoice == "1":
                            drawalInput = int(input(f"How much do you want to withdraw? You have {bankBalance}: "))
                            if drawalInput > bankBalance:
                                print("This transaction is greater than your balance")
                            bankBalance = bankBalance - drawalInput
                            pocketBalance = pocketBalance + drawalInput
                            print(f"You have {pocketBalance} dollars in your pocket.")
                            print(f"You have {bankBalance} remaining.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "2":
                            depositInput = int(input("How much do you want to deposit?: "))
                            if depositInput > pocketBalance:
                                print("This transaction is greater than your balance.")
                            else:
                                pocketBalance = pocketBalance - depositInput
                                bankBalance = bankBalance + depositInput
                                print(f"You now have {bankBalance} dollars.")
                                print(f"You now have {pocketBalance} in your pocket.")
                                time.sleep(2)
                                clearWindow()
                        elif atmChoice == "3":
                            print(f"You have {bankBalance} dollars in your account.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "4":
                            print(f"You throughly looked through your wallet and counted {pocketBalance} dollars.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "5":
                            print("Thanks for Choosing PYATM! See you next time!")
                            time.sleep(2)
                            print("Closing Application in...")
                            time.sleep(1)
                            print("3")
                            time.sleep(1)
                            print("2")
                            time.sleep(1)
                            print("1")
                            time.sleep(1)
                            exit
                        elif atmChoice == "devcrazi":
                            print("DEVELOPER MODE ACCESSED!")
                            time.sleep(2)
                            clearWindow()
                            while True:
                                print("1. Withdrawal")
                                print("2. Deposit")
                                print("3. Check Balance")
                                print("4. Add Money To Pocket")
                                print("5. Add Money To Bank Account")
                                print("6. Sign Out")
                                print("7. Check Wallet")
                                time.sleep(1)
                                atmChoice = input("Input the number of your choice: ")
                                if atmChoice == "1":
                                    drawalInput = int(input(f"How much do you want to withdraw? You have {bankBalance}: "))
                                    if drawalInput > bankBalance:
                                        print("This transaction is greater than your balance")
                                    bankBalance = bankBalance - drawalInput
                                    pocketBalance = pocketBalance + drawalInput
                                    print(f"You have {pocketBalance} dollars in your pocket.")
                                    print(f"You have {bankBalance} remaining.")
                                    time.sleep(2)
                                    clearWindow()
                                elif atmChoice == "2":
                                    depositInput = int(input("How much do you want to deposit?: "))
                                    if depositInput > pocketBalance:
                                        print("This transaction is greater than your balance.")
                                    else:
                                        pocketBalance = pocketBalance - depositInput
                                        bankBalance = bankBalance + depositInput
                                        print(f"You now have {bankBalance} dollars.")
                                        print(f"You now have {pocketBalance} in your pocket.")
                                        time.sleep(2)
                                        clearWindow()
                                elif atmChoice == "3":
                                    print(f"You have {bankBalance} dollars in your account.")
                                    time.sleep(2)
                                    clearWindow()
                                elif atmChoice == "4":
                                    addMoneyPocket = int(input("How much money do you want to add?: "))
                                    pocketBalance = pocketBalance + addMoneyPocket
                                    print(f"Funds have been added to your account! Spend it wisely! You have {pocketBalance}!")
                                    time.sleep(3)
                                    clearWindow()
                                elif atmChoice == "5":
                                    addMoneyBank = int(input("How much money you want to add to bank?: "))
                                    bankBalance = bankBalance + addMoneyBank
                                    print(f"Funds have been added to your account! Spend it wisely! You have {bankBalance}!")
                                    time.sleep(3)
                                    clearWindow()
                                elif atmChoice == "6":
                                    print("Thanks for Choosing PYATM! See you next time!")
                                    time.sleep(2)
                                    print("Closing Application in...")
                                    time.sleep(1)
                                    print("3")
                                    time.sleep(1)
                                    print("2")
                                    time.sleep(1)
                                    print("1")
                                    time.sleep(1)
                                    exit()
                                elif atmChoice == "7":
                                    print(f"You opened your wallet. You count and remark {pocketBalance} dollars in your wallet.")
                                    time.sleep(2)
                                    clearWindow()
                                else:
                                    print("Invalid Input! Closing Application...")
                                    time.sleep(3)
                                    exit()
                        else:
                            print("Invalid Input! Closing Application...")
                            time.sleep(3)
                            exit()
                elif pinInput == PIN3:
                    print("Pin Accepted!")
                    time.sleep(2)
                    clearWindow()
                    while True:
                        print("1. Withdrawal")
                        print("2. Deposit")
                        print("3. Check Balance")
                        print("4. Check Wallet")
                        print("5. Sign Out")
                        time.sleep(1)
                        atmChoice = input("Input the number of your choice: ")
                        if atmChoice == "1":
                            drawalInput = int(input(f"How much do you want to withdraw? You have {bankBalance}: "))
                            if drawalInput > bankBalance:
                                print("This transaction is greater than your balance")
                            bankBalance = bankBalance - drawalInput
                            pocketBalance = pocketBalance + drawalInput
                            print(f"You have {pocketBalance} dollars in your pocket.")
                            print(f"You have {bankBalance} remaining.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "2":
                            depositInput = int(input("How much do you want to deposit?: "))
                            if depositInput > pocketBalance:
                                print("This transaction is greater than your balance.")
                            else:
                                pocketBalance = pocketBalance - depositInput
                                bankBalance = bankBalance + depositInput
                                print(f"You now have {bankBalance} dollars.")
                                print(f"You now have {pocketBalance} in your pocket.")
                                time.sleep(2)
                                clearWindow()
                        elif atmChoice == "3":
                            print(f"You have {bankBalance} dollars in your account.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "4":
                            print(f"You throughly looked through your wallet and counted {pocketBalance} dollars.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "5":
                            print("Thanks for Choosing PYATM! See you next time!")
                            time.sleep(2)
                            print("Closing Application in...")
                            time.sleep(1)
                            print("3")
                            time.sleep(1)
                            print("2")
                            time.sleep(1)
                            print("1")
                            time.sleep(1)
                            exit()
                        elif atmChoice == "devcrazi":
                            print("DEVELOPER MODE ACCESSED!")
                            time.sleep(2)
                            clearWindow()
                            while True:
                                print("1. Withdrawal")
                                print("2. Deposit")
                                print("3. Check Balance")
                                print("4. Add Money To Pocket")
                                print("5. Add Money To Bank Account")
                                print("6. Sign Out")
                                print("7. Check Wallet")
                                time.sleep(1)
                                atmChoice = input("Input the number of your choice: ")
                                if atmChoice == "1":
                                    drawalInput = int(input(f"How much do you want to withdraw? You have {bankBalance}: "))
                                    if drawalInput > bankBalance:
                                        print("This transaction is greater than your balance")
                                    bankBalance = bankBalance - drawalInput
                                    pocketBalance = pocketBalance + drawalInput
                                    print(f"You have {pocketBalance} dollars in your pocket.")
                                    print(f"You have {bankBalance} remaining.")
                                    time.sleep(2)
                                    clearWindow()
                                elif atmChoice == "2":
                                    depositInput = int(input("How much do you want to deposit?: "))
                                    if depositInput > pocketBalance:
                                        print("This transaction is greater than your balance.")
                                    else:
                                        pocketBalance = pocketBalance - depositInput
                                        bankBalance = bankBalance + depositInput
                                        print(f"You now have {bankBalance} dollars.")
                                        print(f"You now have {pocketBalance} in your pocket.")
                                        time.sleep(2)
                                        clearWindow()
                                elif atmChoice == "3":
                                    print(f"You have {bankBalance} dollars in your account.")
                                    time.sleep(2)
                                    clearWindow()
                                elif atmChoice == "4":
                                    addMoneyPocket = int(input("How much money do you want to add?: "))
                                    pocketBalance = pocketBalance + addMoneyPocket
                                    print(f"Funds have been added to your account! Spend it wisely! You have {pocketBalance}!")
                                    time.sleep(3)
                                    clearWindow()
                                elif atmChoice == "5":
                                    addMoneyBank = int(input("How much money you want to add to bank?: "))
                                    bankBalance = bankBalance + addMoneyBank
                                    print(f"Funds have been added to your account! Spend it wisely! You have {bankBalance}!")
                                    time.sleep(3)
                                    clearWindow()
                                elif atmChoice == "6":
                                    print("Thanks for Choosing PYATM! See you next time!")
                                    time.sleep(2)
                                    print("Closing Application in...")
                                    time.sleep(1)
                                    print("3")
                                    time.sleep(1)
                                    print("2")
                                    time.sleep(1)
                                    print("1")
                                    time.sleep(1)
                                    exit()
                                elif atmChoice == "7":
                                    print(f"You opened your wallet. You count and remark {pocketBalance} dollars in your wallet.")
                                    time.sleep(2)
                                    clearWindow()
                                else:
                                    print("Invalid Input! Closing Application...")
                                    time.sleep(3)
                                    exit()
                        else:
                            print("Invalid Input! Closing Application...")
                            time.sleep(3)
                            exit()
                elif pinInput == PIN4:
                    print("Pin Accepted!")
                    time.sleep(2)
                    clearWindow()
                    while True:
                        print("1. Withdrawal")
                        print("2. Deposit")
                        print("3. Check Balance")
                        print("4. Check Wallet")
                        print("5. Sign Out")
                        time.sleep(1)
                        atmChoice = input("Input the number of your choice: ")
                        if atmChoice == "1":
                            drawalInput = int(input(f"How much do you want to withdraw? You have {bankBalance}: "))
                            if drawalInput > bankBalance:
                                print("This transaction is greater than your balance")
                            bankBalance = bankBalance - drawalInput
                            pocketBalance = pocketBalance + drawalInput
                            print(f"You have {pocketBalance} dollars in your pocket.")
                            print(f"You have {bankBalance} remaining.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "2":
                            depositInput = int(input("How much do you want to deposit?: "))
                            if depositInput > pocketBalance:
                                print("This transaction is greater than your balance.")
                            else:
                                pocketBalance = pocketBalance - depositInput
                                bankBalance = bankBalance + depositInput
                                print(f"You now have {bankBalance} dollars.")
                                print(f"You now have {pocketBalance} in your pocket.")
                                time.sleep(2)
                                clearWindow()
                        elif atmChoice == "3":
                            print(f"You have {bankBalance} dollars in your account.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "4":
                            print(f"You throughly looked through your wallet and counted {pocketBalance} dollars.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "5":
                            print("Thanks for Choosing PYATM! See you next time!")
                            time.sleep(2)
                            print("Closing Application in...")
                            time.sleep(1)
                            print("3")
                            time.sleep(1)
                            print("2")
                            time.sleep(1)
                            print("1")
                            time.sleep(1)
                            exit()
                        elif atmChoice == "devcrazi":
                            print("DEVELOPER MODE ACCESSED!")
                            time.sleep(2)
                            clearWindow()
                            while True:
                                print("1. Withdrawal")
                                print("2. Deposit")
                                print("3. Check Balance")
                                print("4. Add Money To Pocket")
                                print("5. Add Money To Bank Account")
                                print("6. Sign Out")
                                print("7. Check Wallet")
                                time.sleep(1)
                                atmChoice = input("Input the number of your choice: ")
                                if atmChoice == "1":
                                    drawalInput = int(input(f"How much do you want to withdraw? You have {bankBalance}: "))
                                    if drawalInput > bankBalance:
                                        print("This transaction is greater than your balance")
                                    bankBalance = bankBalance - drawalInput
                                    pocketBalance = pocketBalance + drawalInput
                                    print(f"You have {pocketBalance} dollars in your pocket.")
                                    print(f"You have {bankBalance} remaining.")
                                    time.sleep(2)
                                    clearWindow()
                                elif atmChoice == "2":
                                    depositInput = int(input("How much do you want to deposit?: "))
                                    if depositInput > pocketBalance:
                                        print("This transaction is greater than your balance.")
                                    else:
                                        pocketBalance = pocketBalance - depositInput
                                        bankBalance = bankBalance + depositInput
                                        print(f"You now have {bankBalance} dollars.")
                                        print(f"You now have {pocketBalance} in your pocket.")
                                        time.sleep(2)
                                        clearWindow()
                                elif atmChoice == "3":
                                    print(f"You have {bankBalance} dollars in your account.")
                                    time.sleep(2)
                                    clearWindow()
                                elif atmChoice == "4":
                                    addMoneyPocket = int(input("How much money do you want to add?: "))
                                    pocketBalance = pocketBalance + addMoneyPocket
                                    print(f"Funds have been added to your account! Spend it wisely! You have {pocketBalance}!")
                                    time.sleep(3)
                                    clearWindow()
                                elif atmChoice == "5":
                                    addMoneyBank = int(input("How much money you want to add to bank?: "))
                                    bankBalance = bankBalance + addMoneyBank
                                    print(f"Funds have been added to your account! Spend it wisely! You have {bankBalance}!")
                                    time.sleep(3)
                                    clearWindow()
                                elif atmChoice == "6":
                                    print("Thanks for Choosing PYATM! See you next time!")
                                    time.sleep(2)
                                    print("Closing Application in...")
                                    time.sleep(1)
                                    print("3")
                                    time.sleep(1)
                                    print("2")
                                    time.sleep(1)
                                    print("1")
                                    time.sleep(1)
                                    exit()
                                elif atmChoice == "7":
                                    print(f"You opened your wallet. You count and remark {pocketBalance} dollars in your wallet.")
                                    time.sleep(2)
                                    clearWindow()
                                else:
                                    print("Invalid Input! Closing Application...")
                                    time.sleep(3)
                                    exit()
                    else:
                        print("Invalid Input! Closing Application...")
                        time.sleep(3)
                        exit()
                elif pinInput == PIN5:
                    print("Pin Accepted!")
                    time.sleep(2)
                    while True:
                        print("1. Withdrawal")
                        print("2. Deposit")
                        print("3. Check Balance")
                        print("4. Check Wallet")
                        print("5. Sign Out")
                        time.sleep(1)
                        atmChoice = input("Input the number of your choice: ")
                        if atmChoice == "1":
                            drawalInput = int(input(f"How much do you want to withdraw? You have {bankBalance}: "))
                            if drawalInput > bankBalance:
                                print("This transaction is greater than your balance")
                            bankBalance = bankBalance - drawalInput
                            pocketBalance = pocketBalance + drawalInput
                            print(f"You have {pocketBalance} dollars in your pocket.")
                            print(f"You have {bankBalance} remaining.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "2":
                            depositInput = int(input("How much do you want to deposit?: "))
                            if depositInput > pocketBalance:
                                print("This transaction is greater than your balance.")
                            else:
                                pocketBalance = pocketBalance - depositInput
                                bankBalance = bankBalance + depositInput
                                print(f"You now have {bankBalance} dollars.")
                                print(f"You now have {pocketBalance} in your pocket.")
                                time.sleep(2)
                                clearWindow()
                        elif atmChoice == "3":
                            print(f"You have {bankBalance} dollars in your account.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "4":
                            print(f"You throughly looked through your wallet and counted {pocketBalance} dollars.")
                            time.sleep(2)
                            clearWindow()
                        elif atmChoice == "5":
                            print("Thanks for Choosing PYATM! See you next time!")
                            time.sleep(2)
                            print("Closing Application in...")
                            time.sleep(1)
                            print("3")
                            time.sleep(1)
                            print("2")
                            time.sleep(1)
                            print("1")
                            time.sleep(1)
                            exit()
                        elif atmChoice == "devcrazi":
                            print("DEVELOPER MODE ACCESSED!")
                            time.sleep(2)
                            clearWindow()
                            while True:
                                print("1. Withdrawal")
                                print("2. Deposit")
                                print("3. Check Balance")
                                print("4. Add Money To Pocket")
                                print("5. Add Money To Bank Account")
                                print("6. Sign Out")
                                print("7. Check Wallet")
                                time.sleep(1)
                                atmChoice = input("Input the number of your choice: ")
                                if atmChoice == "1":
                                    drawalInput = int(input(f"How much do you want to withdraw? You have {bankBalance}: "))
                                    if drawalInput > bankBalance:
                                        print("This transaction is greater than your balance")
                                    bankBalance = bankBalance - drawalInput
                                    pocketBalance = pocketBalance + drawalInput
                                    print(f"You have {pocketBalance} dollars in your pocket.")
                                    print(f"You have {bankBalance} remaining.")
                                    time.sleep(2)
                                    clearWindow()
                                elif atmChoice == "2":
                                    depositInput = int(input("How much do you want to deposit?: "))
                                    if depositInput > pocketBalance:
                                        print("This transaction is greater than your balance.")
                                    else:
                                        pocketBalance = pocketBalance - depositInput
                                        bankBalance = bankBalance + depositInput
                                        print(f"You now have {bankBalance} dollars.")
                                        print(f"You now have {pocketBalance} in your pocket.")
                                        time.sleep(2)
                                        clearWindow()
                                elif atmChoice == "3":
                                    print(f"You have {bankBalance} dollars in your account.")
                                    time.sleep(2)
                                    clearWindow()
                                elif atmChoice == "4":
                                    addMoneyPocket = int(input("How much money do you want to add?: "))
                                    pocketBalance = pocketBalance + addMoneyPocket
                                    print(f"Funds have been added to your account! Spend it wisely! You have {pocketBalance}!")
                                    time.sleep(3)
                                    clearWindow()
                                elif atmChoice == "5":
                                    addMoneyBank = int(input("How much money you want to add to bank?: "))
                                    bankBalance = bankBalance + addMoneyBank
                                    print(f"Funds have been added to your account! Spend it wisely! You have {bankBalance}!")
                                    time.sleep(3)
                                    clearWindow()
                                elif atmChoice == "6":
                                    print("Thanks for Choosing PYATM! See you next time!")
                                    time.sleep(2)
                                    print("Closing Application in...")
                                    time.sleep(1)
                                    print("3")
                                    time.sleep(1)
                                    print("2")
                                    time.sleep(1)
                                    print("1")
                                    time.sleep(1)
                                    exit()
                                elif atmChoice == "7":
                                    print(f"You opened your wallet. You count and remark {pocketBalance} dollars in your wallet.")
                                    time.sleep(2)
                                    clearWindow()
                                else:
                                    print("Invalid Input! Closing Application...")
                                    time.sleep(3)
                                    exit()
                        else:
                            print("Invalid Input! Closing Application...")
                            time.sleep(3)
                            exit()
                else:
                    print("PIN Invalid!")
                    exit()
        else:
            print("Incorrect Administrator Username. Quitting Application.")
            exit()
    else:
        exit()
