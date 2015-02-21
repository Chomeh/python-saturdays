#Listen on a socket and repeat received messages to all other currently connected sockets

import socket
import select


MAX_CONNECTIONS = 20
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("", 8089)) #allow connections from anywhere
serverSocket.listen(MAX_CONNECTIONS)
serverSocket.setblocking(0) #set to non-blocking mode

clientSockets = []

while True:
    #accept any new connections
    potential_readers = [serverSocket]
    potential_writers = []
    potential_errs = [serverSocket]
    timeout = 0
    ready_to_read, ready_to_write, in_error = select.select(potential_readers, potential_writers, potential_errs, timeout)
    if serverSocket in ready_to_read:
        clientSocket, (host, port) = serverSocket.accept()
        print(host + " connected")
        clientSockets.append(clientSocket)

    for clientSocket in clientSockets:
        host, port = clientSocket.getpeername()
        try:
            potential_readers = [clientSocket]
            potential_writers = [clientSocket]
            potential_errs = [clientSocket]
            timeout = 0
            ready_to_read, ready_to_write, in_error = select.select(potential_readers, potential_writers, potential_errs, timeout)

            if in_error:
                raise Exception("select found socket from host:" + host + " in error")
            if not ready_to_read:
                continue #try again next loop

            messageBytes = clientSocket.recv(64)
            if len(messageBytes) == 0:
                continue
            message = host + " >> " + messageBytes.decode('UTF-8')
            print(message)
        except ConnectionError:
            print(host + " disconnected")
            clientSockets.remove(clientSocket)
            continue #problem reading message, skip relay
        except Exception as e:
            print("Error with socket from " + host + ": " + str(e))
            clientSockets.remove(clientSocket)
            continue #problem reading message, skip relay

        #relay message to all writable sockets
        for relaySocket in clientSockets:
            host, port = relaySocket.getpeername()
            try:
                potential_readers = []
                potential_writers = [relaySocket]
                potential_errs = [relaySocket]
                timeout = 0
                ready_to_read, ready_to_write, in_error = select.select(potential_readers, potential_writers, potential_errs, timeout)

                if in_error:
                    raise Exception("select found socket from host:" + host + " in error")
                if not ready_to_write:
                    continue #skip relaying message to this socket

                relaySocket.send(bytes(message, 'UTF-8'))
            except ConnectionError:
                print(host + " disconnected")
                clientSockets.remove(clientSocket)
            except Exception as e:
                print("Error with socket from " + host + ": " + str(e))
                clientSockets.remove(clientSocket)

print("...relay server terminated")