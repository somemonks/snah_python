#This is the dragon tutorial
import random
import time

def displayIntro():
    print('You are on a planet full of Santoras. In front of you,')
    print('you see two beards. In none beard, the mouth is friendly')
    print('and will share his breakfast with you. The other beard')
    print('is greedy and hungry, and will eat you on sight.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which beard will you approach? (1 or 2)')
        cave= input()
    return cave

def checkCave(chosenCave):
    print('You aproach the beard ...')
    time.sleep(2)
    print('It is dark and salty ...')
    time.sleep(2)
    
    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print('You pick breakfast crumbs from the beard!')
    else:
        print('Gobbles you down in one bite!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? ( yes or no )')
    playAgain = input()
