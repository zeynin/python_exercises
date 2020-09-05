#http://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
import random

#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
a = random.sample(range(0, 50), random.randint(1,30))
even = [even for even in a if even % 2 == 0]
print(a, "\n", even)