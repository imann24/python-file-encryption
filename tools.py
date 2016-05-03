import random

cipher_name = "cipher.dat"

def generate_cipher (ascii_limit = 128):
	char_set = []
	for i in range(0, ascii_limit):
		char_set.append(chr(i))
	random.shuffle(char_set)
	cipher = open(cyiher_name, 'w')
	for i in range(0, ascii_limit):
		cypher.write(chr(i) + char_set[i])
		if (i < ascii_limit - 1):
			cipher.write("\n")
	cipher.close()

generate_cipher()

def encrypt (file_path):
	print("Encrypting")

def de_encrypt (file_path):
	print("Unencrypting")

# Adapted from: 
# http://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file-using-python
def translate_chars (file_path, char_hash):
	rewrite_file = open(file_path, 'r+')

	file_text = rewrite_file.read()

	for i in range(0, len(file_text)):
		file_text[i] = char_hash[file_text[i]]

	rewrite_file.truncate()
	rewrite_file.write(file_text)
	rewrite_file.close()