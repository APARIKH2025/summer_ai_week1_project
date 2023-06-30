# You can implement user interface functions here.

def mainMenu():
    print("")
    print("1. Manage my account")
    print("2. Send a message")
    print("5. Quit or Change Account")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. View all my messages")
    print("5. <- Go back ")
    return input("Please Choose a number: ")
