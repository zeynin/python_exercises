# http://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

a = [5, 10, 15, 20]

b = [a[0],a[-1]]

print(a, b)

def firstLast(a):
    return [[a[0],a[-1]]]

print(firstLast(a))