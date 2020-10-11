# http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

def fibonacci(max=10):
    a = [1,1]

    for i in range(1,max-1):
        #a.append(i)
        next = a[i] + a[i-1]
        #print(i,a[i],a[i-1], next)
        a.append(next)
       # i += 1
 
    return a

print(fibonacci(3))