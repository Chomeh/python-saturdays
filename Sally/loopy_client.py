#Connect to a socket and send a single string

import socket
import time

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('10.1.1.37', 8089))
clientSocket.send(bytes('its', 'UTF-8'))
time.sleep(1)
clientSocket.send(bytes('over', 'UTF-8'))
time.sleep(1)
clientSocket.send(bytes('9000!!!', 'UTF-8'))
clientSocket.close()