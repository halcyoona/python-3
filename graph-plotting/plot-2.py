def fibslow(n):
    if n==1 or n==0:
        return n
    else:
        return fibslow(n-1) + fibslow(n-2)
    
    
def fibfast(n):
    if n<=1:
        return n
    a , b = 0, 1
    for i in range(0, n):
        a, b = b, a+b
    return a


import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline


from_n, to_n = 1, 30
x = range(from_n, to_n)
print(x)


def time_function(fn, start, end):
    from datetime import datetime
    
    times = []
    
    for i in range (start, end):
        start_time = datetime.now()
        
        _ = fn(i) #actuall call of the function dont care about the function value
        
        end_time = datetime.now()
        time_taken = end_time - start_time 
        time_taken = time_taken.microseconds
        
        times.append(time_taken)
        
    return times




fibslow_time = time_function(fibslow, from_n, to_n)
fibfast_time = time_function(fibfast, from_n, to_n)

print (fibslow_time)
print (fibfast_time)



plt.figure()
plt.plot(fibslow_time, label = "fibslow")
plt.plot(fibfast_time, label = "fibfast")
plt.xlabel('n')
plt.ylabel('time(microseconds)')
plt.legend()
