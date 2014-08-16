#		Imports a library for url management
import urllib.request

#		Sets a variable url to the given url for the BitStamp Ticker
url = 'https://www.bitstamp.net/api/ticker/'
#		Assigns the variable webpage to the url that has been opened with the imported library
webpage = urllib.request.urlopen(url)
#		However urlopen(url) will just give us the response data from the site, not the source itself. For this we need to read() it. A new variable, str_webpage is assigned to this.
str_webpage = webpage.read()
#		That gave us the entire source code of the website. We need to decode this so that we can get something readable. The variable dec_webpage simply takes the str_webpage and uses
#		the .decode() function to decode it. UTF-8 is used in 99% of situations.
#		Note, a quicker and cleaner way to do this that would not assign so many variables: webpage = urllib.request.urlopen(url).read().decode('utf-8')
dec_webpage = str_webpage.decode('utf-8')
#		Here the .strip() function works to remove the brackets and the double quotation marks. It is not stripping the single quotes. Only what is within those. To strip single quotes,
#		an escape character would be needed, i.e str.strip('\'')
strip_webpage = dec_webpage.strip('{}"')
#		The split function divides a string in to a list at a given character. In this case, comma
split_webpage = strip_webpage.split(', ')

#		Creating an empty list and dict. 
splitList = []
bigDict = {}

#		This for loop cycles through the items in split_webpage (a list from .split(), remember) and then splits them at a colon. This has the effect of dividing the keys from the values
#		in the data. Finally, it adds them to splitList, which was created on line 21. This is essentically 'listception', with a key and value being added to a list, and then that
#		list being appended to splitList.
for newList in split_webpage:
	splitList.append(newList.split(': '))

#		This loop cycles through the newly created splitList, removing the doulbe quotes that surround each item. It then adds the keys from the data as keys in bigDict, and assigns
#		the values from the data as values in bigDict. Note, the values are converted to floats by placing the entire thing within the float() function.
for newerList in splitList:
	bigDict[newerList[0].strip('"')] = float(newerList[1].strip('"'))

#		This defines a new function. The function deals with what the user will be seeing.
def frontEnd():
	print()
	print ("These are the possible values you could wish to know: ")
	print()
#		This cycles through just the keys in bigDict, and prints them. Note, .values() works too.	
	for key in bigDict.keys():
		print (key)
	print()	
	rinput = input("Enter the key for which you want to know the value: ").lower()
	print()
#		Here we get an if statment; if something, then do something. This particular if statement checks if the user input (rinput) matches to a key in bigDict. If it does, it will
#		print the value, by calling on bigDict[rinput] which will provide the value.
	if rinput in bigDict.keys():
		print ("They key for %s is %s" % (rinput , bigDict[rinput]))
		print ("Care to try another?\n")
		r_input = input("Enter Yes/No: ").lower()
		if r_input == 'yes':
			frontEnd()
		elif r_input == 'y':
			frontEnd()
#		If the user enters anything other than yes
		else:
			print ("Well if you're going to be a sleazy fuck and not answer my question, you don't deserve the right to use this program. Fuck you.")
			exit()
	else: 
		print("I'm sorry, I didn't catch that?")
		frontEnd()
		
frontEnd()