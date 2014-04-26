#### Labyrinth ####
### A text based maze game written for a school project ###
### (c) Jacob Warring Eytle 2012 ###
## http://www.fruitbowlstudios.blogspot.com/p/about-me.html ##

#defines the entire game, contains functions within functions - handy.
def game():
#each room is defined in here; working backwards, it has too. Discovered that the hard way.

    def room4():
        print ("\nyaddayaddayadda")

    def room3():
        print ("\nIn front of you, the stream widens into a gushing river",
            "towards the South, before falling over a dark ledge into a ravine that seems to",
            "stretch on for ever! A small rowing boat is straining against",
            "a rope. Will you get in the boat and go South down the waterfall,",
            "or will you go back West and try to find another route?")

        rinput = input("N, S, E, W?: ").upper()
        if rinput == 'N':
            print ("You walk into a wall!")
        elif rinput == 'S':
            room4()
        elif rinput == 'E':
            print ("You walk into a wall!")
        elif rinput == 'W':
            print ("You walk back into the previous corridor.")
            room2()

    def room2():
        print ("\nLooking around, you see a dank corridor, with walls of",
        "patterened green marble, covered with slimey moss. There are torches",
        "on the wall which cast flickering shadows of you all around. A small",
        "underground stream gushes past in a deep gouge in the rock,",
        "heading towards the Eastern exit. The roaring sound is louder",
        "here. There are exits behind you, to the West, and in front of you,",
        "to the East.")

        rinput = input("N, S, E, W?: ").upper()
        if rinput == 'N':
            print ("You walk into a wall!")
        elif rinput == 'S':
            print ("You walk into a wall!")
        elif rinput == 'E':
            room3()
        elif rinput == 'W':
            print ("\nYou walk back into the previous room.")
            room1()

    def room1():
        print ("\nYou're in a dark cave, which is only illuminated",
       "by glowing lichen on the walls. There is no exit behind",
       "you, you're trapped. There are exits East and South.",
       "There are stalagtites hanging down from the ceiling,",
       "and a constant drip of water trickling down the walls.",
       "To the East you can hear a deep roar. To the South is silence.",
       "Which way will you go?")

        rinput = input("N, S, E, W?: ").upper()
        if rinput == 'E':
            room2()
        elif rinput == 'W':
            print ("\n you walk into a wall!")
        elif rinput == 'S':
            print ("Placeholder")
        elif rinput == 'N':
            print ("You walk into a wall")
#The code prints room1, which kicks off the whole game.
    room1()

#the function of the readme for the game. Probably will be re-written, just a placeholder for now.
def readme():
    print ("\nHey! I'm the readme file for this project. ",
    "This is (as you probably know!) a ",
    "basic text-based maze game written in ",
    "Python3. The game is fairly simple. Commands",
    "are just North, South, East or ",
    "West - N, S, E, W. You can view this at any ",
    "time by typing \"Help\"")
#the menu itself now. I'm actually thinking I might just add another function for the menu to run off.
print ("Menu")
print ("Play, Help, Quit")
rinput = input("Enter one of the options:").upper()

if rinput == 'HELP':
    readme()

elif rinput == 'QUIT':
    print ("\nBye!")

elif rinput == 'PLAY':
    game()

