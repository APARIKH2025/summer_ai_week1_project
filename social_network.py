#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui



#Create instance of main social network object
ai_social_network = SocialNetwork()
signed_in = False

while not(signed_in):
    if (input("Do you have an account [y/n]?") == 'y'):
        current_account_name = input("What is your name: ")
        current_account = ai_social_network.list_of_people[ai_social_network.list_of_names.index(current_account_name)]
        if current_account.check_password(input("What is your password: ")):
            print("Welcome")
            signed_in = True
        else:
            print("Wrong password")

    else:
        ai_social_network.create_account()
        current_account_name = input("Please confirm your name: ")
        current_account = ai_social_network.list_of_people[ai_social_network.list_of_names.index(current_account_name)]
        signed_in = True

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            

        elif choice == "2":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                if inner_menu_choice == "5":
                    break

                elif (inner_menu_choice == "1"):
                    print("1. Change your name\n2. Change your age")
                    nameorage = input("Please enter 1 or 2: ")
                    if nameorage == "1":
                        new_name = input("What is the new name: ")
                        current_account_name = new_name
                        current_account.change_name(new_name)
                        ai_social_network.list_of_names[ai_social_network.list_of_people.index(current_account)] = new_name
                        print("Your new name is", current_account.id)
                        break
                    if nameorage == "2":
                        new_age = input("What is the new age: ")
                        current_account.change_age(new_age)
                        break

                else:
                    print("Your input is invalid. Try Again!")
                    inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "3":
            print("Thank you for visiting. Goodbye")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
