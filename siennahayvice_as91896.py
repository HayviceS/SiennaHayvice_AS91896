#Stating risks
print("WARNING: This game has themes of death, entrapment, poison, claustrophobia. Due to these themes if you are not comfortable continuing please exit the game. This game may also save your data\n\
    and can not guarantee your privacy.")

#Yes or No def shortcut
#Used for all yes or no questions as you can modify it to fit the situation
def yes_no(message = "Write 'yes' or 'no' to answer: "): 
     while True:
          user_input = input(message)
          user_input = user_input[0].lower()
          if user_input == "y":
               return True
          elif user_input == "n":
               return False
          else:
               print("Please try writing that again, either answer with 'yes' or 'no': ")

#Asking if user want to play
def start_game():
    global name
    while True:
        name = input("Hello adventurer! What is your name?: ")
        name = name[0].upper() + name[1:].lower()
        if yes_no("Welcome {}, Are you ready to get started? yes/no: ".format(name)):
             print("Great, let's get started!")
             return 
        else:
             print("That's fine! Maybe another time.")
             exit()

#Direction def shortcut
#Used for all questions where you have to pick a left or right direction
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
        death_log.append("Died in a cave in")
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
        death_log.append("Died due to poisonous gas")
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
        print("The room is lit up by torches and you see drawings on the walls depicting ancient battles.")
        print("You stand in the room and feel your knife in your pocket.")
        if yes_no("Do you use the knife to draw/write something on the wall? Yes/no: "):
            wall_writing = input("What do you write or draw on the wall?: ")
            print("You leave {} on the wall and then turn to make your way back to the room you were last in".format(wall_writing))
            return room6()
        else:
             print("You decide to not damage the wall and go back to the room you came from.")
             return room6()

def room8():
        global death_count
        print("You have entered the room to your right.")
        print("Your mouth is dry and you are thirsty. You see a small fountain and have to decide if you will drink the water or if you will continue and risk dying of dehydration before escaping.")
        print("You don't know if the water is safe to drink but you don't know how much longer you will be stuck for.")
        if yes_no("Will you drink the water? Yes/no: "):
             print("You drink the water and die instantly from poisoning. Game over!")
             death_count += 1
             death_log.append("Died due to poison")
             return "loss"
        else:
             print("You choose to not drink the water and continue onto the next room.")
             return room9()
        
def room9():
        print("You have entered the next room.")
        print("You see a way out! You run toward it and find yourself outside the cave and back in the enchanted forest.")
        print("Congratulations {}, you escaped the cave and you can now make your way back home! You win!".format(name))
        print("In total you have died {} times through out the game!".format(death_count))
        print(death_log)
        return "win"


#Main game
def main_game():
    global death_count
    print("After wandering around the enchanted forest you wake up in a cold and dark cave barely able to see your hands in front of you. You remember wandering in and then there was a cave in! Now you have to find your own way out.")
    print("While wiping dirt off your clothes you find 3 items, a fully charged torch, a knife, and a small bag of trail mix.")

    while True:
        if yes_no("Will you turn on the torch? Yes/no: "):
             print("You turn on the torch and find two tunnels")
        else:
             print("You failed to escape the cave! Game over!")
             death_count += 1
             death_log.append("Died, stuck in cave")
             return "loss"
        
        pick = what_direction()
        if pick == 'l':
            return room2() or "loss"
        if pick == 'r':
            return room3() or "loss"

#Making loop
#Makes the game able to start again and leads the death count to be added and reset
def play_loop():
    global death_log
    global death_count
    death_log = []
    death_count = 0 

    while True:

        start_game()
        result = main_game()

        if result == "win":
            death_count = 0
        if result == "win":
             death_log = []


        if yes_no("Do you want to play again? Yes/no: "):
            print("The game will restart now!")
        else:
             print("That's fine, play again soon!")
             exit()
            

#Restart
play_loop()

