# http://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

strings = input('Give me a phrase: ') 

def reverseList(asIs=['this', 'is', 'my', 'name']):
    #strings.split()
    #for i in range(1, len(strings) + 1):
    #    print(strings[i * -1])

    #solution
    #return ' '.join(asIs.split()[::-1])
 
    #return ' '.join([i for i in asIs.split()[::-1]])

    '''
    toBe = asIs.split()
    toBe.reverse()
    return ' '.join(toBe)
    '''

    #return ' '.join( reversed(asIs.split()) )

    y = asIs.split()
    result = []
    for word in y:
        result.insert(0,word)
    return " ".join(result)
         
print(reverseList(strings))