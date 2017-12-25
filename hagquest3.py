from sys import exit
import random

#------------------------------------------------------------------------------
#---------------------------START FUNCTION-------------------------------------
#------------------------------------------------------------------------------
#--------------------called when the game starts-------------------------------

#this is REALLY badly formatted. but it works so i wont touch it
def start():

    prompt = "> "

    print """
You stand at the edge of a vast desert.
Sandstorms whirl around like miniature tornadoes.
Inside you see massive, monstrous shapes moving about.
A withered hag waddles out in front of you.
"EHEHEHEEEE, what is your name small boy??"
    """
    username = raw_input(prompt)

    if username.lower() == "jarek lenda":
        print """
Hmmm, %s, eh?? You sound like a nice young boy.
Well, %s, I hope you're not thinking of exploring...
The desert!!
EHEHEHEHE, many people more courageous and attractive than you have tried...
and failed!!
What makes you think you have what it takes, \'%s\'??
If that is your real name???
        """ % (username, username, username)

    elif (username.lower() == "" or username.lower() == " "):
        print """
The hag screeches and rips you to shreds, displeased by your silence!
You die, nameless wanderer!
              """
        exit()

    else:
        print """
The hag screeches and rips you to shreds, displeased by your name.
You die, %s!
              """ % username
        exit()

    reason = raw_input(prompt)

    print """
The hag isn't really listening. The hag laughs. \"EHEHEHEEEE, as if that will get you through!
No, you'll need a \n~hag\'s help~\nif you\'ve any chance of succeeding! Don't worry,
though, %s, I'll help you out... Just as soon as you help me! This way, this way!\"\n
    """ % username

    raw_input("PRESS ENTER")

    print """
The hag leads you to a nearby apartment complex. \"EHEHEHEEEE, this is
where I live! On the first floor, because I was here first! Me! I'm number one!!\"
She shouts up to the other windows \"BETTER PAY YOUR RENT SOON OR I\'LL REPORT YOU
TO THE LANDLORD, GOOD FOR NOTHINGS!!\" The hag leads you through a door, through an anteroom and
into a messy kitchen. \"Here's the deal...\", says the hag, \"my apartment is a mess!!
I need a strapping young man like you to help me clean it. But there aren't ordinary messes,
oh no. These messes are absolutely... \n~hagalicious~!\nAs such, no normal means of cleaning them will do.\n"""

    raw_input("PRESS ENTER")

    print """
\"First, there are my dishes. I had a super magic cleaning
potion in my secret portal behind the fridge... but the fridge is broken and you're not
allowed to move it til it's fixed! Then, there's my display cabinet in the living room.
I had a magic feather duster... But I don't know where it went. Find it and dust it!
You've also got to vacuum my rug in the bedroom, of course, but good luck with that. I don't
even have a vacuum, and it's not like my good for nothing neighbor will let me borrow his.
Finally, take out my garbage. It stinks. Good luck!!\" You turn to question the hag, but
she's already fled out the front door and you hear a key turn in the lock. \"I'll be back
in an hour!\" she says. \"Make sure my house is spick and span -- or else I'll give you a\n
~hagalicious~\n
beating!!!!!\" Her footsteps fade, and you sense you are alone.\n\n
------------------------------------HAGQUEST------------------------------------\n\n\n\n
To quit, enter \"quit game\".\n\n\n\n"""

    enter(hags_kitchen)

#-------------------------------------------------------------------------------
#-------------------------------CLASSES-----------------------------------------
#-------------------------------------------------------------------------------


#----------------------------ROOMS----------------------------------------------

class Room(object):
    """Parent class for every area."""
    # what do we need in a room?
    # a description of the room, the items in the room,
    # a list of commands that can occur in a room
    # and the exits from the room
    def __init__(self,name,description,exits,items):
        #name of the room
        self.name = name
        #the description
        self.description = description
        #an array of exits, valid and invalid
        self.exits = exits
        #an array of the objects located in the room
        self.items = items


#---------------------------------ITEMS-----------------------------------------
# items are their own class
class Item(object):
    """Parent class for every item."""
    # items have a name, a description and a list of commands that apply to them
    def __init__(self,name,description):
        #name of the item
        self.name = name
        #description of the item
        self.description = description
        #when its created put it into the item dictionary


#---------------------------THE PLAYER------------------------------------------
#the player is their own class
class Player(object):
    pass

#-------------------------------------------------------------------------------
#---------------------------------ITEMS-----------------------------------------
#------------------------------List of items in the game------------------------
potion = Item("Super Magic Cleaning Potion", "A tiny bottle containing a sparkling, iridescent liquid. "+"The virility of this potion is undeniable."
            )

feather_duster = Item("Feather Duster", "The hag said this was magical, but it looks like a regular feather duster to you. Guess that's why you're not a hag."
            )

sword = Item("Sword", "Your sword. Long, thin and metal. You bought it from a used sword shop, but the dealer assured you it works like new."
            )

spider = Item("Spider", "This spider has webs covering the entirety of the hag's cabinet and looks incredibly venomous. Probably best not to approach."
            )


watch = Item("Pocketwatch", "Covered in grime, but tells the time well enough."
            )

box = Item("Terrarium", "Looks like a good home for any small-to-medium sized pet."
            )

key = Item("Key", "Nondescript key. Probably fits a lock somewhere. Otherwise, what's the point?"
            )

knife = Item("Knife", "A... a sharp, glimmering knife. What are you planning to do with that?!"
            )

vacuum = Item("Magic Vacuum", "\"The Super-Sucker 5000 -- the ultimate in cleaning technology, straight from the Plane of Air to your living room!\""
            )

#-------------------------------------------------------------------------------
#-----------------------------------ROOMS---------------------------------------
#---------------------------list of rooms in the game---------------------------

hags_kitchen = Room("Hag's Kitchen","""\n\n
A greasy old kitchen which has seen better days - or maybe not. The dishes are
stacked high, almost to the ceiling, and have started to ooze out onto the
floor. The refrigerator is flickering and sparking ominously. Most of the
cupboards and drawers are either missing or chocked full of what look like
noxious magical ingredients. Only one of the drawers looks like it's in working
condition. Windows on the west wall open out onto a dismal alley. The ceiling
fan still works, though, so there's that. You find the slight breeze rather
refreshing.\n""",
{"valid exits" : ["east","west"], "invalid exits" : ["north","south","northeast","southeast","northwest","southwest"]},
[watch,knife])

hags_livingroom = Room("Hag's Living Room","""
\n\nIt looks as if someone made it their goal to come here every day of their life
and neglect this room. It\'s filled with a kind of tarry, viscous smoke of
unidentifiable origin which, sadly, does not prevent you from seeing how filthy
it is. The wallpaper is old, peeling and stained a sort of blackish purple, with
any pattern that had been there before now hidden. There is a TV in the corner
which seems to be switching between static and what appears to be some sort of
informercial. There is a purple recliner facing the TV, with a hag-shaped
indentation in the seat. Against the far wall is what has to be the oldest,
saggiest display cabinet you've ever seen. Perhaps the purpose was originally to
display cobwebs, but you doubt it -- regardless, that's what it is displaying
now, with a huge, nasty looking spider glaring at you from inside.\n""",
{"valid exits" : ["west"], "invalid exits" : ["north","south","northeast","southeast","northwest","southwest","east"]},
[spider])

alley = Room("Alley","""\n\nA long, narrow, alley about twenty feet wide which is bricked
up on either end, throwing everything into shadow. You are at one end of the alley,
and at the other end you think you can see a dumpster (who puts a dumpster in a
bricked up alley?? How does the garbageman even get it????) It's hard to tell,
of course, because between you and the dumpster is a huge dragon.\n""",
{"valid exits" : ["east"], "invalid exits" : ["north","south","northeast","southeast","northwest","southwest","west"]},
[])

#------------------------------------------------------------------------------
#---------------------------GLOBAL VARIABLES-----------------------------------
#------------------------------------------------------------------------------

#dictionary of all items in game with name as key to object
item_dict = {}

#dictionary of all rooms in game with name as key to room

#one's inventory, should be able to check it with "i"
inventory = [sword]

#list of commands possible for items
#item_commands =

#------------------------------------------------------------------------------
#---------------------------GLOBAL FUNCTIONS-----------------------------------
#------------------------------------------------------------------------------

#--------------------------------ENTER-----------------------------------------
#this is called when entering a new room and for the first time when the game
#is started
#loads up the room
def enter(room):
    #prints room name
    print room.name
    #prints the room description
    print room.description
    #prints a list of items in the room
    for item in room.items:
        print "There is a " + item.name.lower() + " here.\n"
    #prints a list of available exits in the room
    for exit in room.exits["valid exits"]:
        print "There is an exit to the " + exit + " here.\n"

    #this calls the parser that interacts with the "Room" objects
    roomparse(room.name,room.description,room.exits,room.items)

#----------------------------DIRECTION FINDER----------------------------------
#parses the player's input to see if they're trying to move in a direction, and
#returns correct response
def direction_finder(command,name,exits):
    #for the dictionary of invalid and valid exits brought over from the "room" objects
    for i in exits["valid exits"]:
        #if any movement keywords related to the valid exits exist we go that way and call up the enter function
        if (command == "%s" % i or command == "go %s" % i or command == "move %s" % i or command == "walk %s" % i)\
                and name == "Hag's Kitchen":

            if "west" in command:
                print "You go West.\n"

                enter(alley)

            elif "east" in command:
                print "You go East.\n"

                enter(hags_livingroom)
        elif (command == "%s" %i or command == "go %s" % i or command == "move %s" % i or command == "walk %s" % i)\
                and name == "Alley":

            print "You go East.\n"

            enter(hags_kitchen)

        elif (command == "%s" %i or command == "go %s" % i or command == "move %s" % i or command == "walk %s" % i)\
                and name == "Hag's Living Room":
            if "west" in command:

                print "You go West.\n"

                enter(hags_kitchen)

#---------------------------ITEM_GETTER-----------------------------------------
#checks to see if an item is in the room and gettable; if so, removes from room
#and adds to inventory
def item_getter(command,items):
    for item in items:
        if item.name.lower() in command:
            #add the object to the list however i do that
            #how to stop a for loop when i hit the one that i want
            #a for loop that only searches for one thing
            #and then does a different function on the rest
            #i could just make a tiny different function that's called here which
            #prints the description for the rest of the is

            #i could record its index?

            #i could even do another for loop
            #"for item.name.lower() not in command"
            #yeah! dude! YOU ROCK!!!!!!
        else:
            print "I don't see a %s here." % item


#-------------------------------------------------------------------------------
#--------------------------------PARSERS----------------------------------------
#-------------------------------------------------------------------------------
#----------parse player input for rooms, items, etc-----------------------------
#-------------------------------------------------------------------------------

#------------------------------ROOM PARSER--------------------------------------
#this parser parses what actions can be done to basically anything at this point
def roomparse(name,description,exits,items):

    """Parses actions."""

    #fun responses for when the parser cant parse what the player put in
    invalid_input = ["No... Think! What would a Lenda do?!\n",
    "You consider the idea briefly, then discard it. There's got to be a better way...\n",
    "As if. If you'd only paid attention in hag-banishing class, you wouldn't be in this situation.\n",
    "Sorry, but... what? How would that help at all?\n",
    "That won't work... You wish you were back home with Schuyler and Zeke...\n",
    "Maybe? No, no, time to stop fooling around.\n"]

    #so... always
    while 1:

        #the beginning of each run asks the player for their input
        command = raw_input("> ").lower()

        #this calls direction_finder on the player's input to see if the player
        #is trying to move rooms
        direction_finder(command,name,exits)

        #if a taking or getting keyword is in the input, calls up the function
        #for taking items
        if ("take" in command or "get" in command or "pick up" in command):
            item_getter(command, items)

        #command to pull up one's inventory
        if command == "i":
            for item in inventory:
                print item.name

        #"look" restates the description, a list of exits and any items in the
        #room
        if command == "look":
            print name

            print description

            for item in items:
                print "There is a " + item.name.lower() + " here.\n"

            for exit in exits["valid exits"]:
                print "There is an exit to the " + exit + " here.\n"

        #just a fun command if someone tries laughing
        #laughing makes you live longer, you know
        #i like making my code more complicated for no reason
        elif command == "laugh":
            print """
            You'd laugh, but you're Jarek Lenda. You remember what your father
            always told you... \"Son! Don't laugh at hags!\"
            That's asking for trouble!\n
            """

        #quit game
        elif (command == "exit game" or command == "quit game"):
            print "Goodbye, quitter!\n"
            break

        #naything else the parser fills in with stock "does not compute" phrases
        #NOT WORKING FOR SOME REASON, QUARANTINE
        #else:
        #    print random.choice(invalid_input)



#finally, starting the game up
start()