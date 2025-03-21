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
                        print("Your new age is", current_account.year)
                        break

                elif inner_menu_choice == "2":
                    friend = input("Who do you want to add as your friend: ")
                    if friend in ai_social_network.list_of_names and not(friend in current_account.friendlist):
                        current_account.friendlist.append(friend)
                    elif friend in current_account.friendlist:
                        print(friend,"is already your friend.")
                    else:
                        print(friend, "was not found.")
                    break

                elif inner_menu_choice == "3":
                    current_account.print_friendlist()
                    break
                    

                elif inner_menu_choice == "4":
                    if current_account.inbox == []:
                       print("You have no new messages.")
                    else:
                        for message in current_account.inbox:
                            print(message[0], "from", message[1])
                            if (input("Do you want to reply [y/n]: ") == "y"):
                                ai_social_network.list_of_people[ai_social_network.list_of_names.index(message[1])].inbox.append([input("What is the message you would like to send: ") , current_account_name])
                        current_account.inbox.remove(message)
                    break

                else:
                    print("Your input is invalid. Try Again!")
                    inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "2":
            current_account.send_message(ai_social_network.list_of_people, ai_social_network.list_of_names, current_account_name)
            
        
        elif choice == "3":
            person_to_block = input("Who would you like to block: ")
            if person_to_block in current_account.friendlist:
                current_account.friendlist.remove(person_to_block)
            if current_account_name in ai_social_network.list_of_people[ai_social_network.list_of_names.index(person_to_block)].friendlist:
                ai_social_network.list_of_people[ai_social_network.list_of_names.index(person_to_block)].friendlist.remove(current_account_name)
            print(person_to_block, "has been blocked.")

        elif choice == "4":
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

        elif choice == "5":
            print("Thank you for visiting. Goodbye")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()