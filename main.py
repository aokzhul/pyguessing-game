# Author: Aokzhul Lahzbumc
# Description: Simple Python Number Guessing Game, for have fun
from random import randint

def main():
	# I add a max_attempts to make the game a bit more challenging
	attempts = 0
	max_attempts = 10
	print('\nWELCOME TO PYGUESSING GAME\n\n')
	print('Hey there, What\'s up!?!\nWould you like to play a game? It\'s very simple, I think of a number between 0 and 100 and you try to guess what number I thought.')
	print('\nPS.: Type "exit" at any time, if you don\'t play anymore')
	secret_number = randint(0, 100)

	while attempts < max_attempts:
		guess = input('Type your guess: ')
		if guess.lower() in ('quit', 'exit'):
			print('Right, Thanks for playing! See you next time...')
			break
		try:
			guess = int(guess)
		except ValueError:
			print('Oops, that doesn\'t look like a number. Please type again!')
			continue

		if guess < 0 or guess > 100:
			print('Hey, this number is out of the scope I asked for! Please, give a number BETWEEN 0 and 100')
			continue

		attempts += 1
		if attempts >= max_attempts:
			print('Woah, seams that your attempts over, you lose the game :(')
			break

		if guess > secret_number:
			print(f'The number I\'m thinking is lesser! (You have {max_attempts-attempts} attempts left)')
		elif guess < secret_number:
			print(f'The number I\'m thinking is greater! (You have {max_attempts-attempts} attempts left)')
		else:
			print(f'Wow, congratulations!! You guessed it in {attempts} attempts!')
			break
if __name__ == '__main__':
	main()