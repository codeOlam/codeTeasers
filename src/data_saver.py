#!/usr/bin/env python3

"""
	Grab Most Freqent Letter In A Text Input

	This script will save on data space by determining the most
	frequent letter in an input text and then output the text 
	with the letter removed.
"""

def textInput():
	"""
		This function takes in input from user
		and save all text input in a list
		then returns the list
	"""
	#get text input from user
	text = ''
	text_list = []
	while text != "\q":
		text = input('[*] Enter text input or "\q" to quit: ')
		text_list.extend(text)
	return text_list[:-2]


def sliptText(text):
	"""
		This function will split text input into 
		individual char and save in a list
	"""
	return [char for char in text]

def countChar(txt, split_txt):
	"""
		This function counts the char with the highest 
		frequency and returns a dictionary
	"""
	char_dict = dict()

	for i in split_txt:
		char_count = txt.count(i)
		char_dict.update({i:char_count})

	return char_dict

def detChar(char_dic):
	"""
		This function will determine the keys and values 
		of the char dict for the highest frequency
	"""
	#get the key
	max_char_key = max(char_dic, key=char_dic.get)
	#get the value
	max_char_val = max(char_dic.values())

	return (max_char_key, max_char_val)

def main():

	text = textInput()
	print ('[*] The text entered is: \n', text)

	#split letters in the text and save in a list
	split_text = sliptText(text)

	charDict = countChar(text, split_text)

	max_charKey, max_charVal = detChar(charDict)

	print('\n[+] Maximum char is {} with frequency of {}'.format(max_charKey, max_charVal ))




if __name__ == '__main__':
	main()