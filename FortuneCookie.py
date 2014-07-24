#!/usr/bin/python

#Fortune Cookie Program
#The Computer generates a random positive message 
#Messages will be either inspirational or motivational quotes 
#By actual famous people,Random people or Lawton C. Mizell 

#Random Module Imported
import random 

print("Welcome!\n")
print("Here is your random positive message for the day...\n") 

positive_message = random.randint(1,5) 

if positive_message == 1: 
	print("Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time. -Thomas A. Edison")

elif positive_message == 2:
	print("Problems are not stop signs, they are guidelines. -Robert H. Schuller")  
elif positive_message == 3: 
	print("Believe in yourself! Have faith in your abilities! Without a humble but reasonable confidence in your own powers you cannot be successful or happy. -Norman Vincent Peale")
elif positive_message == 4: 
	print("Always do your best. What you plant now, you will harvest later. -Og Mandino")
elif positive_message == 5:
	print("Expect problems and eat them for breakfast. -Alfred A. Montapert")

