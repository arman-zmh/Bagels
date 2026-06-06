import random
NUM_DIGITS = 3
MAX_GUESSES = 10 

def main():
    print('''Bagels, a deductive logic game.
    By arman-zmh

    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:       That means:
    Pico              One digit is correct but in the wrong position.
    Fermi             One digit is correct and in the right position.
    Bagels            No digit is correct.

    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico.'''.format(NUM_DIGITS))

    while True:
        secNumber = getSecretNum()
        print ('I have thought up a number.')
        print ('you have {}guesses to get it.'.format(MAX_GUESSES))

        numGuess = 1
        while numGuess <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print ('Guess #{}'.format(numGuess))
                guess = input ('> ')
                
            clues = getClues(guess, secNumber)
            print(clues)
            numGuess += 1
                
            if guess == secNumber:
                break
            if numGuess > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secNumber))

        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')
        

def getSecretNum():

    numbers = list('0123456789')
    random.shuffle(numbers)

    SecNum = ''
    for i in range(NUM_DIGITS):
        SecNum += str(numbers[i])
    return SecNum
    
def getClues(guess, SecNum):
    if guess == SecNum:
        return 'you got it'
    
    clues = []

    for i in range (len(guess)):
        if guess[i] == SecNum[i]:
            clues.append('fermi')
        
        elif guess[i] in SecNum:
            clues.append('Pico')
    
    if len(clues) == 0:
        return 'Bagels'
    
    clues.sort()
    return ' '.join(clues)
    
if __name__ == '__main__':  
    main()
