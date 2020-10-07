# http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

number = int( input("Give me a number: ") )
'''divisor_list = []

for val in range(1, divisors + 1):
    if (divisors % val) == 0:
        divisor_list.append(val)
'''

def divisors( divisor = 1 ): 
    divisor_list = []
    
    for x in range(1, divisor + 1):
        if (divisor % x) == 0:
            divisor_list.append(x)
        
    return divisor_list

print( divisors(number) )
