# Debugging coin toss program
import random

guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    toss = random.randint(0, 1)  # 0 is tails, 1 is heads
    coin_flip = "heads" if toss == 1 else "tails"

    if guess == coin_flip:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input()
        if guess == coin_flip:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')
