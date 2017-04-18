from Crypto.PublicKey import RSA
from Crypto import Random
import socket
import sys
import time

random_gen = Random.new().read
key_private = RSA.generate(8192, random_gen)
key_pub = key_private.publickey()

addr = str(input("Enter destination address: "))
port = int(input("Enter port number: "))

msg_num = 0

while True:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((addr, port))
	msg_num += 1

	if msg_num == 1:
		key_exp = open('key_internal', 'w')
		key_exp.write(str(key_private.exportKey()))
		time.sleep(2)
		key_file = open('key', 'r')
		key_pub_srv = RSA.importKey(key_file.read())
		s.send(str(key_private.publickey().exportKey()).encode())
	else:
		message = key_pub_srv.encrypt(input("> "), 8192)
		s.send(str(message).encode())