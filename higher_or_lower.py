from random import randrange

def highlow():
	x =int( input("Give me a number between 0 and 10: "))
	y = int(randrange(1,11))
	if x > y:
		print("Too High")
	elif y > x:
		print("Too Low")
	else:
		print("Correct!")
	print("Random Number was " + str(y))
highlow()
