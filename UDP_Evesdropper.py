import socket
import pickle
from RSA import rsa_generate, rsa_decrypt
from hashing import unHash
from weiner_attack import weiner_attack

#  create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# The first argument should be AF_INET
	# The second argument is SOCK_STREAM for TCP service
	#    and SOCK_DGRAM for UDP service

# bind it to a host and a port
host = 'localhost'
port = 43379 # arbitrarily chosen non-privileged port number
s.bind((host,port))

n, e = input("EVESDROPPER: Enter the public Key [n e]: ").split()
n = int(n)
e = int(e)


#getting the public key from UDP_Serevr
print("EVESDROPPER: PublicKey is [n, e]",[n, e])

print("Evesdropper started...waiting for a message")

# receive some bytes and print them
data, addr = s.recvfrom(1024) # buffer size is 1024 bytes
data = pickle.loads(data)
print("Evesdropper: Received MESSAGE=",data,"from ADDR=",addr)

d = weiner_attack(e, n)

#print the predicted d
print("EVESDROPPER: Predicted d is: ",d)

#decrypting message
hash_message = []
for i in range(0, len(data)):
	hash_message.append(rsa_decrypt(data[i], d, n))


message = unHash(hash_message)

print("EVESDROPPER: Message is:",message)




