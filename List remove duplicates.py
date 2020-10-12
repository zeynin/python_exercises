#http://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#c = {*set(a).intersection(b)}
c = set(a + b)

print(c)

def uniqueSortedCombined():
    d = sorted(a + b)
    for i in range(1,len(d)):
        if i >= len(d): break
        while(d[i] == d[i-1]):
            d.remove(d[i])

    return d

print(uniqueSortedCombined())

def solution(x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y

print(solution(a+b))