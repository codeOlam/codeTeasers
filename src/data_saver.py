#!/usr/bin/env python3

"""
	Grab Most Freqent Letter In A Text Input

	This script will save on data space by determining the most
	frequent letter in an input text and then output the text 
	with the letter removed.
"""

def main():

	#get text input from user
	text = input('Enter text input: ')
	print ('The text entered is: \n', text)

	#split letters in the text and save in a list
	split_text = [char for char in text]
	print(split_text)

	#create a new dict
	char_dict = dict()

	#count each letter
	for i in split_text:
		char_count = text.count(i)
		print('The number of letter {} is \t :{}'.format(i, char_count))

		char_dict.update({i:char_count})
	
	print(char_dict)

	print('\nTo get the most frequent letter')

	#get the key
	max_char_key = max(char_dict, key=char_dict.get)
	#get the value
	max_char_val = max(char_dict.values())

	print('Maximum char is {} with frequency of {}'.format(max_char_key, max_char_val))




if __name__ == '__main__':
	main()