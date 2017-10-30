from Crypto.PublicKey import RSA
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
key_pub_temp = clientsocket.recv(8129).decode
key_pub = RSA.importKey(key_pub_temp)
###

time.sleep(5)

while True:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((addr, port))
	
	message = key_pub.encrypt(input("> "), 8192)
	s.send(str(message).encode())
