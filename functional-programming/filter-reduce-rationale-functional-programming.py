#Great intro here: 
#https://www.codenewbie.org/blogs/object-oriented-programming-vs-functional-programming 
#(https://www.codenewbie.org/blogs/object-oriented-programming-vs-functional-programming)


#Filter
x = filter(str.isalpha ,['2','3','a','b','5'])
print(x)

list(x)

#Reduce
from functools import reduce

def add(x,y):
    return x+y



reduce(add,[2,3,5],0)


lines = [
"A cow is a domestic animal. A cow is a very useful animal.",
"A cow is kept in barns. Cow milk is very healty.",
"Another cow."
]


#let count words in all these three lines


from collections import defaultdict
def count_words(s):    #takes in a single string 
    counts = defaultdict(int)    # initialize keys not already present
    
    for word in s.split():
        counts[word] += 1
    
    return dict(counts)     # don't want to send back the default dict


#see more about collection here:
#https://docs.python.org/dev/library/collections.html


dict(count_words(lines[0]))

list(map(count_words,lines))


counts_map = list(map(count_words,lines))


def reduce_counts(x, y):
    print('x:', x)
    print('y:', y)
    print('-----')
    return {'word': 0}

from collections import Counter
def reduce_counts(x, y):
    counter = Counter()   #{key:value} where value is not count 
    
    counter.update(x)    #Get numbers from x
    counter.update(y)    #Add counts from y
    return dict(counter)


print(reduce(reduce_counts,counts_map,{}))

#Hadoop and spark are used for big data processing

#functional programming is very usefull in javascript