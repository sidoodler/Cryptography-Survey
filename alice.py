d = 329
n = 1961


import socket
import math


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.105'
port = 43387
s.bind((host,port))


print("Server started...waiting for a connection from the client")
s.listen(1) 
connection_socket, addr = s.accept()
print("Connection initiated from ",addr)


data = connection_socket.recv(4096)
print("SERVER RECEIVED: ", data.decode())
connection_socket.send("Sure, hope you have my public key.".encode('utf-8'))
data = connection_socket.recv(4096)
print("SERVER RECEIVED: ", data.decode())


while True:
	data = connection_socket.recv(4096)
	if data.decode().isdigit() == False:
		break
	c = int(data.decode())
	print("SERVER RECEIVED: ", c)
	m = pow(c, d)%n
	print("ORIGINAL DATA WAS: ", m)
	connection_socket.send("Got your message.".encode('utf-8'))
	
	
print("SERVER RECEIVED: ", data.decode())
connection_socket.send("Okay, thanks for connecting!".encode('utf-8'))


connection_socket.close()
