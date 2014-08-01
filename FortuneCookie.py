#!/usr/bin/python

#Fortune Cookie Program
#The Computer generates a random positive message 
#Messages will be either inspirational or motivational quotes 
#By actual famous people,Random people or Lawton C. Mizell 

#Random Module Imported
import random 

print("Welcome!\n")
print("Here is your random positive message for the day...\n") 

positive_message = random.randint(1,7) 

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
elif positive_message == 6: 
	print("The will to win, the desire to succeed, the urge to reach your full potential... these are the keys that will unlock the door to personal excellence. -Confucius")
elif positive_message == 7:
	print("Infuse your life with action. Don't wait for it to happen. Make it happen. Make your own future. Make your own hope. Make your own love. And whatever your beliefs, honor your creator, not by passively waiting for grace to come down from upon high, but by doing what you can to make grace happen... yourself, right now, right down here on Earth. -Bradley Whitford") 
