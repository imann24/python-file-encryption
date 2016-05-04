# Author: Isaiah Mann
# Description: Simple implementation of using a hash to encrypt a file
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

def cipher_exists ():
	return os.path.isfile(cipher_name)


def is_cipher (file_path):
	return cipher_name in file_path

def encrypt (file_path):
	cipher = open(cipher_name, 'r')
	char_hash = create_char_hash(cipher.read(), 0, 1)
	translate_file(file_path, char_hash) 

def encrypt_string (plain_string):
	cipher = open(cipher_name, 'r')
	char_hash = create_char_hash(cipher.read(), 0, 1)
	return translate_string(plain_string, char_hash)

def de_encrypt (file_path):
	cipher = open(cipher_name, 'r')
	char_hash = create_char_hash(cipher.read(), 1, 0)
	translate_file(file_path, char_hash)

def de_encrypt_string (encrypted_string):
	cipher = open(cipher_name, 'r')
	char_hash = create_char_hash(cipher.read(), 1, 0)
	return translate_string(encrypted_string, char_hash)

def create_char_hash(all_text, key_index, value_index):
	text_array = all_text.split("\n")
	text_dict = dict([])
	for i in range(0, len(text_array)):
		text_dict[text_array[i][key_index]] = text_array[i][value_index]
	return text_dict

def translate_file (file_path, char_hash):
	rewrite_file = open(file_path, 'r+')

	file_text = rewrite_file.read()

	rewrite_file.seek(0)
	rewrite_file.truncate()
	rewrite_file.write(translate_string(file_text, char_hash))
	rewrite_file.close()

# Adapted from: 
# http://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file-using-python
def translate_string (text, char_hash):
	text = list(text)

	for i in range(0, len(text)):
		if (text[i] in char_hash.keys()):
			text[i] = char_hash[text[i]]

	return "".join(text)