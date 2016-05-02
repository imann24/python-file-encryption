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

def translate_chars (file_path, char_hash):
	print("Translating")