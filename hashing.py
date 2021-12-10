#function to hash a input string
def hash(message):
	hash_string = []
	for i in range(0, len(message)):
		hash_string.append(ord(message[i]))
	return hash_string

def unHash(hash_message):
	list_char = []
	message = ""
	for i in range(0, len(hash_message)):
		char = chr(hash_message[i])
		message = message + char
	return message


