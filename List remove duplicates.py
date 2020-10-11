#http://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#c = {*set(a).intersection(b)}
c = set(a + b)

print(c)

def uniqueCombined():
    e = []
    d = a + b
    print(d)
    for i in d:
        if(i not in e):
            e.append(i)
        elif(i in d):
            d.remove(i)
    print(e)
    return d

print(uniqueCombined())