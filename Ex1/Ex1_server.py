'''
Created on September 26, 2022

@author: Jack Thay, Dorian Rechak

TCP Server side of ex1 from MP1
'''
from socket import *

# >>> Code inspired from professor's slides <<<
serverPort = 700 # Socket port opened for receiving
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)

print(">>>Server ready, waiting for client...")
while True:
    connectionSocket, address = serverSocket.accept()
    message = connectionSocket.recv(2048)
    modifiedMessage = message.decode("utf-8").upper()
    connectionSocket.send(modifiedMessage.encode("utf8"))
    connectionSocket.close()