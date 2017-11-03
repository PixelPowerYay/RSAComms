import rsa
import socket
import sys
import time

addr = str(input("Enter destination address: "))
port = int(input("Enter port number: "))

#### Key receiving
srvsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srvsocket.bind((addr, port+1))
srvsocket.listen(1)
(clientsocket, address) = srvsocket.accept()
print("Connection established, transferring key...")
time.sleep(1)
key_pub = clientsocket.recv(2048).decode()
###

time.sleep(5)

while True:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((addr, port))
	
	message = rsa.encrypt(input("> "), key_pub)
	s.send(str(message).encode('utf-8'))
