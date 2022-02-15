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

