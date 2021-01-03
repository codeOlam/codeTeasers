#! /usr/bin/env python3

"""
	Guess Operation Teaser

	Given three integers, this script will determine which
	operation coud have resulted to the third integer from
	the first two.
	For example, for integers 5, 3, 2, the operation could
	have been subtraction. For integers 5, 4, 1, the 
	operation could have been eith subtraction or xor. 
	The scrit will output all the operations that could 
	work given the following set: + - * / % ^ & | << >>

	Note:
		% means remainder/mod
		^ & | << >> are bit operations
"""
import sys

def takeInt():
	#This function wil prompt users for input
	
	try:
		#Take all integer inputs
		x = int(input('[*] Enter First integer: '))
		y = int(input('[*] Enter Second integer: '))
		z = float(input('[*] Enter Third integer: '))
	except ValueError:
		#if value entered by user is not integer, reprompt user
		print('[!] Please Make sure values entered are integer\n')

		x = int(input('[*] Enter First integer: '))
		y = int(input('[*] Enter Second integer: '))
		z = float(input('[*] Enter Third integer: '))
	except ValueError:
		#Exit program
		print ('[x] value entered wrong!')
		sys.exit("[*] Program exiting...")

	return x, y, z

def checkOp():
	#This function will check the operations on the three integers

	x, y, z = takeInt()

	switcher = {
		'+':x + y == z,
		'-':x - y == z,
		'*':x * y == z,
		'/':x / y == z,
		'%':x % y == z,
		'^':x ^ y == z,
		'&':x & y == z,
		'|':x | y == z,
		'<<':x << y == z,
		'>>':x >> y == z,
	}

	operators_dict = dict()

	#get operations by dictionary comprehension
	operators_dict = {key:value for (key, value) in switcher.items() if value == True}

	print('\n[+] The Operations on the integers {}, {} and {} are: '.format(x, y, z))
	for i in operators_dict.keys():
		print(i)

	if operators_dict == {}:
		print('[-] None!')

def main():
	checkOp()



if __name__ == '__main__':
	main()
