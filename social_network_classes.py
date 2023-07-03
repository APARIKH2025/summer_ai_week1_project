# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        self.list_of_names = []
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def  create_account(self):
        name = input("What is your name: ")
        self.list_of_people.append(Person(name, input("What is your age: "), input("What is your password: ")))
        #implement function that creates account here
        self.list_of_names.append(name)
        print("Done")
        pass


class Person:
    def __init__(self, name, age, password):
        self.id = name
        self.year = age
        self.password = password
        self.friendlist = []
        self.inbox = []

    def send_message(self, list_of_people, list_of_names, sender):
        keep_going = True
        while keep_going == True:
            recipient = input("Who would you like to send a message to: ")
            if recipient in list_of_names:
                list_of_people[list_of_names.index(recipient)].inbox.append([input("What is the message you would like to send: ") , sender])
                keep_going == False
                break
            else:
                keep_going = (input("This person is not on the platform, would you like to quit [y/n]?") == "n")
        

    def change_name(self, name):
        self.id = name
        pass

    def change_age(self, age):
        self.year = age
        pass

    def check_password(self, password):
        return self.password == password
    
    def print_friendlist(self):
        for friend in self.friendlist:
            print(friend)