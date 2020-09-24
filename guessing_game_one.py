# http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
import random

answer = random.randint(1,9)
tries = 0

while(1):
    guess = input('Guess a number between 1 and 9: ')

    try:
        guess = int( guess )
    except ValueError:
        #guess = 0 
        print( 'Exiting...' )
        break
    tries += 1

    if( guess == answer ):
        print( 'You guessed it! It only took you', tries, 'tries. Well done.' )
        break
    elif( guess < answer ):
        print( 'A little higher. Guess again!')
    else:
        print( 'Lower....Guess again!')