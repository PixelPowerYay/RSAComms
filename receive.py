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
key_str = str(pubkey)[:10]
#s.send(key_str.encode())
print(key_str)
####

srvsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srvsocket.bind((addr, port))
srvsocket.listen(1)
(clientsocket, address) = srvsocket.accept()

print("Main connection established with " + str(address))

while True:
	(clientsocket, address) = srvsocket.accept()
	print("> " + str(key_private.decrypt(clientsocket.recv(8192).decode())))
