# http://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

strings = input('Give me a phrase: ').split() #['this', 'is', 'my', 'name']

def reverseList():
    
    for i in range(1, len(strings) + 1):
        print(strings[i * -1])

reverseList()