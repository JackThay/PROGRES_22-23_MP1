'''
Created on September 26, 2022

@author: Jack Thay, Dorian Rechak

Server side of ex2 from MP1
'''
from socket import *
import http.server
import socketserver

# >>> Code inspired from https://stackabuse.com/serving-files-with-pythons-simplehttpserver-module/ <<<

PORT = 80 #Port 80 because is the standard one for http

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Server started at localhost:" + str(PORT))
    httpd.serve_forever()