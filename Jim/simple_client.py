#Connect to a socket and send a single string

import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('10.1.1.37', 8089))
clientSocket.send(bytes('hello', 'UTF-8'))
clientSocket.close()