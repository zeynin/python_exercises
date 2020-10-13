# http://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

strings = input('Give me a phrase: ') 

def reverseList(asIs=['this', 'is', 'my', 'name']):
    #strings.split()
    #for i in range(1, len(strings) + 1):
    #    print(strings[i * -1])

    #solution
    #return ' '.join(w.split()[::-1])
 
    return [i for i in asIs.split()[::-1]]
         
print(reverseList(strings))