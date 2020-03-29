import random

# Declaring variable
word = ['hold', 'hanging', 'soccer', 'calculator', 'playboy']
index = random.randint(0, len(word) - 1)
secret = word[index]
dash = '-' * len(secret)
turns = 7
pic = 0

# Drawing hanging man
drawings = [
    " ____\n|    |\n| \n| \n| \n|\n-\n",
    " ____\n|    |\n|    O\n| \n| \n|\n-\n",
    " ____\n|    |\n|    O\n|   |\n| \n|\n-\n",
    " ____\n|    |\n|    O\n|   -|\n| \n|\n-\n",
    " ____\n|    |\n|    O\n|   -|-\n| \n|\n-\n",
    " ____\n|    |\n|    O\n|   -|-\n|   /\n|\n-\n",
    " ____\n|    |\n|    O\n|   -|-\n|    /\\\n|\n-\n",
]

# Main game function
def hangman():
    global secret
    global dash
    global turns
    global pic
    print(f'\n{dash}')
    print(f'You have {turns} tries')

    # Looping through the game while turn is 
    # greater than 0 and the secret has not been guessed
    while turns > 0 and dash != secret:
        guess = input('Guess a letter: ')
        
        # check if the guess is in the secret and update the dash
        # otherwise decrement turn and loop again
        if guess in secret:
            print(f"{guess} is in the secret word")
            result = ''
            for i in range(len(secret)):
                if secret[i] == guess:
                    result += guess
                else:
                    result += dash[i]

            dash = result
        else:
            turns -= 1
            print(f'{guess} is not in the secret word')
            print(drawings[pic])
            pic += 1
        print(f'\n{dash}')
        print(f'Tries letf: {turns}')
    
    # Display win/loss message
    if turns == 0:
        print(f'\nYou lose. The secret word is {secret}\n')
    else:
        print(f'\nCongratulations you guessed correctly. \nThe secret word is {secret}\n')


hangman()