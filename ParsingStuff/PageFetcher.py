#		Imports the lib for url shiznang
import urllib.request

#		specifies the url in a variable. Quotes are importa, make it a str
url = "http://www.google.com/"

#		Tells the compiler that Cunt is the var that the webpage will be stored in,
#		and then opens the webpage using the imported lib
webpage = urllib.request.urlopen(url)

#		"""
#		prints the type of the variable webpage. Is not
#		defined yet, so it cannot print anything properly, just takes the fact that
#		the webpage does exist and so shows the type (HTTPResponse)
#		print(webpage)
#		"""
	
#		This assigns the read webpage (a string, remember?) to the var str_webpage
str_webpage = webpage.read()

#		This decoedes the webpage string into a readable format. Or something akin
#		to that.
str_webpage = str_webpage.decode('utf-8')

#		prints the newly formed readable string-variable str_webpage, god Jacob this is easy
print (str_webpage)

#		This writes a file (w) called google.html. Default is r, read, so w needs to be specified.
file = open('google.html', 'w')

#		Finally, write the string str_webpage to the file!
file.write(str_webpage)

#Doneeee!