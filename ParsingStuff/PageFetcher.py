import urllib.request
url = "http://www.google.com/"
webpage = urllib.request.urlopen(url)
str_webpage = webpage.read()
str_webpage = str_webpage.decode('utf-8')
print (str_webpage)
file = open('google.html', 'w')
file.write(str_webpage)