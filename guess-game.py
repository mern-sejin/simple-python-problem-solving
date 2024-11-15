# Guess Game
import random
print('To stop anytime press: q')
score = 0
while True:
    num = random.randint(0, 10)
    guess = input('Guess a number between 0 to 10: ')
    if guess == 'q':
        print('Game Over.')
        break
    guess_num = int(guess)
    if guess_num is num:
        print('Congrats! you guessed it correctly.')
        score += 10
        print('Your New Score:', score)
    else: 
        print('Your guess did not match.')
        print('The number was:', num)
