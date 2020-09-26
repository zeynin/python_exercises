# http://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
import random

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#c = {*set(a).difference(b)}

#x = [1, 2, 3]
#y = [5, 10, 15]
#allproducts = [a*b for a in x for b in y]
#Output: [5, 10, 15, 10, 20, 30, 15, 30, 45]
#[EXPRESSION FOR_LOOPS CONDITIONALS]

a = random.sample(range(0, 50), random.randint(1,30))
b = random.sample(range(0, 50), random.randint(1,30))
c = sorted({*set(a).intersection(b)})
d = {i for i in a if i in b}
#result = [i for i in a if i in b]
result = [i for i in set(a) if i in b]
print(a, '\n', b, '\n', c, '\n', result)
