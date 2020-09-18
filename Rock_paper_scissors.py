# http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
'''Rock beats scissors
Scissors beats paper
Paper beats rock'''

player1 = ''
player2 = ''

while( (player1 or player2) != 'esc' ):
    player1 = input("PLAYER 1: What is your play? Enter rock, paper or scissors. ")
    player2 = input("PLAYER 2: What is your play? Enter rock, paper or scissors. ")

    if(player1 == player2):
        print('Draw.')
        continue

    if( (player1 or player2) == 'rock'):
        #rock beats scissors
        if(player1 == 'scissors'):
            print('You won PLAYER 2')
        elif(player2 == 'scissors'):
            print('You won PLAYER 1')
    elif( (player1 or player2) == 'scissors'):
        #Scissors beats paper
        if(player1 == 'paper'):
            print('You won PLAYER 2')
        elif(player2 == 'paper'):
            print('You won PLAYER 1')
    elif( (player1 or player2) == 'paper'):
        #Paper beats rock
        if(player1 == 'rock'):
            print('You won PLAYER 2')
        elif(player2 == 'rock'):
            print('You won PLAYER 1')
        else:
            print('PLAYER 1 = ', player1, 'PLAYER 2 = ', player2)

print( 'All done.' )