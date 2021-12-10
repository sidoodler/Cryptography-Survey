e = 101
n = 1961


import socket
import math


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host='192.168.0.105'
port=43387
s.connect((host,port))


s.send("I want to send you some data secretly.".encode('utf-8'))
response = s.recv(4096)
print("CLIENT RECEIVED: ",response.decode())
s.send("Yes, I do. Sending data...".encode('utf-8'))


while True:
	m = int(input("Enter your message: "))
	if m == 0:
		break
	c = pow(m, e)%n
	s.send(str(c).encode('utf-8'))
	response = s.recv(1024)
	print("CLIENT RECEIVED: ",response.decode())
	
	
s.send("Closing connection. Bye-bye!".encode('utf-8'))
response = s.recv(1024)
print("CLIENT RECEIVED: ",response.decode())


s.close()
