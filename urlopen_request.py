iport urllib2
req = urllib2.Request("http://www.example.com")
req.add_header("Content-Type", "text/plain")
req.add_data("query=python")  # POST method
f = urllib2.urlopen(req)
print f.read(300)
