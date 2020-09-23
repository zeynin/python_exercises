# http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
'''Rock beats scissors
Scissors beats paper
Paper beats rock'''

player1 = ''
player2 = ''
ESC = chr(27) #0x1b

def player1Test( x ):
    b = x in player1
    return b 

def player2Test( x ):
    b = x in player2
    return b 

while( 1 ):
    player1 = input("PLAYER 1: What is your play? Enter rock, paper or scissors. ")
    if( player1Test(ESC) ): break # escape character

    player2 = input("PLAYER 2: What is your play? Enter rock, paper or scissors. ")
    if( player2Test(ESC) ): break # escape character

    if( player1Test(player2) ):
        print('Draw.')
        continue

    if( player1Test('rock') or player2Test('rock') ):
        #rock beats scissors
        if( player1Test('scissors') ):
            print('You won PLAYER 2')
            continue
        elif( player2Test('scissors') ):
            print('You won PLAYER 1')
            continue
    
    if( player1Test('scissors') or player2Test('scissors') ):
        #Scissors beats paper
        if( player1Test('paper') ):
            print('You won PLAYER 2')
            continue
        elif( player2Test('paper') ):
            print('You won PLAYER 1')
            continue
    
    if( player1Test('paper') or player2Test('paper') ):
        #Paper beats rock
        if( player1Test('rock')):
            print('You won PLAYER 2')
            continue
        elif( player2Test('rock') ):
            print('You won PLAYER 1')
            continue
    
    print('PLAYER 1 = ', player1, 'PLAYER 2 = ', player2)

print( 'All done.' )