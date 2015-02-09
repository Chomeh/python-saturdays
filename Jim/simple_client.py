#Connect to a socket and send a single string

import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('localhost', 8089))
clientSocket.send(bytes('hello', 'UTF-8'))
