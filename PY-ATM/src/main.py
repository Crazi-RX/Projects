import time
import os
def clearWindow():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
changeLog = input("Would you like to see the Changelog?: (y/n)")
if changeLog == "y":
    print("""Changelog:
          - Fixed Bug when Limit is exceeded on Deposit or Withdraw beyond the Bank Account limit or Pocket Change Limit
          - Fixed Bug when user accepts the Changelog and automatically quits the application.
          - Fixed Bug when user types letters into a deposit input or withdrawal input and causes the application to quit.
          - Currently working on preventing the Pocket Change and Bank Account integers from going into negatives.
          - Changed messages after transactions.""")
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
                        print("4. Sign Out")
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
                        print("4. Sign Out")
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
                        print("4. Sign Out")
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
                        print("4. Sign Out")
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
                        print("4. Sign Out")
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
                        print("4. Sign Out")
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
                        print("4. Sign Out")
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
                        print("4. Sign Out")
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
                        print("4. Sign Out")
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
                        print("4. Sign Out")
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