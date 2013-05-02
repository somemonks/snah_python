import random
HANGMANPICS = ['''

 +---+
 |   |
     |
     |
     |
     |
========''', '''

 +---+
 |   |
 o   |
     |
     |
     |
========''', '''

 +---+
 |   |
 o   |
 |   |
     |
     |
========''', '''

 +---+
 |   |
 o   |
/|   |
     |
     |
========''', '''

 +---+
 |   |
 o   |
/|\  |
     |
     |
========''', '''

 +---+
 |   |
 o   |
/|\  |
/    |
     |
========''', '''

 +---+
 |   |
 o   |
/|\  |
/ \  |
     |
========''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings
    wordIndex = random.randint(0, len(wordList) -1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): #replace guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks [i+1:]
        
    for letter in blanks: # show secret word with spaces
        print(letter, end=' ')
        print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered and validates
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('HEY BUB! Enter a single letter.')
        elif guess in alreadyGuessed:
            print('You already guessed that letter silly!')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    #returns true if player wants to play again, otherwise false
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
        #Let player type a letter
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #Check if player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! the secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True

    else:
        missedLetters = missedLetters + guess

        # check if player has guessed too many times and lost

        if len(missedLetters) == len(HANGMANPICS) -1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have lost!\nAfter ' + str(len(missedLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

            #Ask the player if they want to play again
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
