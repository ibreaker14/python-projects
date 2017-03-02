import os
import math
import sys
from datetime import datetime

# Author: Mingtau Li, 011110539
# Project Euler: Summation of Primes under 2 million
# CECS 424

# returns whether input is prime
# param:	input: int number to be checked
		#	divisor_a: smallest divisor to be compared with
		#	divisor_b: largest divisor to be compared with
def is_prime(input):
	if input == 2 or input == 3:
		return True
	elif input < 2:
		return False
	elif input % 2 == 0:
		return False

	divisor_a = 3

	# prime rule: a number N is the square of a number x. 
	# Other factors of N is comprised of a number a that is larger than x 
	# and a number b that is smaller than x or a and b is equal to x	
	divisor_b = math.floor(math.sqrt(input))
	if divisor_b % 2 == 0: 
		divisor_b = divisor_b + 1

	# loop ends when a and b meets
	while (divisor_a <= divisor_b):
		if(input % divisor_a == 0 or input % divisor_b == 0):
			return False;

		divisor_a = divisor_a + 2
		divisor_b = divisor_b - 2
		

	return True


# returns list of primes
# param:	n: starting number 
def get_primes(n):
	startValue = 0			# number to start counting from
	maxValue = 2000000		# max value is two million
	list = []				# declare list
	if n < 2:				#special case: 1 is not prime but 2 is
		n = 2

	if n == 2:				# special case: 2 is a prime number
		list.append(n)
		startValue = n + 1
	elif n % 2 == 0:
		startValue = n + 1	# force start value to be odd number
	else:
		startValue = n 		# start value is chosen number

	for x in range(startValue, maxValue, 2):	# loop through every odd number
		if is_prime(x):
			list.append(x)

	return list

# returns the sum of a list of primes
# param:	n: starting number up to 2 million
def sum_primes(n):
	sum = 0
	list = get_primes(n)
	for i in range(len(list)):
		sum = sum + list[i]
	return sum

startVal = 0

if len(sys.argv) > 1:
	try:
		startVal = int((sys.argv[1]))
	except ValueError:
		print("Invalid argument. Start value will now revert back to 0:\n")

print("Calculating...")

print("sum of primes from",startVal,"to 2000000: ", sum_primes(startVal))

# keeps console alive in windows
if os.name == 'nt':
	os.system("pause")