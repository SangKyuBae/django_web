from urllib2 import urlopen
data = "query=python"
f = urlopen("http://www.example.com", data)
print f.read(300)
