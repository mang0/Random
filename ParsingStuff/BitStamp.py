import urllib.request

url = 'https://www.bitstamp.net/api/ticker/'
webpage = urllib.request.urlopen(url)
str_webpage = webpage.read()
dec_webpage = str_webpage.decode('utf-8')
strip_webpage = dec_webpage.strip('{}"')
split_webpage = strip_webpage.split(', ')
splitList = []
bigDict = {}

for newList in split_webpage:
	splitList.append(newList.split(': '))

for newerList in splitList:
	bigDict[newerList[0].strip('"')] = float(newerList[1].strip('"'))

def frontEnd():
	print()
	print ("These are the possible values you could wish to know: ")
	print()
	for key in bigDict.keys():
		print (key)
	print()
	rinput = input("Enter the key for which you want to know the value: ").lower()
	print()
	if rinput in bigDict.keys():
		print ("They key for %s is %s" % (rinput , bigDict[rinput]))
		print ("Care to try another?\n")
		r_input = input("Enter Yes/No: ").lower()
		if r_input == 'yes':
			frontEnd()
		elif r_input == 'y':
			frontEnd()
		else:
			print ("Well if you're going to be a sleazy fuck and not answer my question, you don't deserve the right to use this program. Fuck you.")
			exit()
	else: 
		print("I'm sorry, I didn't catch that?")
		frontEnd()
		
frontEnd()