f = open('dummy-file.txt', 'r')
for line in f:
    print(line)
f.close()


with open('dummy-file.txt', 'r') as f:
    for line in f:
        print(line)   # no need to close file. with done this automatically



import time

def some_function():
    time.sleep(1)
    

# %time some_function()  # but this can only be done in python notebook


start_time = int(round(time.time() * 1000))

some_function()

end_time = int(round(time.time() * 1000))
elapsed = end_time - start_time
print("code took %d ms to run." % elapsed)



from contextlib import contextmanager # import the decorator

@contextmanager
def timeit():
    start_time = int(round(time.time() * 1000))
    
    yield   # Remember this from generator 

    end_time = int(round(time.time() * 1000))
    elapsed = end_time - start_time
    print("code took %d ms to run." % elapsed)


with timeit():
    some_function()

def another_function():
    time.sleep(0.5)


with timeit():
    another_function()



    


