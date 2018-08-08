def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)



fib(3)

#%time fib(35)


def logger(f):
    
    #f will be remembered by the wrapper even after we exit the logger
    #this is the concept of a closure
    
    def wrapper(n):
        print("I am going to call a function.")
        v = f(n)
        print("The function return : ", v)
    
    
    return wrapper 
        


logged_fib = logger(fib) # we are not calling a function we are just creating a new funciton


logged_fib(1)