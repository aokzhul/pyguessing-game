# Author: Aokzhul Lahzbumc
# Description: Simple Python Number Guessing Game, for have fun
from random import randint

print('\nWELCOME TO PYGUESSING GAME\n\n')
print('Hey there, What\'s up!?!\nWould like to play a game? It\'s very simple, I think a number between 0-100 and you try to guess what the number I think of.')
secret_number = randint(0, 100)

while True:
	try:
		guess = int(input('Type your guess: '))
	except ValueError:
		print('Oops, that doesn\'t look like a number. Please type again!')
		continue

	if guess > secret_number:
		print('The number I\'m thinking is lesser!')
	elif guess < secret_number:
		print('The number I\'m thinking is greater!')
	else:
		print('Wow, congratulations!! You guesset it!')
		break
