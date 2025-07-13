#Stating risks
print("WARNING: This game has themes of death, entrapment, poison, claustrophobia. Due to these themes if you are not comfortable continuing please exit the game. This game may also save your data\n\
    and can not guarantee your privacy.")
#Asking if user want to play
def start_game():
    global name
    while True:
        name = input("Hello adventurer! What is your name?: ")
        name = name[0].upper() + name[1:].lower()
        starting = input("Welcome {}, Are you ready to get started? yes/no: ".format(name)).lower()
        if starting == "yes":
            print("Great, let's get started!")
            break
        elif starting == "no":
            leave = input("Are you sure you don't want to contiune? yes/no: ")
            leave.lower()
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
        global death_count
        print("You have entered the room to your left.")
        print("You quickly recognize this room is a dead end and before you can turn back there is another cave in and you die")
        print("Game over!")
        death_count += 1
        return "loss"

def room3():
        print("You have entered the room to your right.")
        print("The roof of the cave is filled with glow worms, they light up the room and you spend a few seconds watching them before looking around for your next move.")
        print("You find out there is only one way to go so you follow the path.")
        return room4()

def room4():
        print("You have entered another room and find two more tunnels to choose from.")
        pick = what_direction()
        if pick == 'l':
            return room5()
        if pick == 'r':
            return room6()

def room5():
        global death_count
        print("You have entered the room to your left.")
        print("As you walk into the room you walk into a trip wire and a poisonous gas fills the room killing you.")
        print("Game over")
        death_count += 1 
        return "loss"
            
def room6():
        print("You have entered the room to your right.")
        print("You yet again find yourself in a room with two more tunnels to choose from.")
        print("The tunnel on your left is bright and inviting but you can't quite see whats inside. In the tunnel on your right you don't see any light but you hear the sound of water.")
        pick = what_direction()
        if pick == 'l':
            return room7()
        if pick == 'r':
            return room8()

def room7():
        print("The room is lit up by torches and you see drawings on the walls depicting ancient battles. However, there is no way out this way and so you return to the room you were in prior.")
        return room6()

def room8():
        global death_count
        print("You have entered the room to your right.")
        print("Your mouth is dry and you are thirsty. You see a small fountain and have to decide if you will drink the water or if you will continue and risk dying of dehydration before escaping.")
        print("You don't know if the water is safe to drink but you don't know how much longer you will be stuck for.")
        drink = input("Will you drink the water? yes/no: ")
        drink = drink[0].lower()
        if drink == "y":
            print("You drink the water and die instantly from poisoning. Game over!")
            death_count += 1
            return "loss"
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
        print("In total you have died {} times through out the game!".format(death_count))
        return "win"


#Main game
def main_game():
    global death_count
    print("After wandering around the enchanted forest you wake up in a cold and dark cave barely able to see your hands in front of you. You remember wandering in and then there was a cave in! Now you have to find your own way out.")
    print("While wiping dirt off your clothes you find 3 items, a fully charged torch, a knife, and a small bag of trail mix.")

    while True:
        light = input("Will you turn on the torch? yes/no: ")
        if light == "yes":
            light = light[0].lower()
            print("You turn on the torch and find two tunnels")
            break
        if light == "no":
            light = light[0].lower()
            print("You failed to escape the cave! Game over") 
            death_count += 1
            return "loss"
        else:
            print("Please trying writing that again, I don't understand. Write 'yes' or 'no': ")

    pick = what_direction()
    if pick == 'l':
        return room2() or "loss"
    if pick == 'r':
        return room3() or "loss"

#Making loop
def play_loop():
    global death_count
    death_count = 0 

    while True:
        start_game()
        result = main_game()

        if result == "win":
             death_count = 0

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
            print("Please try writing that again, I don't understand")

#Restart
play_loop()

