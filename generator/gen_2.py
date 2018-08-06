import random

def random_gen(low, high, num):
    i = 0
    while i < num:
        yield random.randrange(low, high)
        i += 1



r = random_gen(0, 100, 5)


print(type(r))

print(list(r))


#this give a infinite list
def random_gen_inf(low, high):
    while True:
        yield random.randrange(low, high)


r = random_gen_inf(0, 100)


print(next(r))