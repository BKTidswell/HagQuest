from sys import exit
import random

#this parser needs a list of what actions can be done to rooms
#then one for what can be done to objects...? maybe that wouldnt work
def roomparse(description,exits,objects):

    invalid_input = ["No... Think! What would a Lenda do?!\n",
    "You consider the idea briefly, then discard it. There's got to be a better way...\n",
    "As if. If you'd only paid attention in hag-banishing class, you wouldn't be in this situation.\n",
    "Sorry, but... what? How would that help at all?\n",
    "That won't work... You wish you were back home with Schuyler and Zeke...\n"]

    while 1:

        command = raw_input("> ").lower()

        if command == "look":
            print description

        elif command == "laugh":
            print """You'd laugh, but you're Jarek Lenda. You remember what your father
always told you... \"Son! Don't laugh at hags!\" That's asking for trouble!\n"""

        elif command == "exit":
            break

        else:
            print random.choice(invalid_input)

class Room(object):
    """Parent class for every area."""
    # what do we need in a room?
    # a description of the room, the items in the room,
    # and the exits from the room
    def __init__(self,name,description,exits,objects):
        #name of the room
        self.name = name
        #the description
        self.description = description
        #an array of exits
        self.exits = exits
        #an array of the objects located in the room
        self.objects = objects

        #can call this every time someone enters a given room
        #or when someone uses the "look" command
    def enter(self):

        print self.description

        for member in self.objects:
            print "There is a " + member + " here.\n"

        for exit in self.exits:
            print "There is an exit to the " + exit + " here.\n"

        #really simple (atm) function that parses the results of the player's input
        #in limited ways
        #HOW DO I GET IT TO
        roomparse(self.description,self.exits,self.objects)


hags_kitchen = Room("Hag's Kitchen","""Hag's Kitchen\nA greasy old kitchen which has seen better days - or maybe not.
The dishes are stacked high, almost to the ceiling, and have started to ooze
out onto the floor. The refrigerator is flickering and sparking ominously.
Most of the cupboards and drawers are either missing or chocked full of what look
like noxious magical ingredients. Windows on the west wall open out onto a dismal alley.
The ceiling fan still works, though, so there's that.
You find the slight breeze rather refreshing.\n""",
["North","South"],
["watch","knife"])

#print hags_kitchen.description
#print hags_kitchen.exits
#print hags_kitchen.objects
hags_kitchen.enter()
