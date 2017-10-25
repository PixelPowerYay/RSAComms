from Crypto.PublicKey import RSA
import socket
import sys
import time

addr = str(input("Enter sender address: "))
port = int(input("Enter port number: "))

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((addr, port))
msg_num = 0
serversocket.listen(1)
clientsocket, address = serversocket.accept()
print("Connection from " + str(address))

while True:
	msg_num += 1
	
	if msg_num == 1:
		key_pub_client = clientsocket.recv(65536).decode()
		key_client_file = open('key', 'w')
		key_client_file.write(str(key_pub_client))
		key_client_file.close()
		time.sleep(1)
		key_file = open('key_internal', 'r')
		key_private = RSA.importKey(key_file.read())
		key_private.close()
		
	else:
		data = key_private.decrypt(clientsocket.recv(8196).decode())
		if not data:
			break
		print("> " + str(data))
