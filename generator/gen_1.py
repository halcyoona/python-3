def myrange(n):
    x = 0
    while x < n:
        yield x      #Yield turns the function into a generator
        x += 1



print(type(myrange(4)))


for i in myrange(5):
    print(i)



def countdown(n):
    while n > 0:
        print("computing Next Number: ")
        yield n
        n -= 1




for i in countdown(5):
    print(i)


v = countdown(5)


next(v)