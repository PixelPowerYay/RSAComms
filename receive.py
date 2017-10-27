from Crypto.PublicKey import RSA
from Crypto import Random
import socket
import sys
import time

random_gen = Random.new().read
key_private = RSA.generate(1024, random_gen)

addr = str(input("Enter sender address: "))
port = int(input("Enter port number: "))

#### Key sending
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((addr, port+1))
s.send(str(key_private.publickey().exportKey(format='PEM')).encode())
####

srvsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srvsocket.bind((addr, port))
srvsocket.listen(1)
(clientsocket, address) = srvsocket.accept()

print("Main connection established with " + str(address))

while True:
	(clientsocket, address) = srvsocket.accept()
	print("> " + str(key_private.decrypt(clientsocket.recv(8192).decode())))
