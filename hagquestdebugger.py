from sys import exit
import random

#------------------------------------------------------------------------------
#---------------------------START FUNCTION-------------------------------------
#------------------------------------------------------------------------------
#--------------------called when the game starts-------------------------------

#this is REALLY badly formatted. but it works so i wont touch it
def start():

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
potion = Item("Super Magic Cleaning Potion", "A tiny bottle containing a sparkling, iridescent liquid. "+"The virility of this potion is undeniable.")

feather_duster = Item("Feather Duster", "The hag said this was magical, but it looks like a regular feather duster to you. Guess that's why you're not a hag.")

sword = Item("Sword", "Your sword. Long, thin and metal. You bought it from a used sword shop, but the dealer assured you it works like new.")

spider = Item("Spider", "This spider has webs covering the entirety of the hag's cabinet and looks incredibly venomous. Probably best not to approach.")

watch = Item("Pocketwatch", "Covered in grime, but tells the time well enough.")

box = Item("Terrarium", "Looks like a good home for any small-to-medium sized pet.")

key = Item("Key", "Nondescript key. Probably fits a lock somewhere. Otherwise, what's the point?")

knife = Item("Knife", "A... a sharp, glimmering knife. What are you planning to do with that?!")

vacuum = Item("Magic Vacuum", "\"The Super-Sucker 5000 -- the ultimate in cleaning technology, straight from the Plane of Air to your living room!\"")

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

house = [hags_kitchen,hags_livingroom,alley]

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

def quitGame(name,description,exits,items,command):
	print "Goodbye, quitter!\n"
	exit()

def laugh(name,description,exits,items,command):
	print """
		You'd laugh, but you're Jarek Lenda. You remember what your father
		always told you... \"Son! Don't laugh at hags!\"
		That's asking for trouble!\n
		"""

def look(name,description,exits,items,command):
	print name

	print description

	for item in items:
		print "There is a " + item.name.lower() + " here.\n"

	for exit in exits["valid exits"]:
		print "There is an exit to the " + exit + " here.\n"

def checkInventory(name,description,exits,items,command):
	 for item in inventory:
				print item.name

def helpMe(name,description,exits,items,command):
	print "Here are the functions you can use:"
	for d in actionDict:
		print d



#----------------------------DIRECTION FINDER----------------------------------
#parses the player's input to see if they're trying to move in a direction, and
#returns correct response
def direction_finder(name,description,exits,items,command):
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
def item_getter(name,description,exits,items,command):
	foundItem = False
	for item in items:
		if item.name.lower() in command:
			inventory.append(item)
			for room in house:
				if room.name == name:
					room.items.remove(item)
					foundItem = True
					print "You took the %s." % item.name

	if foundItem == False:
		print "I guess you can't %s" % command

#--------------------------------Action Dictionary----------------------------------------

actionDict =    {"exit game":quitGame,"quit game":quitGame,"laugh":laugh,"look":look,"-i":checkInventory,"take":item_getter,
				"get":item_getter,"pick up":item_getter,"east":direction_finder,"west":direction_finder,"north":direction_finder,
				"south":direction_finder,"help":helpMe}


#--------------------------------Invalid Inputs----------------------------------------
#fun responses for when the parser cant parse what the player put in
invalid_input = ["No... Think! What would a Lenda do?!\n",
	"You consider the idea briefly, then discard it. There's got to be a better way...\n",
	"As if. If you'd only paid attention in hag-banishing class, you wouldn't be in this situation.\n",
	"Sorry, but... what? How would that help at all?\n",
	"That won't work... You wish you were back home with Schuyler and Zeke...\n",
	"Maybe? No, no, time to stop fooling around.\n"]

#-------------------------------------------------------------------------------
#--------------------------------PARSERS----------------------------------------
#-------------------------------------------------------------------------------
#----------parse player input for rooms, items, etc-----------------------------
#-------------------------------------------------------------------------------

#------------------------------ROOM PARSER--------------------------------------
#this parser parses what actions can be done to basically anything at this point
def roomparse(name,description,exits,items):

	#so... always
	while 1:

		#the beginning of each run asks the player for their input
		command = raw_input("> ").lower()

		validInput = False

		for d in actionDict:
			if d in command:
				actionDict[d](name,description,exits,items,command)
				validInput = True
				house = [hags_kitchen,hags_livingroom,alley]
				break

		if not validInput:
			print random.choice(invalid_input)



#finally, starting the game up
start()
