'''
Created on September 26, 2022

@author: Jack Thay, Dorian Rechak

TCP Client side of ex1 from MP1
'''
from socket import *

# >>> Code inspired from professor's slides <<<
serverName = "127.0.0.1" # IP Adress of destination, should be changed according to need
serverPort = 1236 # Socket port of destination
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

message = "test"
message_to_server = message.encode("utf-8")
clientSocket.send(message_to_server)
modifiedMessage = clientSocket.recv(2048)
print(modifiedMessage)
clientSocket.close()