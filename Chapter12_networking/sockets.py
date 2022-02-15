# a code provided in the video of Dr Chucks
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a handle
mysock.connect(('data.pr4e.org', 80)) # make the connection. Now mysock is a true variable. Impossible to inspect mysock with spyder
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # if we don't put .encode(), Python will say : a bytes-like object is required, not 'str'
# in the terminal, we need bytes but not string. encode() permits to transform unicode (the string) into utf-8 (what the terminal can recognize=

# \r means new line, but the cursor is still at the first line


# after .encode(), lines are bytes
# after .decode(), lines are string

mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()


#  http://www.dr-chuck.com/page1.htm
# =============================================================================
# Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page. You can use split('/') to break the URL into its component parts so you can extract the host name for the socket connect call. Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.
# =============================================================================
import re
import socket

inp=input('Enter a url: ')
out=re.findall('\.(\S+?)/',inp) # important, no greedy, if not, host name error
out=out[0]
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    mysock.connect((out,80))
    print('socket connected successfully\n')
except:
    print('incorrect host name\n')
cmdd='GET '+inp+' HTTP/1.0\r\n\r\n'
cmd=cmdd.encode()

try:
    mysock.send(cmd)
    print('command sent successfully\n')
except:
    print('command sent failure\n')

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()

# success with http://www.dr-chuck.com/page1.htm
# however if i change the website, there is no traceback, but what socket received is "bad request"

