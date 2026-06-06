import random
NUM_DIGITS = 3
MAX_GUSSES = 10 

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
        secretnumber = getSecretNum()
        print ('I have thought up a number.')
        print ('you have {}guesses to get it.'.format(MAX_GUSSES))

        numGuess = 1
        

def getSecretNum():

    numbers = {1,2,3,4,5,6,7,8,9}
    random.shuffle(numbers)

    SecNum = ''
    for i in range(NUM_DIGITS):
        SecNum += str(numbers(i))
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
    
    if clues == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)
    
if __name__ == '__main__':  
    main()
