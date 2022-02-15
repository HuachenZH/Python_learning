# urllib : URL library

# Example code 
import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') # comparing to the precedent code in sockets.py, this line has done the GET, done the .encode()
for line in fhand:
    print(line.decode().strip())
#










