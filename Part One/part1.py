import os
import sys
from getch import *

# Author: Mingtau Li, 011110539
# Coin Rearranger Game
# CECS 424
# Dependencies: getch.py (for capturing key input)

#Swaps coins based on given index
def swap(coins, index):
	swapDest = coins.find("-")	# index of gap
	coins = list(coins)	# coin pattern
	
	if swapDest - index > 1 or index < len(coins)-1:
		# if there is no gap, make one and then swap
		if "-" not in coins:					
			coins.extend([coins[index],coins[index+1]])
			coins[index] = "-"
			coins[index+1] = "-"
		# swaps chosen coins with gap
		else:									
			coins[swapDest] = coins[index]
			coins[swapDest+1] = coins[index+1]
			coins[index] = "-"
			coins[index+1]= "-" 

	coins = "".join(coins)	# converts coins list to string for readability
	return coins

# captures user input and returns chosen coin position
def choose_position():
	index = 0	# cursor position
	space = " "	# space character
	space_string = ""	# string of space characters

	# if gap is in front of pattern, move cursor to the first coin after gap
	if "-" in coins and coins.find("-") == 0:		
		index = 2									
		space_string = space_string + space + space
		sys.stdout.flush()
		sys.stdout.write("\r" + space_string)
			
	while True: 
		key = ord(getch())

		# if Enter key is pressed, return cursor position
		if key == 13:
			sys.stdout.flush()
			sys.stdout.write("\r")
			return index

		# if Ctrl+C is pressed, terminate game
		if key == 3: 
			sys.stdout.flush()
			sys.stdout.write("\rGame Terminated\n\n")
			break

		elif key == 32:	# if button pressed is a space
			if len(space_string) < len(coins) - 1:

					# if cursor is in right before gap, move cursor to next available coin position to the right
					if index + 1 == coins.find("-"):
						if coins.find("-") != len(coins) - 2:
							space_string = space_string + space + space + space
							index = index + 3

					# move cursor to next coin position to the right
					else:
						space_string = space_string + space
						index = index + 1

					# print cursor space
					sys.stdout.write("\r"+space_string)
					sys.stdout.flush()

		elif key == 224:	# if button pressed is a special character (224 for windows, 91 for linux)
			key = ord(getch())

			if key == 77: # right arrow (77 for windows, 67 for linux)
				if len(space_string) < len(coins) - 1:

					# if cursor is in right before gap, move cursor to next available coin position to the right
					if index + 1 == coins.find("-"):
						if coins.find("-") != len(coins) - 2:
							space_string = space_string + space + space + space
							index = index + 3

					# move cursor to next coin position to the right
					else:
						space_string = space_string + space
						index = index + 1

					# print cursor space
					sys.stdout.write("\r"+space_string)
					sys.stdout.flush()


			elif key == 75: # left arrow (75 for windows, 68 for linux)
				if "-" not in coins: # if there is no gap

					# move cursor left as long as theere is space
					if index > 0:
						space_string = space_string[0:len(space_string)-1]
						index = index - 1

				else:	# if gap exists

					if coins.find("-") != 0:	# if gap is not in very front of pattern

						# skip gap and place cursor to next available coin position left of the gap
						if index - 2 == coins.find("-"):
							space_string = space_string[0:len(space_string)-3]
							index = index - 3

						# move cursor left
						elif index > 0:
							space_string = space_string[0:len(space_string)-1]
							index = index - 1

					else:	# if gap is in very front of pattern

						# restrict cursor to first coin position right of the gap
						if index > 2:
							space_string = space_string[0:len(space_string)-1]
							index = index - 1

				# print cursor space			
				sys.stdout.write("\r"+space_string)
				sys.stdout.flush()

		elif key == 91:	# if button pressed is a special character (224 for windows, 91 for linux)
			key = ord(getch())

			if key == 67: # right arrow (77 for windows, 67 for linux)
				if len(space_string) < len(coins) - 1:

					# if cursor is in right before gap, move cursor to next available coin position to the right
					if index + 1 == coins.find("-"):
						if coins.find("-") != len(coins) - 2:
							space_string = space_string + space + space + space
							index = index + 3

					# move cursor to next coin position to the right
					else:
						space_string = space_string + space
						index = index + 1

					# print cursor space	
					sys.stdout.write("\r"+space_string)
					sys.stdout.flush()
				
			elif key == 68: # left arrow (75 for windows, 68 for linux)
				if "-" not in coins: # if there is no gap

					# move cursor left as long as theere is space
					if index > 0:
						space_string = space_string[0:len(space_string)-1]
						index = index - 1

				else:	# if gap exists

					if coins.find("-") != 0:	# if gap is not in very front of pattern

						# skip gap and place cursor to next available coin position left of the gap
						if index - 2 == coins.find("-"):
							space_string = space_string[0:len(space_string)-3]
							index = index - 3

						# move cursor left
						elif index > 0:
							space_string = space_string[0:len(space_string)-1]
							index = index - 1

					else:	# if gap is in very front of pattern
					
						# restrict cursor to first coin position right of the gap
						if index > 2:
							space_string = space_string[0:len(space_string)-1]
							index = index - 1

				# print cursor space			
				sys.stdout.write("\r"+space_string)
				sys.stdout.flush()
		
# main game
coins = "HHHHHTTTTT"

welcome_message = "\n==== Welcome to the Coin Arranger Game ====\nThe goal of the game is to rearrange the coin pattern HHHHHTTTTT into either HTHTHTHTHT or THTHTHTHTH.\nCoins are moved in pairs of 2 at a time. Coins must be adjacent to each other.\nYour first chosen pair of coins will be brough to the end of the pattern, creating a 2-coin gap.\nEvery move after that will swap a pair of coins into the gap. You have 5 moves.\n"
play_instructions = "Use your arrow keys to move the cursor left and right (spacebar also works for moving right)\nPress Enter to choose coins. Chosen coins are coin under cursor and adjacent coin to the right of it.\nCtrl + C terminates game.\n"

print(welcome_message);

# player has 5 moves
for x in range(5):
	while True:
		print(play_instructions)
		print(coins)

		chosenIndex = choose_position() # player chooses coins based on cursor position

		if chosenIndex == None: # terminates game if Ctrl + C is pressed
			exit()

		# player has to keep choosing coins until moves are valid
		if chosenIndex == len(coins) - 1 or chosenIndex + 1 == coins.find("-"):
			print("You can't make this move\n")

		# if move is valid, swap coins with gap
		else:
			coins = swap(coins,chosenIndex)
			print("move # ",x+1,"\n")
			break

	# if pattern matches before 5 moves, end game
	if coins.find("THTHTHTHTH") != -1 or coins.find("HTHTHTHTHT") != -1:
		print("Congrats! You won the game!")
		print("\nFinal pattern: ",coins,"\n")
		exit()

# prints final pattern
print("\nFinal pattern: ",coins,"\n")

# prints whether player wins or loses
if coins.find("THTHTHTHTH") != -1 or coins.find("HTHTHTHTHT") != -1:
	print("Congrats! You won the game!")
else:
	print("You lost. Better luck next time")

# keeps console alive in windows
if os.name == 'nt':
	os.system("pause")


