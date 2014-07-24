#!/usr/bin/python

#Guess my Number Program
#The computer generates a number between 1 and 100
#The player tries to guess the number and the computer
#Lets the player know if he is too high, too low or
#Right on target

#Random module is imported

import random 

#Game is explained

print ("\nWelcome to 'Guess My Number' !")
print ("Program Created by Alcamech, Godspeed :)\n")
print("--------------------------------------------------------\n")
print ("I'm thinkiing of a number between 1-100...")
print ("You get 5 tries to do it")
print ("Good Luck failing!\n")

#initial values are set

number = random.randint(1,100)
tries = 1
guess = int(input("Enter your guess:"))

#guessing loop

while tries < 5 and  guess != number:
	if guess > number:
	    print("Lower...")
	else:
            print("Higher...")
 
	guess = int(input("Enter your guesss:"))
	tries = tries + 1

	if guess == number:
		print("You guessed it! The number was", number)
		print("And it only took you", tries, "tries!\n") 


print("Too many tries!\n")

input("\n\nPress the enter key to exit.")


