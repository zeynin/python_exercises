#http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

palindrome = input('Enter a string: ')
'''
is_pal = True
index = 0

for i in palindrome:
    index = index - 1
    if( palindrome[index] != i):
        is_pal = False

if is_pal: print("You entered a palindrome!")
else: print("You did not enter a palindrome")
'''

reversed = palindrome[::-1]

if( reversed == palindrome ):
    print('You entered a palindrome!')
else:
    print('You did not enter a palindrome')