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
		x = int(input('[-] Enter First integer: '))
		y = int(input('[-] Enter Second integer: '))
		z = int(input('[-] Enter Third integer: '))
	except ValueError:
		#if value entered by user is not integer, reprompt user
		print('[!] Please Make sure values entered are integer\n')

		x = int(input('[-] Enter First integer: '))
		y = int(input('[-] Enter Second integer: '))
		z = int(input('[-] Enter Third integer: '))

	finally:
		#Exit program
		print ('[x] value entered wrong!')
		sys.exit("Program exiting...")

	return x, y, z

def checkOp(x, y, z):
	#This function will check the operations on the three integers
	pass

def main():
	# initialize a list to hold all operators
	op = []

	#Take input
	x = int(input('Enter first integer:\t '))
	y = int(input('Enter second integer:\t '))
	z = int(input('Enter Third integer:\t '))

	#check the operation
	if x + y == z:
		print('[+] {} is an operator '.format('+'))
		op.append('+')
	elif x - y == z:
		print('[+] {} is an operator '.format('-'))
		op.append('-')
	elif x * y == z:
		print('[+] {} is an operator '.format('*'))
		op.append('*')
	elif x / y == z:
		print('[+] {} is an operator '.format('/'))
		op.append('/')
	elif x % y == z:
		print('[+] {} is an operator '.format('%'))
		op.append('%')
	elif x ^ y == z:
		print('[+] {} is an operator '.format('^'))
		op.append('^')
	elif x & y == z:
		print('[+] {} is an operator '.format('&'))
		op.append('&')
	elif x | y == z:
		print('[+] {} is an operator '.format('|'))
		op.append('|')
	elif x << y == z:
		print('[+] {} is an operator '.format('<<'))
		op.append('<<')
	elif x >> y == z:
		print('[+] {} is an operator '.format('>>'))
		op.append('>>')
	else:
		print('[x] No Operation found for the integers')
		op.append('None')

	print("[+] The operator for the integers {}, {}, and {} are {}".format(x, y, z, op))



if __name__ == '__main__':
	main()
