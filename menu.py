from scanner import runZap
#import scanner
import os
import subprocess



# Define functions for each menu option
def webscanpart():
    print("\n\nWEB APPLICATION VULNERABILITY TESTING")
    print("*******************************************\n")

    ###### ENTER TARGET URL TO ATTACK ######

    attacksite = input("\n [*] ENTER TARGET URL TO CONTINUE : ")

    ##### PASSING ATTACK URL TO MAIN CODE #####

    target = attacksite
    useScanPolicy = None
    ascanIds = []

    ###### SCAN POLICY ######

    ## FALSE > ALL ATTACKS
    ## TRUE > SELECTED ATTACKS

    print("\n1. SELECT ATTACKS")
    print("\n2. PERFORM ALL ATTACKS (takes time)")
    scanpolicy = int(input("[*] Enter your choice (1 or 2) : "))

    if scanpolicy == 1:
        useScanPolicy = True

        ###### OPEN ATTACK ID LIST ######

        #os.startfile('attacks in zap.xlsx')

        ###### TAKE ATTACK IDs FROM USER ######

        num_list = []
        n = int(input("\nEnter the number of attacks you want to perform: "))
        for i in range(n):
            num = int(input("Enter ID for attack {}: ".format(i + 1)))
            num_list.append(num)
        print("\n\nYou have selected the following attack IDs:", num_list)

        ascanIds = num_list

    elif scanpolicy == 2:
        useScanPolicy = False

    else:
        print("\nInvalid Choice")


    ###### SET ATTACK STRENGTH ######

    print(" Attack Strength : ")
    print("\nCan be: 1. Low  |  2. Medium  |  3. High  ")
    strength = int(input("\n Enter your choice (1,2,3) : "))

    if strength == 1:
        attackStrength = 'Low'
    elif strength == 2:
        attackStrength = 'Medium'
    elif strength == 3:
        attackStrength = 'High'
    else:
        print("Invalid Choice")

###### CALL MAIN API ######
    runZap(target, useScanPolicy, ascanIds, attackStrength)
#subprocess.call(['python', 'webscanner.py'])



def iotpart():
    print("\n\nIoT VULNERABILITY TESTING")
    print("*******************************************\n")





print("\n\n")
print("********************************************************************************\n\n")
print(" _   _      _      ____    ____    ___   _   _    ____   _____   ____   ")
print("| | | |    / \    |  _ \  | __ )  |_ _| | \ | |  / ___| | ____| |  _ \  ")
print("| |_| |   / _ \   | |_) | |  _ \   | |  |  \| | | |  _  |  _|   | |_) | ")
print("|  _  |  / ___ \  |  _ <  | |_) |  | |  | |\  | | |_| | | |___  |  _ <  ")
print("|_| |_| /_/   \_\ |_| \_\ |____/  |___| |_| \_|  \____| |_____| |_| \_\ ")
print("\n\n********************************************************************************\n\n")

while True:
    print("Menu:")
    print("1. Web Application Vulnerability Testing")
    print("2. Iot Vulnerability Testing")
    print("3. Exit")

    choice = input("[*] Enter your choice: ")

    # Call the appropriate function based on the user's choice
    if choice == "1":
        webscanpart()
    elif choice == "2":
        iotpart()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")


