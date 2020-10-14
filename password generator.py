# http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

import random

def generateSpecialCharacters():
    #0x21,0x7f visible characters
    return random.randrange(0x21,0x7f)

password = []
maxChars = 12

while( maxChars ):
    password.append( chr(generateSpecialCharacters()) )
    maxChars -= 1

print( ''.join(password) )

#s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample( str(range(0x21,0x7f)), passlen ))
print(p)
