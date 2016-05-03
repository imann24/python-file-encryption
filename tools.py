import random
import os.path

cipher_name = "cipher.dat"

def generate_cipher (ascii_base = 32, ascii_limit = 128):
	char_set = []
	for i in range(ascii_base, ascii_limit):
		char_set.append(chr(i))
	random.shuffle(char_set)
	cipher = open(cipher_name, 'w')
	for i in range(0, ascii_limit - ascii_base):
		cipher.write(chr(i + ascii_base) + char_set[i])
		if (i + ascii_base < ascii_limit - 1):
			cipher.write("\n")
	cipher.close()

def encrypt (file_path):
	cipher = open(cipher_name, 'r')
	char_hash = create_char_hash(cipher.read(), 0, 1)
	translate_chars(file_path, char_hash) 

def cypher_exists ():
	return os.path.isfile(cipher_name)

def de_encrypt (file_path):
	cipher = open(cipher_name, 'r')
	char_hash = create_char_hash(cipher.read(), 1, 0)
	translate_chars(file_path, char_hash)

def create_char_hash(all_text, key_index, value_index):
	text_array = all_text.split("\n")
	text_dict = dict([])
	for i in range(0, len(text_array)):
		text_dict[text_array[i][key_index]] = text_array[i][value_index]
	return text_dict

# Adapted from: 
# http://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file-using-python
def translate_chars (file_path, char_hash):
	rewrite_file = open(file_path, 'r+')

	file_text = rewrite_file.read()

	file_text = list(file_text)

	for i in range(0, len(file_text)):
		file_text[i] = char_hash[file_text[i]]
	rewrite_file.seek(0)
	rewrite_file.truncate()
	rewrite_file.write("".join(file_text))
	rewrite_file.close()