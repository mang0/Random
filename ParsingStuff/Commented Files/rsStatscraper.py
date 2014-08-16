#	Here we import a library for url management
import urllib.request

#	The URL is specified. Perhaps work out how to get stats from a user decided by rinput?
url = 'http://services.runescape.com/m=hiscore/index_lite.ws?player=i+am+felix'
#	Variable webpage is the url giving in the variable url, opened using a function from the imported library
webpage = urllib.request.urlopen(url)
#	In the docts for urllib it states that the .urlopen() function works much like a file i/o library, so we can .read() the webpage as we would .read() a file. Else we just get the source code for
#	website, formatted as a byte-string, we don't want that.
#	By using read(), we change webpage into a regular string, (hence str_webpage).
str_webpage = webpage.read()
#	However this just gives us the type. In order to read the entire page, we have to tell python the encoding, so that we can decode it. In 99% of cases, the encoding will be utf-8.
#	This line decodes the str_webpage variable (which is in string form from using read() and then overwrites the variable str_webpage.
str_webpage = str_webpage.decode('utf-8')
#	Here we split the content of the page in to a list. The '\n' specifies where to split the page for a different item. Each time we get to a line break in the HTML, a new item in the list is added.
split_str_webpage = str_webpage.split('\n')
#	Simply makes an empty list called skillList, for later use.
skillList = []
#	Simply makes an empty dictionary called statsDict, for later use.
statsDict = {}
#	Makes a list with all the skills in the order they appear from the website.
skillNames = ['overall' , 'attack' , 'defence' , 'strength' , 'constitution' , 'ranged' , 'prayer' , 'magic' , 'cooking' , 'woodcutting' , 'fletching' , 'fishing' , 'firemaking' , 'crafting' , 'smithing' , 'mining' , 'herblore' , 'agility' , 'thieving' , 'slayer' , 'farming' , 'runecrafting' , 'hunter' , 'construction' , 'summoning' , 'dungeoneering' , 'divination']

#	For loop
#		This splices the list split_str_webpage to only use the first 27 entries. After that is other crap that is not needed for this program. It also cycles through split_str_webpage and
for statLine in split_str_webpage[0:27]:
#		This does the same as the other split above. Creates a new list called split_statLine, where we have split at every comma. This means we have a list of individual stats as seperate items.
	split_statLine = statLine.split(',')
#		Dictionary. Here we assign a key, 'rank' to the first item in split_statLine. (his is called a value in a dict). The second key, 'level' is assigned the value of the second item in split_statLine,
#		and so on. We then append the contents of the dict to skillList. We cannot just overwrite skillList, we must use append. This is because it is still inside the loop. Creating a list inside
#		the loop will mean that every time it loops back, the list would be overwritten. We just want to add to one that is made outside the loop (see line 17).
	lineStat = {'rank' : split_statLine[0] , 'level' : split_statLine[1] , 'xp' : split_statLine[2]}
	skillList.append(lineStat)

#	For loop
#		This is where the program creates a dictionary of all the skills (from skillNames, line 21) matched up to all the stats of the skills (added to skillList that is created on line 17 and appended
#		to in the previous for loop. Using x as the variable for the numbers going in to the dictionaries, we can use the same one throughout the loop.
for x in range(0, len(skillNames)):
	statsDict[skillNames[x]] = skillList[x]

#	This for loop cycles through the skillNames list and prints each value for the user to see.
for skill in skillNames:
	print(skill)

#	Prints a newline, derp
print()
#	Assigns a user inputed string to the variable rinput.
rinput = input("Enter skill: ").lower()
#	Grabs the stats for whichever skill the user entered and prints them.
print('%s' %(statsDict[rinput]))

#	Makes a new file data.txt. 'w' is needed as default is 'r'ead, not 'w'rite. Good practice to specify which one anyway.
file = open('data.txt', 'w')
#	Writes the contents of the variable str_webpage to the file.
file.write(str_webpage)
#	Closes the file.
file.close()