#Stating risks
print("This game has themes, of death, being trapped, posion, claustrophobia. If you are not ok with this I would suggest you dont continue. This game may also save your data\n\
    and can not garantie your privicy.")

#Asking if user want to play
def start_game():
    global name
    while True:
        name = input("Hello adventurer! What is your name? ")
        name = name[0].upper() + name[1:].lower()
        starting = input("Welcome {}, Are you ready to get started? yes/no: ".format(name)).lower()
        if starting == "yes":
            print("Great, let's get started!")
            break
        elif starting == "no":
            leave = input("Are you sure you don't want to contiune? yes/no: ")
            leave.lower
            if leave == "yes": 
                print("That's fine! Maybe another time.")
                exit()
            elif leave == "no":
                print("Then let's get started!")
                break

#Direction shortcut
def what_direction():
    pick = input("What way would you like to go? Left or right: ")   
    if pick == '': 
        return None
    pick = pick[0].lower()
    if pick in ['l','r']:
        return pick
    else:
        print("Please trying writing that again, I don't understand")
        return what_direction()

# Defining rooms
def room2():
        print("You have entered you have entered the room to your left.")
        print("This room is a dead end")
        return False

def room3():
        print("You have entered the room to your right.")
        print("The roof of the cave is filled with glow worms, they light up the room and you spend a few seconds watching them before looking around for your next move.")
        print("You find out there is only one way to go so you follow the path.")
        return room4()

def room4():
        print("You have entered another room and find two more tunnles to choose from.")
        pick = what_direction()
        if pick == 'l':
            return room5()
        if pick == 'r':
            return room6()

def room5():
        print("You have entered the room to your left.")
        print("As you walk into the room you walk into a trip wire and a poisonous gas fills the room killing you.")
        print("Game over")
        return False
            
def room6():
        print("You have entered the room to your right.")
        print("You yet again find yourself in a room with two more tunnels to choose from.")
        print("The tunnle on your left is bright and inviting but you can't quite see whats inside. In the tunnel on you right you don't see any light but you hear the sound of water.")
        pick = what_direction()
        if pick == 'l':
            return room7()
        if pick == 'r':
            return room8()

def room7():
        print("The room is lit up by touches and you see drawing on the walls depicting ancient battles. However, there is no way out this way and so you return to the room you were in prior.")
        return room6()

def room8():
        print("You have entered the room to your right.")
        print("Your mouth is dry and you are thirsty. You see a small fountain and have to deside if you will drink the water or if you will continue and risk dying of dehydration before escaping.")
        print("You don't know if the water is safe to drink but you don't know how much longer you will be stuck for.")
        drink = input("Will you drink the water? yes/no: ")
        drink = drink[0].lower()
        if drink == "y":
            print("You drink the water and die instantly from posioning. Game over!")
            return
        if drink == "n":
            print("You choose to not drink the water and continue onto the next room.")
            return room9()
        else: 
            print("Please trying writing that again, I don't understand. Write 'yes or 'no':")
            return room8()
        
def room9():
        print("You have entered the next room.")
        print("You see a way out! You run toward it and find yourself outside the cave and back in the enchanted forest.")
        print("Congratulations {}, you escaped the cave and you can now make your way back home! You win!".format(name))
        return True


#Main game
def main_game():
    print("After wondering around the enchanted forest you wake up in a cold and dark cave. You remember wandering in and then there was a cave in! Now you have to find your own way out.")
    print("While wiping dirt off your clothes you find 3 items, a fully charged torch, a knife, and a small bag of trail mix.")

    while True:
        light = input("Will you turn on the torch? yes/no: ")
        if light == "yes":
            light = light[0].lower()
            print("You turn on the torch and find two tunnles")
            break
        if light == "no":
            light = light[0].lower()
            print("You failed to escape the cave! Game over") 
            return False
        else:
            print("Please trying writing that again, I don't understand. Write 'yes' or 'no': ")

    pick = what_direction()
    if pick == 'l':
        return room2()
    if pick == 'r':
        return room3()

#Making loop
def play_loop():
    while True:
        start_game()
        result = main_game()
        again = input("Do you want to play again? yes/no: ")
        again = again[0].lower()
        if again == '':
            return None
        if again == 'y':
            print("Great let's play again!")
            continue
        elif again == 'n':
            print("That's fine! Maybe another time.")
            return
        else:
            print("Please trying writing that again, I don't understand")

#Restart
play_loop()

