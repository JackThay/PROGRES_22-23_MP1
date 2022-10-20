'''
Created on October 17, 2022

@author: Jack Thay, Dorian Rechak

TCP Relay of ex2 from MP1
'''
from socket import *

data = []
fichier = "cache.txt"

def files (origin, message):
    file_cache = open(fichier, "a")
    file_cache.write(origin + "\n" + str(message) +"\n") # le message n'a pas été decodé car sinon cela provequera une erreur 
    file_cache.close()

def read (test):
    file_cache = open(test, "r")
    learn = file_cache.read()
    file_cache.close()
    return learn

def search_files (test):
    try : 
        file_cache = open(test,"r")
        file_cache.read()
    except (FileNotFoundError, IOError):
        print("Wrong file or file path")


# >>> Code inspired from professor's slides <<<
# For the server side of the relay
port1 = 1234 # Socket port opened for receiving
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",port1))
serverSocket.listen(1)
# For the client side of the relay
serverName = "127.0.0.1" # IP Adress of destination, should be changed according to need
port2 = 80 # Socket port of destination, should be different from port1 if test are made on the same computer
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,port2))

# >> Launching relay <<
print(">>>Relay ready, waiting for client...")
while True:
    connectionSocket, address = serverSocket.accept() # Opening socket
    message_from_client = connectionSocket.recv(2048) # Receiving from socket
    print("Intercepted message from client:")
    if search_files (message_from_client) : 
        print ("lire dans le fichier test")
        learn = read(message_from_client)
        connectionSocket.send(learn.encode("utf-8"))
    else : 
        data.append(message_from_client)
        print(data)
    print(message_from_client.decode("utf-8")) # Displaying intercepted traffic from client
    clientSocket.send(message_from_client) # Sending message_from_client to server
    message_from_server = clientSocket.recv(2048) #Receiving bytes from server
    files("trafic du client:", message_from_client)
    files("trafic du serveur:", message_from_server)
    connectionSocket.send(message_from_server) # Sending message_from_server to client
    print("Intercepted message from server:")
    print(message_from_server) # Displaying intercepted traffic from server