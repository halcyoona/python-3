#!pip install requests
import requests

import time
from contextlib import contextmanager # import the decorator

@contextmanager
def timeit():
    start_time = int(round(time.time() * 1000))
    
    yield   # Remember this from generator 

    end_time = int(round(time.time() * 1000))
    elapsed = end_time - start_time
    print("code took %d ms to run." % elapsed)


gists = ['https://gist.github.com/recluze/1d2989c7e345c8c3c542',
'https://gist.github.com/recluze/a98aa1804884ca3b3ad3',
'https://gist.github.com/recluze/5051735efe3fc189b90d',
'https://gist.github.com/recluze/460157afc6a7492555bb',
'https://gist.github.com/recluze/5051735efe3fc189b90d',
'https://gist.github.com/recluze/c9bc4130af995c36176d']


def get_gists(g):
    print("Starting request : %s" %g)
    r = requests.get(g)
    g_length = len(r.text)
    print("Got response of length: %d" %g_length)




with timeit():
    for g in gists:
        get_gists(g)
    print ("ALl Done")




#Lets d that parallel
import threading



with timeit():
    threads = []
    for g in gists:
        # create workers
        t = threading.Thread(target = get_gists, args=(g,))
        
        #Go
        t.start()
        
        #keep a list for records
        threads.append(t)
        
    for t in threads:
        t.join()

    print("All Done")
        
        
