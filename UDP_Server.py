# This is the Server program that uses UDP
#
# Sequence of steps:
#	1. create a socket  
#	2. bind the socket to a host and port address
#	3. start sending and receiving data on this socket


import socket
import pickle
from RSA import rsa_generate, rsa_decrypt
from hashing import unHash


#  create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# The first argument should be AF_INET
	# The second argument is SOCK_STREAM for TCP service
	#    and SOCK_DGRAM for UDP service

# bind it to a host and a port
host = 'localhost'
port = 43378 # arbitrarily chosen non-privileged port number
s.bind((host,port))

print("Server started...waiting for a connection from the client")

# receive some bytes and print them
data, addr = s.recvfrom(1024) # buffer size is 1024 bytes
print("Server: Received MESSAGE=",data.decode(),"from ADDR=",addr)

#generating keys
bitlength = 20
n, e, d= rsa_generate(bitlength)

#setting up the public and private key
print("SERVER: The public key is:n = {}, e = {} ".format(n, e))
print("SERVER: The private key is:n = {}, d = {} ".format(n, d))


publicKey = [n, e]

#send public key
s.sendto(pickle.dumps(publicKey), (addr[0], addr[1]))

#receive message
data, addr = s.recvfrom(1024) # buffer size is 1024 bytes

data = pickle.loads(data)
print("SERVER: Message received is ", data)

#decrypting message
hash_message = []
for i in range(0, len(data)):
	hash_message.append(rsa_decrypt(data[i], d, n))

print("SERVER: Decrypted message is: ",hash_message)
message = unHash(hash_message)

print("SERVER: Message is:",message)

message = "Ok, message received"
s.sendto(message.encode('utf-8'), (addr[0], addr[1]))
# close the connection
s.close()
