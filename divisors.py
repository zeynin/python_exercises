#http://www.practicepython.org/exercise/2014/02/26/04-divisors.html

divisors = int( input("Give me a number: ") )
'''divisor_list = []

for val in range(1, divisors + 1):
    if (divisors % val) == 0:
        divisor_list.append(val)
'''

divisor_list = [*filter( lambda x: (divisors % x) == 0, range(1, divisors + 1) )]
print(divisor_list) 