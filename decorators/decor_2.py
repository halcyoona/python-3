


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


#We have to do some stuff before calling to fib function




def memoize(f):    
    mem = {}
    
    def memoized_function(n):      #typically called a wrapper
        if n not in mem:
            mem[n] = f(n)
        return mem[n]
    
    return memoized_function 
            


fib = memoize(fib)   #not calling fib at that time

print(fib(111))


def memoize(f):    
    mem = {}
    
    def wrapper(x):      
        if x not in mem:
            mem[x] = f(x)
        return mem[x]
    
    return wrapper 


@memoize       #This is called a decorator, Equals: fib = memoize(fib)
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


 print(fib(50))