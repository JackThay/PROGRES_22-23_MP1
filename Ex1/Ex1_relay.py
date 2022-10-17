'''
Created on October 17, 2022

@author: Jack Thay, Dorian Rechak

TCP Relay of ex1 from MP1
'''
from socket import *

# >>> Code inspired from professor's slides <<<
# For the server side of the relay
port1 = 1234 # Socket port opened for receiving
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",port1))
serverSocket.listen(1)

# For the client side of the relay
serverName = "127.0.0.1" # IP Adress of destination, should be changed according to need
port2 = 700 # Socket port of destination, should be different from port1 if test are made on the same computer
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,port2))


# >> Launching relay <<
print(">>>Relay ready, waiting for client...")
while True:
    connectionSocket, address = serverSocket.accept() # Opening socket
    message_from_client = connectionSocket.recv(2048) # Receiving from socket
    print("Intercepted message from client:")
    print(message_from_client.decode("utf-8")) # Displaying intercepted traffic from client
    clientSocket.send(message_from_client) # Sending message_from_client to server
    message_from_server = clientSocket.recv(2048) #Receiving bytes from server
    print("Intercepted message from server:")
    print(message_from_server.decode("utf-8")) # Displaying intercepted traffic from server
    connectionSocket.send(message_from_server) # Sending message_from_server to client
    clientSocket.close()
    connectionSocket.close()