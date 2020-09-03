#http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
from itertools import chain
from itertools import combinations
from collections import Counter 
import random

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
b = random.sample(range(0, 50), random.randint(1,30))
print(b)
a = random.sample(range(0, 50), random.randint(1,30))
print(a)

z = []
for a_same in a:
    for b_same in b:
        if( a_same == b_same ):
            z.append(b_same)

z = [*set(z)]
print(z)

#y = [set(chain(a,b))] #not quite
#y = [set(b) - set(a)] #not quite
y = [*set(same for same in a + b if same in a and same in b)]
print(y)

#x = [set(a + b)] #nope
#print(x)

x = [*set(a).intersection(b)]
print(x)
