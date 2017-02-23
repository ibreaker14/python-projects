# CECS-424-Sp2017-Assignment-2
CECS 424 Python Project

Author: Mingtau Li, 011110539

## Part One
### Coin Rearranger Game
A game in which a player inserts a pair of adjacent coins into a two-coin gap in a list of coins to create a specific pattern

#### Instructions:
Initially, coins are arranged in the pattern **HHHHHTTTTT**

The goal of the game is to rearrange the coins to either **HTHTHTHTHT** or **THTHTHTHTH**

Only pairs of adjacent coins can be moved at a time.
Use the *left* and *right arrow* keys to move a cursor left and right (*space* also works for moving cursor right) until it is below your chosen coin.
The coin pairs chosen will the the coin above the cursor and the adjacent coin to the right of it.	
Press the *Enter* key to confirm selection. Pressing *Ctrl + C* terminates the game.

You have only 5 moves available. Your first move will move your first pair of coins to the end of the pattern, creating a two-coin gap. Your second pair of coins will be swapped with the two-coin gap. Every subsequent pair of coins will be swapped with wherever a gap exists until you have no more moves. Game ends when you either match the pattern or run out of moves.

Screenshot:
![alt text](Part%20One/screenshot.png "Screenshot")

## Part Two
### Project Euler: Summation of Primes Below 2 Million
Calculates prime numbers from 0 to 2000000.
No input is required.

If you wish to change the starting value, you can pass the value as an argument at runtime.
Constraints: numbers below 2000000

````
python3 part2.py <number>
````
