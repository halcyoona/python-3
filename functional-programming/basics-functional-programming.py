#Map


from math import sqrt
[sqrt(i) for i in [1,4,9,16]]


map(sqrt,[1,4,9,16])


#so this is like a generator
x = map(sqrt,[1,4,9,16])
list(x)


def mymap(f, seq):
    result = []
    for elt in seq:
        result.append(f(elt))
    return result


mymap(sqrt,[1,4,9,16])



def powerOfTwo(k):
    return 2**k

powerOfTwo(3)



list(map(powerOfTwo,[1,2,3,4]))

#short
list(map(lambda k: k**2, [1,2,3,4]))