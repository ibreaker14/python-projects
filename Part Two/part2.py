import os
import math
from datetime import datetime

# Author: Mingtau Li, 011110539
# Project Euler: Summation of Primes under 2 million
# CECS 424

# returns whether input is prime
def is_prime(input, divisor = 3):

	if input == 2: 			# if input is 2, it is prime
		prime = True
	elif input % 2 == 0:	# if divisible by 2, it is not prime
		prime = False
	elif input < 2:			# if input is less than 2, it is not prime
		prime = False
	elif divisor * divisor > input:  	# prime rule: a number N is the square of a number x. 
										# Other factors of N is comprised of a number a that is larger than x 
										# and a number b that is smaller than x or a and b is equal to x
		prime = True
	elif (input % divisor) == 0:	# skip all even numbers
		prime = False
	else:  							# look for primes with odd divisors
		prime = is_prime(input, divisor = divisor + 2)
	return prime

# returns list of primes
def get_primes(n):
	startValue = 0
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
def sum_primes(n):
	sum = 0
	list = get_primes(n)
	print("number of primes found: ",len(list))
	for i in range(len(list)):
		sum = sum + list[i]
	return sum


startTime = datetime.now()	# starts timer

startVal = 0
print("sum of primes from",startVal,"to 2000000: ", sum_primes(startVal))

# print(datetime.now() - startTime) # uncomment to view calculated execution time

# keeps console alive
os.system("pause")