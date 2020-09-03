#http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

print('hell0')

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#l = []

#less_than_ten = lambda x: x < 10
#for val in filter(less_than_ten, a):
#    print(val)
#    l.append(val)

l = [val for val in a if val < 5]

print(l, a)

