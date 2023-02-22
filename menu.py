print("\n\n")
print("********************************************************************************\n\n")
print(" _   _      _      ____    ____    ___   _   _    ____   _____   ____   ")
print("| | | |    / \    |  _ \  | __ )  |_ _| | \ | |  / ___| | ____| |  _ \  ")
print("| |_| |   / _ \   | |_) | |  _ \   | |  |  \| | | |  _  |  _|   | |_) | ")
print("|  _  |  / ___ \  |  _ <  | |_) |  | |  | |\  | | |_| | | |___  |  _ <  ")
print("|_| |_| /_/   \_\ |_| \_\ |____/  |___| |_| \_|  \____| |_____| |_| \_\ ")
print("\n\n********************************************************************************\n\n")


# Define functions for each menu option
def option1():
    print("\n\nWEB APPLICATION VULNERABILITY TESTING")
    print("*******************************************\n")
    attacksite = input("\n [*] ENTER TARGET URL TO CONTINUE : ")


    while True:
        print("\n")
        print("\n 1. SELECT ATTACKS")
        print("\n 2. ALL ATTACKS ")

        attackchoice = input("\n\n ENTER YOUR CHOICE: ")

        



def option2():
    print("\n\nIoT VULNERABILITY TESTING")
    print("*******************************************\n")


while True:
    print("Menu:")
    print("1. Web Application Vulnerability Testing")
    print("2. Iot Vulnerability Testing")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Call the appropriate function based on the user's choice
    if choice == "1":
        option1()
    elif choice == "2":
        option2()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

