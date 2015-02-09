#Listen on a socket and print the first string received

import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('localhost', 8089))
serverSocket.listen(1)

connection, address = serverSocket.accept()
buffer = connection.recv(64)
host, port = address
print(host + " >> " + buffer.decode('UTF-8'))