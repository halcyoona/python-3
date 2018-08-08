def sqrt(x, guess =0.1):
    print("trying ", guess, "-- value ", guess * guess)
    if good_enough(guess, x):
        return guess
    else:
        guess = improve_guess(guess, x)
        return sqrt(x, guess)
    



def good_enough(guess, x):
    if abs(guess * guess - x) < 1:
        return True
    else:
        False



def avg(a, b):
    return (a + b ) /2.0

def improve_guess(guess, x):
    return avg(guess, float(x)/guess)



sqrt(36)

print("--------------------------------------------------------------")


def sqrt(x, is_ge = good_enough, guess =0.1):
    print("trying ", guess, "-- value ", guess * guess)
    if is_ge(guess, x):
        return guess
    else:
        guess = improve_guess(guess, x)
        return sqrt(x, is_ge, guess)

#if the function in parameter is not given use the good_enough function else use the given function to calculate good_enough


#By the nuclear reactor people
def very_accurate_good_enough(guess, x):
    return abs(guess * guess - x)  < 0.000000001



sqrt(36, very_accurate_good_enough)



#The variable is_ge is termed as a "callback" --some function that you send to another piece of code.That piece of code called this function back at a later point in time