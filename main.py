# Author: Aokzhul Lahzbumc
# Description: Simple Python Number Guessing Game, for have fun
from random import randint

print('\nWELCOME TO PYGUESSING GAME\n\n')
print('Hey there, What\'s up!?!\nWould you like to play a game? It\'s very simple, I think of a number between 0 and 100 and you try to guess what number I thought.')
print('\nPS.: Type "exit" at any time, if you don\'t play anymore')
secret_number = randint(0, 100)

while True:
	guess = input('Type your guess: ')
	if guess.lower() in ('quit', 'exit'):
		print('Right, Thanks for playing! See you next time...')
		break
	try:
		guess = int(guess)
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
