import urllib.request

url = 'http://services.runescape.com/m=hiscore/index_lite.ws?player=i+am+felix'
webpage = urllib.request.urlopen(url)
str_webpage = webpage.read()
str_webpage = str_webpage.decode('utf-8')
split_str_webpage = str_webpage.split('\n')
skillList = []
statsDict = {}
skillNames = ['overall' , 'attack' , 'defence' , 'strength' , 'constitution' , 'ranged' , 'prayer' , 'magic' , 'cooking' , 'woodcutting' , 'fletching' , 'fishing' , 'firemaking' , 'crafting' , 'smithing' , 'mining' , 'herblore' , 'agility' , 'thieving' , 'slayer' , 'farming' , 'runecrafting' , 'hunter' , 'construction' , 'summoning' , 'dungeoneering' , 'divination']

for statLine in split_str_webpage[0:27]:
	split_statLine = statLine.split(',')
	lineStat = {'rank' : split_statLine[0] , 'level' : split_statLine[1] , 'xp' : split_statLine[2]}
	skillList.append(lineStat)

for x in range(0, len(skillNames)):
	statsDict[skillNames[x]] = skillList[x]

for skill in skillNames:
	print(skill)

print()
rinput = input("Enter skill: ").lower()
print('%s' %(statsDict[rinput]))

file = open('data.txt', 'w')
file.write(str_webpage)
file.close()