# this is a number guessing game
import random

guessesTaken = 0

print ('Hello bub! What is your name?')
playerName = input()

number = random.randint(1,200)
print('Well, ' + playerName + ', I am thinking of a number between 1 and 200.')

while guessesTaken < 6:
    print ('Take a guess.')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken +1

    if guess < number:
        print('Too low!')
    if guess > number:
        print('Too high')
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good Job, ' + playerName + ', You got it in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. You suck, it was ' + number + '.')

