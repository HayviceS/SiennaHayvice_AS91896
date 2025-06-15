#Stating risks
print("This game has themes, of death, being trapped, posion, claustrophobia. If you are not ok with this I would suggest you dont continue. This game may also save your data\n\
    and can not garantie your privicy.")

#Asking if user want to play
while True:
    name = input("Hello adventurer! What is your name? ")
    starting = input("Welcome {}, Are you ready to get started? yes/no: ".format(name))
    starting.lower
    if starting == "yes":
        print("Great, let's get started!")

#Begining game
        print("After wondering around the enchanted forest you wake up in a cold and dark cave. You remember wandering in and then there was a cave in! Now you have to find your own way out.")
        print("While wiping dirt off your clothes you find 3 items, a fully charged torch, a knife, and a small bag of trail mix.")
        light = input("Will you turn on the torch? yes/no: ")
        if light == "no":
            print("You failed to escape the cave! Game over.")
        if light == "yes":
            print("You turn on the torch and find two tunnles")


    if starting == "no":
        exit = input("Are you sure you don't want to contiune? yes/no: ")
        exit.lower
        if exit == "yes": 
            print("That's fine! Maybe another time.")
            break
            if exit == "no":
                print("Then let's get started!")
