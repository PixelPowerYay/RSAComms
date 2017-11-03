import rsa
import socket
import sys
import time

(pubkey, privkey) = rsa.newkeys(2048)

addr = str(input("Enter sender address: "))
port = int(input("Enter port number: "))


#### Key sending
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((addr, port+1))
s.send(rsa.PublicKey().save_pkcs1(format='PEM').encode('utf-8'))
####

srvsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srvsocket.bind((addr, port))
srvsocket.listen(1)
(clientsocket, address) = srvsocket.accept()

print("Main connection established with " + str(address))

while True:
	(clientsocket, address) = srvsocket.accept()
	print("> " + str(rsa.decrypt(clientsocket.recv(2048).decode('utf-8'), privkey)))
