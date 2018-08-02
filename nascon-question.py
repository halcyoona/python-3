
#This function takes two arguments.First the number from which binary number is generated and second argument is the pattern that we have to find in that binary number.

def f(n):
    if n == 1 or n == 0:
        return str(n)
    return f(n-1)+f(n-2)

def fun(n, p):
    count = 0 
    binary = f(n)
    length = len(binary)
    l = len(str(p))
    for i in range(length-1):
        pat = binary[i:l+i]
        if pat == str(p):
            count += 1
    return count

fun(4,110)