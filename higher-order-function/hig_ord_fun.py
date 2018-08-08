x = 24

def square(x):
    return x**2



square(5)



square

f = square

f

f(6)


#Let we want to write a function to calculate the sum of the square 

def summation(low, high):
    total = 0 
    for i in range(low, high+1):
        val = i ** 2
        total += val
    return total



print(summation(1,3))



def summation(low, high):
    total = 0 
    for i in range(low, high+1):
        val = i ** 3
        total += val
    return total



def square(x):
    return x**2
def cube(x):
    return x**3





def summation(low, high, fn):
    total = 0 
    for i in range(low, high+1):
        val = fn(i)
        total += val
    return total




print(summation(1, 3, square))

print(summation(1, 3, cube))

print(summation(1, 3, lambda i: i**2)) # lambda is an anonymous function.


#Summation is a higher order function because it takes another function as a input