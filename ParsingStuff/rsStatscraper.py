import urllib.request

url = 'http://services.runescape.com/m=hiscore/index_lite.ws?player=i+am+felix'

webpage = urllib.request.urlopen(url)

str_webpage = webpage.read()

str_webpage = str_webpage.decode('utf-8')

split_str_webpage = str_webpage.split('\n')

for statLine in split_str_webpage[0:27]:
	split_statLine = statLine.split(',')
	#print (split_statLine)
	print ("The rank is %s, the level is %s and the xp is a mighty %s!" % (split_statLine[0], split_statLine[1], split_statLine[2]))
#split_statLine = statLine.split(',')
#print (split_statLine)

file = open('data.txt', 'w')

file.write(str_webpage)

file.close()

file = open('data_neat.txt' , 'r')
str_file = file.read()
#print (str_file)
file.close()

#var = abc123
#print ("This is a test %s and another %s" % (var, var2)