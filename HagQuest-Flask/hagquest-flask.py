from sys import exit
import random
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

talkerCounter = 0

global history
history = ""

#------------------------------------------------------------------------------
#---------------------------GLOBAL FUNCTIONS-----------------------------------
#------------------------------------------------------------------------------

#--------------------------------ENTER-----------------------------------------
#this is called when entering a new room and for the first time when the game
#is started
#loads up the room
def enter(room,command):
	global history 
	#prints room name
	#history += "\n" + room.name
	#prints the room description
	#history += "\n" + room.description
	#prints a list of items in the room
	#for item in room.items:
	#	if item.takable:
	#		history += "\n" + "There is a " + item.name.lower() + " here.\n"
	#prints a list of available exits in the room
	#for exit in room.exits["valid exits"]:
	#	history += "\n" + "There is an exit to the " + exit + " here.\n"

	#this calls the parser that interacts with the "Room" objects
	return roomparse(room.name,room.description,room.exits,room.items,room,command)


#--------------------------------User Response-----------------------------------

def quitGame(name,description,exits,items,command,room):
	global history 
	history += "\n" + "Goodbye, quitter!\n"
	exit()

def laugh(name,description,exits,items,command,room):
	global history 
	history += "\n" + """
		You'd laugh, but you're Jarek Lenda. You remember what your father
		always told you... \"Son! Don't laugh at hags!\"
		That's asking for trouble!\n
		"""

def look(name,description,exits,items,command,room):
	global history 
	history += "\n" + name

	history += "\n" + description

	for item in items:
		if item.takable:
			history += "\n" + "There is a " + item.name.lower() + " here.\n"

	for exit in exits["valid exits"]:
		history += "\n" + "There is an exit to the " + exit + " here.\n"

def checkInventory(name,description,exits,items,command,room):
	global history 
	for item in inventory:
				history += "\n" + "You have a " + item.name

def helpMe(name,description,exits,items,command,room):
	global history 
	history += "\n" + "Here are the functions you can use:"
	for d in actionDict:
		history += "\n" + d

def item_adder(item,roomName):
	for room in house:
		if room.name == roomName:
			usingRoom = room
			break
	usingRoom.items.append(item)

def item_remover(item,roomName):
	for room in house:
		if room.name == roomName:
			usingRoom = room
			break
	if item in usingRoom.items:
		usingRoom.items.remove(item)

def item_invent_adder(itemName,eh):
	for item in allItems:
		if item.name == itemName:
			inventory.append(item)
			return

def item_invent_remover(itemName,eh):
	for item in inventory:
		if item.name == itemName:
			inventory.remove(item)
			return

def room_description_changer(description,roomName):
	for room in house:
		if room.name == roomName:
			usingRoom = room
			break
	usingRoom.description = description

def item_description_changer(description,itemName):
	for item in allItems:
		if item.name == itemName:
			usingItem = item
			break
	usingItem.description = description

def usage_descriptor(description,eh):
	global history 
	history += "\n" + description

def spider_adder(roomName,numSpiders):
	for room in house:
		if room.name == roomName:
			usingRoom = room
			break
	for x in range(numSpiders):
		usingRoom.items.append(spider)

def manTalker(name,description,exits,items,command,room):
	global history 
	global talkerCounter
	if room.name == "Backyard":
		if vacuum in inventory:
			history += "\n" + "The man waves to you. \"Thanks and good luck!\" he shouts."
		elif talkerCounter == 0:
			history += "\n" + """The man scowls at you. \"What do you want?? You're one of the hag's cronies, aren'tcha?
			Well whatever you want I'm not interested. This hag blocked my door with her stupid pool, and
			now I'm stuck here. I didn't plan to leave home anyway, but I'm just so lonely... I wish I had
			some sort of friend or pet or something. But instead all I get are you suckers coming to do her
			chores!! Well, push off. I'm not helping you clean.\"\n"""
			talkerCounter = 1
		elif talkerCounter == 1:
			history += "\n" + """The man scoffs at you. \"Didn't I already tell you to get lost? What, are you after my
			vacuum? Well, like I said, you can forget it. That hag is why I'm so lonely and friendless, and
			I don't plan to help her any time soon!\n"""
			talkerCounter = 2
		else:
			history += "\n" + "The man doesn't say anything, just flips you off. He definitely needs a friend.\n"
	else:
		history += "\n" + "There's no one here to talk to. You mumble to yourself a little.\n"



#----------------------------DIRECTION FINDER----------------------------------
#parses the player's input to see if they're trying to move in a direction, and
#returns correct response
def direction_finder(name,description,exits,items,command,room):
	global history 
	#for the dictionary of invalid and valid exits brought over from the "room" objects
	for i in exits["valid exits"]:
		#if any movement keywords related to the valid exits exist we go that way and call up the enter function
		if (command == "%s" % i or command == "go %s" % i or command == "move %s" % i or command == "walk %s" % i)\
				and name == "Hag's Kitchen":

			if "west" in command:
				history += "\n" + "You go West.\n"
				return alley

			elif "east" in command:
				history += "\n" + "You go East.\n"
				return hags_livingroom

		elif (command == "%s" %i or command == "go %s" % i or command == "move %s" % i or command == "walk %s" % i) and name == "Alley":

				history += "\n" + "You go East.\n"
				return hags_kitchen

		elif (command == "%s" %i or command == "go %s" % i or command == "move %s" % i or command == "walk %s" % i) and name == "Hag's Living Room":

			if "west" in command:
				history += "\n" + "You go West.\n"
				return hags_kitchen

			elif "east" in command:
				history += "\n" + "You go East.\n"
				return hags_bedroom

			elif "north" in command:
				history += "\n" + "You go North.\n"
				return hags_backyard

		elif (command == "%s" %i or command == "go %s" % i or command == "move %s" % i or command == "walk %s" % i)\
				and name == "Hag's Bedroom":

			if "west" in command:
				history += "\n" + "You go West.\n"
				return hags_livingroom

		elif (command == "%s" %i or command == "go %s" % i or command == "move %s" % i or command == "walk %s" % i)\
				and name == "Backyard":

			if "south" in command:
				history += "\n" + "You go South.\n"
				return hags_livingroom

	history += "\n" + "You can't go %s.\n" % command
	return room

#---------------------------ITEM_GETTER-----------------------------------------
#checks to see if an item is in the room and gettable; if so, removes from room
#and adds to inventory
def item_getter(name,description,exits,items,command,room):
	global history 
	for item in items:
		if item.name.lower() in command and item.takable:
			inventory.append(item)
			for room in house:
				if room.name == name:
					room.items.remove(item)
					history += "\n" + "You took the %s." % item.name
					return

	history += "\n" + "I guess you can't %s." % command

#---------------------------ITEM_DROPPER-----------------------------------------
#checks to see if an item is in the room and gettable; if so, removes from room
#and adds to inventory
def item_dropper(name,description,exits,items,command,room):
	global history 
	for item in allItems:
		if item.name.lower() in command and item in inventory:
			inventory.remove(item)
			for room in house:
				if room.name == name:
					room.items.append(item)
					history += "\n" + "You dropped the %s." % item.name
					return

	history += "\n" + "I guess you can't %s" % command

#---------------------------Item User-----------------------------------------
#checks to see if item can be used in the room, if so uses it.

def item_user(name,description,exits,items,command,room):
	global history 
	splitcommand = command.split(" ")
	usingName = splitcommand[1]

	itemExists = False
	haveItem = False
	usable = False

	for item in allItems:
		if usingName.lower() in item.name.lower():
			usingItem = item
			itemExists = True
			break

	if not itemExists:
		history += "\n" + "%s doesn't exist....." % usingName
		return

	if usingItem in inventory:
		haveItem = True

	if not haveItem:
		history += "\n" + "You don't have a %s......" % item.name
		return

	targetName = raw_input("What do you want to use the %s on? \n > "% item.name).lower()

	isTarget = False
	inRoom = False

	for item in allItems:
		if targetName.lower() in item.name.lower():
			targetItem = item
			isTarget = True
			break

	if not isTarget:
		history += "\n" + "%s doesn't exist......" % targetName
		return

	if targetItem == spider and usingItem == spider:
		spider_adder(name,random.randint(2,10))
		history += "\n" + "Spiders appeared!!!!"
		return

	if targetItem in items:
		inRoom = True

	if not inRoom:
		history += "\n" + "%s isn't here....." % targetItem.name
		return

	for k in targetItem.usages:
		if k.name == usingItem.name:
			funcArray = targetItem.usages[usingItem]
			for x in range(0,len(funcArray),2):
				funcArray[x](funcArray[x+1][0],funcArray[x+1][1])
			return

	history += "\n" + "You used the %s on the %s. But. Nothing happened..." % (usingItem.name,targetItem.name)


#---------------------------ITEM LOOKER-----------------------------------------
#for examining items/objects
#to do - better function name than item looker????
def item_looker(name,description,exits,items,command,room):
	global history 
	for item in items:
		if command.split(" ")[1] in item.name.lower():
			if item in inventory:
				history += "\n" + item.description
				return
			for room in house:
				if room.name == name:
					history += "\n" + item.description
					return

	history += "\n" + "Eh? You don't see that here."


#------------------------------------------------------------------------------
#---------------------------Hag Start Phrases----------------------------------
#------------------------------------------------------------------------------


hagSpeech1 = """
You stand at the edge of a vast desert.
Sandstorms whirl around like miniature tornadoes.
Inside you see massive, monstrous shapes moving about.
A withered hag waddles out in front of you.
"EHEHEHEEEE, what is your name small boy??"
	"""

def hagSpeech2(username):
	return """
	Hmmm, %s, eh?? You sound like a nice young boy.
	Well, %s, I hope you're not thinking of exploring...
	The desert!!
	EHEHEHEHE, many people more courageous and attractive than you have tried...
	and failed!!
	What makes you think you have what it takes, \'%s\'??
	If that is your real name???
	""" % (username, username, username)

def hagSilentMurder(username):
	return """
	The hag screeches and rips you to shreds, displeased by your silence!
	You die, nameless wanderer!
			  """
def HagMurder(username):
	return """
	The hag screeches and rips you to shreds, displeased by your name. If only you had been named Jarek Lenda!!!
	You die, %s!
	""" % username

def hagSpeech3(username):
	return """
	The hag isn't really listening. The hag laughs. \"EHEHEHEEEE, as if that will get you through!
	No, you'll need a \n~hag\'s help~\nif you\'ve any chance of succeeding! Don't worry,
	though, %s, I'll help you out... Just as soon as you help me! This way, this way!\"\n\n "PRESS SUBMIT" 
		""" % username

def hagSpeech4(username):
	return """
	The hag leads you to a nearby apartment complex. \"EHEHEHEEEE, this is
	where I live! On the first floor, because I was here first! Me! I'm number one!!\"
	She shouts up to the other windows \"BETTER PAY YOUR RENT SOON OR I\'LL REPORT YOU
	TO THE LANDLORD, GOOD FOR NOTHINGS!!\" The hag leads you through a door, through an anteroom and
	into a messy kitchen. \"Here's the deal...\", says the hag, \"my apartment is a mess!!
	I need a strapping young man like you to help me clean it. But there aren't ordinary messes,
	oh no. These messes are absolutely... \n~hagalicious~!\nAs such, no normal means of cleaning them will do.\n\n "PRESS SUBMIT"
	"""

def hagSpeech5(username):
	return """
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
	def __init__(self,name,description,takable,usages):
		#name of the item
		self.name = name
		#description of the item
		self.description = description
		#when its created put it into the item dictionary
		self.takable = takable
		#determine if you can take it
		self.usages = usages
		#dictionary of tools that you can use with it



#---------------------------THE PLAYER------------------------------------------
#the player is their own class
class Player(object):
	pass

#-------------------------------------------------------------------------------
#---------------------------------ITEMS-----------------------------------------
#------------------------------List of items in the game------------------------
potion = Item("Super Magic Cleaning Potion", "A tiny bottle containing a sparkling, iridescent liquid. "+"The virility of this potion is undeniable.",
	True,{})

feather_duster = Item("Feather Duster", "The hag said this was magical, but it looks like a regular feather duster to you. Guess that's why you're not a hag.",
	True,{})

sword = Item("Sword", "Your sword. Long, thin and metal. You bought it from a used sword shop, but the dealer assured you it works like new.",
	True,{})

spider = Item("Spider", "This spider has webs covering the entirety of the hag's cabinet and looks incredibly venomous. Probably best not to approach.",
	True,{})

watch = Item("Pocketwatch", "Covered in grime, but tells the time well enough.",
	True,{})

key = Item("Key", "Nondescript key. Probably fits a lock somewhere. Otherwise, what's the point?",
	True,{})

knife = Item("Knife", "A... a sharp, glimmering knife. What are you planning to do with that?!",
	True,{})

vacuum = Item("Vacuum", "\"The Super-Sucker 5000 -- the ultimate in cleaning technology, straight from the Plane of Air to your living room!\"",
	True,{})

terrarium = Item("Terrarium", "Looks like the perfect home for any small-to-medium-sized reptile, amphibian, insect or gnome.",
	True,{spider:[usage_descriptor,["You open up the terrarium and show it to the spider. She happily jumps in and makes herself at home!"],
						item_invent_adder,["Spider Box","eh"],
						item_invent_remover,["Spider","eh"],
						item_invent_remover,["Terrarium","eh"]]})

telephone_book = Item("Book", "A telephone book with only one number 1,000 times?? It's for a fridge repairman.",
	True,{})

hammer = Item("Hammer of Radiant Light", "Holy light shines out of this hammer. Powerful enoguh to defeat any evil. Or annoyance.",
	True,{})

trash = Item("Trash", "It's a hag's trash. I wouldn't look in if I were you -- definitely not EPA approved.",
	True,{})

ladder = Item("Ladder", "Hag's ladder. The rungs spell out H A G. Not convenient or even safe, but definitely stylish.",
	True,{})

tv = Item("TV", "You can barely see anything through the static on this TV. It looks like some sort of informercial? Starring a dwarf?",
	False,{})

portable_forge = Item("Forge", "It's the latest and greatest in portable blacksmithing -- though honestly, portable blacksmithing hasn't come far.",
	True,{})

spider_box = Item("Spider Box", "It's the terrarium with the spider inside. She looks happy here, making webs and... you know, other spider things.",
	True,{})

ceiling_fan = Item("Ceiling Fan", "A pretty pristine ceiling fan. It's set to the highest setting, creating a strong breeze. Colder definitely is better!",
				False,{})

chair = Item("Recliner", "It's a tiny purple recliner, though the lever seems to be broken. The seat has molded perfectly to the hag's butt.",
			False, {})

rusty_hammer = Item("Rusty Hammer", "A rusty hammer. Looks like it's been used for breaking nuts.",
	True,{portable_forge:[usage_descriptor,["You throw the hammer in and forge all the rust off it. It's beautiful enough to make you weep.","eh"],
						   item_invent_adder,["Hammer of Radiant Light","eh"],
						   item_invent_remover,["Rusty Hammer","eh"]]})

cabinet = Item("Cabinet", "A dusty cabinet.",
	False,{feather_duster:[usage_descriptor,["""
	You steel yourself and get to dusting. It\'s like your father always said -
	\"Son, if you cannot dust a hag\'s cabinets then you will never be successful
	in your chosen career, whatever it may be, though if you want to be an actor
	or something silly like that I will still love you as my son.\"
	A man of few words, but wise ones, truly.
	Your dusting knocks webs left and right, and the spider tumbles to the floor.
	On the ground, she doesn't look so venomous or dangerous at all - must have
	been the webs.
	Finally, the cabinets are as beautiful as they were when first made. You see
	the metallic gleaming was a key lying on the bottom shelf!\n
	""","eh"],
	item_adder,[spider,"Hag's Living Room"],
	item_adder,[key,"Hag's Living Room"],
	item_description_changer,["A clean cabinet","Cabinet"],
	item_description_changer,["This spider actually looks rather nice and friendly -- must've been the webs. She waves at you.","Spider"],
	room_description_changer,["""\n\n
	It looks as if someone made it their goal to come here every day of their life
	and neglect this room... but now it's a little better. It\'s filled with a kind of tarry, viscous smoke of
	unidentifiable origin which, sadly, does not prevent you from seeing how filthy
	it is. The wallpaper is old, peeling and stained a sort of blackish purple, with
	any pattern that had been there before now hidden. There is a TV in the corner
	which seems to be switching between static and what appears to be some sort of
	informercial. There is a purple recliner facing the TV, with a hag-shaped
	indentation in the seat. Against the far wall is what has to be the oldest,
	saggiest display cabinet you've ever seen. Since the dusting, though, you've
	come to appreciate more. It's not old and saggy, it's... antique. Yeah.\n
	""","Hag's Living Room"]]})

dishes = Item("Dishes", "Some dirty dishes.",
	False,{potion:[usage_descriptor,["You slowly, slowly, s l o w l y uncork the. "+
	"bottle and let a single drop of the potion fall onto the nearest of the dirty "+
	"dishes. When you can see and hear again and have made sure all your limbs "+
	"are still in place, you realize all the dishes are not only clean, but "+
	"stacked in neat little rows! The salad forks and entree forks have even "+
	"been separated! Truly magic is still alive in this world. Another chore down!\n","eh"],
				   item_description_changer,["You can better appreciate the dishes now that they're clean. The hag has an impressive collection of Fiestaware.","Dishes"],
				   room_description_changer,["""\n
				   A significantly less greasy old kitchen which has seen better days -
				   but they're not as far distant now. The dishes are
				   stacked high, almost to the ceiling, but they are beautiful
				   stacks of clean-looking diningware instead of the mess they were before.
				   The refrigerator is fixed and is humming smoothly, though the food has
				   gone bad. Most of the cupboards and drawers are either missing or chocked
				   full of what look like noxious magical ingredients.
				   The only working drawer is open and empty. Against the wall is a grimy phone,
				   though it looks like the numbers 9 and 1 have been removed. Windows on the
				   west wall open out onto a dismal alley. The ceiling fan still works,
				   and it's still blowing a mighty fine breeze. You bask a bit.\n""","Hag's Kitchen"]]})

garbage_can = Item("Garbage Can", "A can for garbage.",
	False,{trash:[usage_descriptor,["You place the garbage right in the can","eh"],
					item_adder,[terrarium,"Alley"],
					item_description_changer,["A can full of garbage.","Garbage Can"]]})

dragon = Item("Dragon", "It's one big ol' dragon.",
	False,{hammer:[usage_descriptor,["You bop the dragon on the nose","eh"],
				   item_adder,[garbage_can,"Alley"],
				   item_description_changer,["This dragon looks badly beaten","Dragon"],
				   room_description_changer,["No dragons here anymore. Youc an get to the garbage can tho","Alley"]]})

rug = Item("Rug", "It's like a shag carpet, if the shag were dust. ... What I'm trying to say is it's incredibly dusty. You walk skirting the edges.\n",
	False,{vacuum:[usage_descriptor,["You turn on the vaccum and clean off that rug","eh"],
				   item_description_changer,["Wow this rug is now clean. Not just grey and dusty.","Rug"],
				   room_description_changer,["Looks like this room has a clean rug in it.","Hag's Bedroom"]]})

satellite_dish = Item("Satellite Dish", "The satellite dish. It's barely held up by a feather duster. If you just took the duster it would probably break and the hag would have your head.",
	False,{sword:[usage_descriptor,["You quickly swap out the sword for the feather duster! The sword is sure wedged in there now. You probably couldn't get it back without breaking the satellite dish.\n","eh"],
				  item_invent_adder,["Feather Duster","eh"],
				  item_invent_remover,["Sword","eh"],
				  item_description_changer,["The satellite dish. It's securely held up by your sword.","Satellite Dish"],
				  item_description_changer,["Now is crystal clean. You can see an add for a portable forging set","TV"]]})

roof = Item("Roof", "The top of the house. You can see a satellite dish, thought it's too far to reach for now.....",
	False,{ladder:[usage_descriptor,["You place the ladder. Now you have access to the satellite dish!","eh"],
						   item_adder,[satellite_dish,"Alley"],
						   item_invent_remover,["Ladder","eh"],
						   item_description_changer,["The roof. Now you can access the satellite dish!","Roof"]]})

pool = Item("Pool", "The pool is filled with acid. There's something at the bottom, but you'd need to clean the acid away first.",
	False,{potion:[usage_descriptor,["You hold the potion as far away as you can and let a few drops "+
	"fall into the acid pool. There's a hissing, then a creaking, then a sound you "+
	"can only describe as a pool full of acid being cleared of acid. When you go back to inspect the pool "+
	"the acid is all gone! It turns out there was an old hammer lying at the bottom of the pool!\n","eh"],
				   item_adder,[rusty_hammer,"Backyard"],
				   item_description_changer,["An empty pool with a rusty hammer at the bottom. You'd swim in this now -- I mean, if there were water.","Pool"]]})

elemental = Item("Man", "He appears to be a large, blue man who seems thoroughly unhappy. He's dressed in a bathrobe.",
	False,{spider_box:[usage_descriptor,["You give the man the terrarium with the spider. He seems overjoyed and thanks you profusely. He disappears inside, and returns with a big vacuum which he tosses it to you."],
				   item_invent_adder,["vacuum","eh"],
				   item_invent_remover,["Spider Box","eh"],
				   item_description_changer,["A happy air elemental with his pet spider, waving to you from the window.","Man"],
				   room_description_changer,["""\n\nYou wouldn't think there was much room for a backyard here, and you'd be right.
				   This is a tiny, probably 15x15 strip of land, the majority of which is taken up by a pool.
				   It looks like the hag bought the biggest pool that could possibly fit in this tiny space and put it here.
				   You don't even know how she got it here. Everything is in shadows because the walls rise so high around
				   this pathetic place that the sun could only appear at high noon. You do make out a door
				   on the other side of the pool, however, and next to that a window, and in the window a
				   large blue man waving to you and smiling.
				   ""","Backyard"]]})

drawer = Item("Drawer", "This is the one drawer in the hag's kitchen that isn't "+
	"overflowing with potions or otherwise broken... but it's locked. Maybe it holds something important?",
	False,{key:[usage_descriptor,["Tingling with anticipation, you slide the key "+
	"in the lock and slowly turn. You hear the lock click open, and you reach inside to discover... a telephone book??","eh"],
		item_adder,[telephone_book,"Hag's Kitchen"],
		item_description_changer,["Now that the drawer has been unlocked, much of its mysterious allure is gone. You sigh. Life is full of little disappointments like this.\n","Drawer"]]})

telephone = Item("Phone", "It's the hag's escape-proof telephone. Rotary, of course."+
	"There's a note that says \"REMEMBER TO CALL LINDA AND THEN TURN HER INTO A FROG\".",
	False,{telephone_book:[usage_descriptor,["You pick up the telephone and,\n"+
	"trying to keep it as far from your face as possible, dial the fridge repairman's number.\n"+
	"While you're waiting for someone to pick up, a goblin vaults through the\n"+
	"window with a toolbox and start fixing the fridge without saying a word to you.\n"+
	"Before you can gather your wits and say anything, he finishes and jumps\n"+
	"back out the window. The phone goes to voicemail, but the fridge is fixed!\n"+
	"It opens to reveal the potion you need!","eh"],
	item_adder,[potion,"Hag's Kitchen"],
	room_description_changer,["""\n
	A greasy old kitchen which has seen better days - or maybe not. The dishes are
	stacked high, almost to the ceiling, and have started to ooze out onto the
	floor. The refrigerator is fixed and is humming smoothly, though the food has
	gone bad. Most of the cupboards and drawers are either missing or chocked
	full of what look like noxious magical ingredients. The only working drawer
	is open and empty. Against the wall is a grimy phone,
	though it looks like the numbers 9 and 1 have been removed. Windows on the
	west wall open out onto a dismal alley. The ceiling fan still works, though,
	so there's that. You find the slight breeze rather refreshing.\n""","Hag's Kitchen"]]})

fridge = Item("Refrigerator","This refrigerator is sparking, creaking and crying. It would be best not to approach it, certainly.",
	False,{})

potions = Item("Potions","You'd say these haggy potions are the biggest mess of all, but it seems the hag likes them just the way they are. Best not to get too near lest you become Jarek, Frog Prince.",
	False,{})

window = Item("Window 1","This window looks out onto a bricked up alley. A charming remnant of the 18th century \"Bad Architecture\" movement, to be sure.",
	False,{})

window2 = Item("Window 2","This window... Is this even a window? It's got a glass pane, but then it's just bricks. Either the architect or the windowsmith is to blame, but you don't know who.",
	False,{})

allItems = [potion,feather_duster,sword,spider,watch,key,knife,vacuum,cabinet,dragon,garbage_can,
			rug,dishes,trash,hammer,telephone_book,terrarium,satellite_dish,roof,ladder,tv,
			portable_forge,rusty_hammer,pool,elemental,spider_box,drawer,telephone,fridge,
			ceiling_fan,chair,tv,potions,window,window2]

#ok so some chains of events

#"eh" is there when a second arguemnt is needed only to fill the slot.

#beat dragon on nose -> adds garbage can
#put trash in garbage can -> find terrarium

#use ladder on roof -> adds stalite dish
#use sword of stalite dish -> drops feather duster

#use potion on pool -> drop rusty hammer
# use portable forge on rusty hammer -> get good hammer


#-------------------------------------------------------------------------------
#-----------------------------------ROOMS---------------------------------------
#---------------------------list of rooms in the game---------------------------

hags_kitchen = Room("Hag's Kitchen","""\n\n
A greasy old kitchen which has seen better days - or maybe not. The dishes are
stacked high, almost to the ceiling, and have started to ooze out onto the
floor. The refrigerator is flickering and sparking ominously. Most of the
cupboards and drawers are either missing or chocked full of what look like
noxious magical ingredients. Only one of the drawers looks like it's in working
condition. Against the wall is a grimy phone, though it looks like the numbers
9 and 1 have been removed. Windows on the west wall open out onto a dismal alley.
The ceiling fan still works, though, so there's that. You find the slight breeze
rather refreshing.\n""",
{"valid exits" : ["east","west"], "invalid exits" : ["north","south","northeast","southeast","northwest","southwest"]},
[dishes,trash,telephone,fridge,ceiling_fan,drawer,potions,window])

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
{"valid exits" : ["west","east","north"], "invalid exits" : ["south","northeast","southeast","northwest","southwest"]},
[cabinet,chair,tv])

alley = Room("Alley","""\n\nA long, narrow, alley about twenty feet wide which is bricked
up on either end, throwing everything into shadow. You are at one end of the alley,
and at the other end you think you can see a dumpster (who puts a dumpster in a
bricked up alley?? How does the garbageman even get it????) It's hard to tell,
of course, because between you and the dumpster is a huge dragon.
There is a little speck of roof that juts out from the wall above you, with what
looks to be a row of satellite dishes on it.\n""",
{"valid exits" : ["east"], "invalid exits" : ["north","south","northeast","southeast","northwest","southwest","west"]},
[dragon,roof])

hags_bedroom = Room("Hag's Bedroom", """\n\nAhhh, the prized jewel of casa del Hag.
There is a four poster bed draped with what is either a sensuous curtain or a malaria net,
or maybe both. You can see the hag's makeup kit on her armoire, which seems to be composed
of different colors of poison dart frog. The window provides a wonderful view of a brick wall,
Her closet is filled with literal skeletons, but by far the star of the show is the carpet.
To call it a dusty carpet would not do it justice -- rather, it seems to be a pile of dust
with ruglike attributes.
Smells like hag in here.
""",
{"valid exits" : ["west"], "invalid exits" : ["north","south","east","northeast","southeast","northwest","southwest"]},
[rug,window2])

hags_backyard = Room("Backyard","""\n\nYou wouldn't think there was much room for a backyard here, and you'd be right.
This is a tiny, probably 15x15 strip of land, the majority of which is taken up by a pool.
It looks like the hag bought the biggest pool that could possibly fit in this tiny space and put it here.
You don't even know how she got it here. Everything is in shadows because the walls rise so high around
this pathetic place that the sun could only appear at high noon. You do make out a door
on the other side of the pool, however, and next to that a window, and in the window a
large blue man making an obscene gesture at you.
""",
{"valid exits" : ["south"], "invalid exits" : ["north","east","west","northeast","northwest","southeast","southwest"]},
[pool,elemental,ladder])

house = [hags_kitchen,hags_livingroom,alley,hags_bedroom,hags_backyard]

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

#--------------------------------Action Dictionary----------------------------------------

actionDict =    {"die":quitGame,"exit game":quitGame,"quit game":quitGame,"laugh":laugh,"look":look,"-i":checkInventory,"take":item_getter,
				"get":item_getter,"pick up":item_getter,"east":direction_finder,"west":direction_finder,"north":direction_finder,
				"south":direction_finder,"help":helpMe,"use":item_user,"x":item_looker,"examine":item_looker,"check":item_looker,
				"drop":item_dropper,"talk":manTalker,"speak":manTalker}


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
def roomparse(name,description,exits,items,room,command):
	global history
	#so... always

	#the beginning of each run asks the player for their input
	validInput = False

	for d in actionDict:
		if d in command:
			if actionDict[d] != direction_finder and actionDict[d] != look:
				actionDict[d](name,description,exits,items,command,room)
				look(name,description,exits,items,command,room)
				return room
			elif actionDict[d] != look:
				newRoom = actionDict[d](name,description,exits,items,command,room)
				enter(newRoom,"look")
				return newRoom
			else:
				look(name,description,exits,items,command,room)
				return room
			validInput = True
			break

	if not validInput:
		history += "\n" + random.choice(invalid_input)
		return room

#-------------------------------------------------------------------------------
#--------------------------------FLASK------------------------------------------
#-------------------------------------------------------------------------------
global CharName
CharName = " "
global text
text = "look"
global currentRoom
currentRoom = hags_kitchen
global introCount
introCount = 0

@app.route('/')
def start():
	return redirect(url_for('beginning'))

@app.route('/YourNameIsJarekLenda')
def beginning():
	global history
	history += "\n\n" + hagSpeech1
	return render_template('nameAsk.html')

@app.route('/YourNameIsJarekLenda', methods=['POST'])
def get_name():
	text = request.form['text']
	global CharName
	CharName = text
	if "jarek lenda" in CharName.lower():
		return redirect(url_for('intro'))
	elif CharName == "":
		return hagSilentMurder(CharName)
	else:
		return HagMurder(CharName)

@app.route('/Intro')
def intro():
	global history
	history += "\n\n" + "> %s" % CharName
	history += "\n\n" + hagSpeech2(CharName)
	return render_template('input.html', response = history.split('\n'))

@app.route('/Intro', methods=['POST'])
def intro_cont():
	global introCount
	global history
	text = request.form['text']
	history += "\n\n" + "> %s" % text
	if introCount == 0:
		introCount += 1
		history += "\n\n" + hagSpeech3(CharName)
		return render_template('input.html', response = history.split('\n'))
	if introCount == 1:
		introCount += 1
		history += "\n\n" + hagSpeech4(CharName)
		return render_template('input.html', response = history.split('\n'))
	if introCount == 2:
		introCount += 1
		history += "\n\n" + hagSpeech5(CharName)
		return render_template('input.html', response = history.split('\n'))
	if introCount == 3:
		return redirect(url_for('start_input'))

@app.route('/TheQuest')
def start_input():
	global history
	global currentRoom
	currentRoom = enter(currentRoom,text)
	return render_template('input.html', response = history.split('\n'))

@app.route('/TheQuest', methods=['POST'])
def get_input():
	global text
	global history
	global currentRoom
	text = request.form['text']
	history += "\n\n" + ">" + text
	currentRoom = enter(currentRoom,text)
	return render_template('input.html', response = history.split('\n'))

if __name__ == '__main__':
   app.run(port=3000)