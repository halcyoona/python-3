import threading
import time

num_threads = 5
iteration_in_one_thread = 100


counter = 0 # just a variable


def f():
    global counter
    
    for i in range(iteration_in_one_thread):
        v = counter
        time.sleep(0.000000000001)
        v += 1
        counter = v
        
def run_experiment():
    global counter
    counter = 0
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=f)
        threads.append(t)
        t.start()
    for i in threads:
        i.join()
    
    print("calculated Value : %d" % counter)
    print(" expected Value : %d" % (num_threads * iteration_in_one_thread))


run_experiment()


# This we will expecting

counter  = 0


v1 = counter    #this is done by first thread
v1 += 1
counter = v1


v2 = counter
v2 += 1
counter = v2

print (counter)



#this is what actually happens


counter = 0

#thread 1 start
v1 = counter 
v1 += 1
#---- break


#thread 2 start
v2 = counter
v2 += 1
counter = v2
#thread 2 done

#----back to thread 1
counter = v1
#--- thread 1 done

print(counter)



# what we need to do is ensure that critical sections are executed all in one go
# we can remove this problem by using locks

lock = threading.Lock()


def f():
    global counter
    
    for i in range(iteration_in_one_thread):
        lock.acquire()   # critical part start
        v = counter
        time.sleep(0.000000000001)
        v += 1
        counter = v
        lock.release() #critical part ends


run_experiment()



def f():
    global counter
    
    for i in range(iteration_in_one_thread):
        with lock:
            v = counter
            time.sleep(0.000000000001)
            v += 1
            counter = v




run_experiment()