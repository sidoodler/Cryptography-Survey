# This is the client program that uses UDP

# Sequence:
#
# 1. Create a socket
# 2. Send messages to it
# (We need to know the server's hostname and port.)

import socket
import pickle
from hashing import hash
from RSA import rsa_encrypt
# create a socket
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# The first argument should be AF_INET
	# The second argument is SOCK_STREAM for TCP service
	#    and SOCK_DGRAM for UDP service

host='localhost'
port=43378 # this is the server's port number, which the client needs to know
port1=43379 # this is the eaves dropper's port
# send some bytes (encode the string into Bytes first)
message = "Hi, I want to send a message send your public key"
s.sendto( message.encode('utf-8'), (host,port))

#receive the public key
publicKey, addr = s.recvfrom(1024) # buffer size is 1024 bytes
print("Client received publicKey [n, e] =",pickle.loads(publicKey)," from ADDR=",addr)
publicKey=pickle.loads(publicKey)

#hashing the message to their respective ascii value
message = input("Enter the message here\n")
#message = "My fridge just groned, rolled their eyes and, hissed at me:\n\"Not you again!\"  "
hash_message=hash(message)
print("CLIENT: The hashed message ", hash_message)

#encrypting sring
encrypt_message = []
for i in range(0, len(hash_message)):
	encrypt_message.append(rsa_encrypt(hash_message[i],publicKey[0], publicKey[1]))

print("CLIENT: The encrypted message is: ",encrypt_message)

#send the message to the server
s.sendto( pickle.dumps(encrypt_message), (host,port))
#sending message to evesdropper
s.sendto(pickle.dumps(encrypt_message), (host,port1))

# see if the other side responds
data, addr = s.recvfrom(1024) # buffer size is 1024 bytes
print("CLIENT: received MESSAGE=",data.decode()," from ADDR=",addr)


# close the connection
s.close()
