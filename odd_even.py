#http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

initial_num = int( input('Give me a number: ') )

if (initial_num % 2) != 0:
    #odd
    print("That's odd")
else:
    print("Even steven")

    if (initial_num % 4) == 0:
        print("Four!")

num, check = map( int, input('Give me two more numbers: ').split() )

if (num % check) == 0:
    print("Division")
else:
    print('nothing to divide')