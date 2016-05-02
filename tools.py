import random

cypher_name = "cypher.dat"

def generate_cypher (ascii_limit = 128):
	char_set = []
	for i in range(0, ascii_limit):
		char_set.append(chr(i))
	random.shuffle(char_set)
	cypher = open(cypher_name, 'w')
	for i in range(0, ascii_limit):
		cypher.write(chr(i) + char_set[i])
		if (i < ascii_limit - 1):
			cypher.write("\n")
	cypher.close()

generate_cypher()

def encrypt (file_path):
	print("Encrypting")

def de_encrypt (file_path):
	print()
def translate_chars (file_path, char_hash):