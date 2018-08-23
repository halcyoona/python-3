import time
import threading
global balance
balance = 10000
num_threads = 1010



def fun():
    global balance
    if balance < 10:
        return 
    else:
        time.sleep(1)
        balance -= 10



def run_experiment():
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=fun)
        threads.append(t)
        t.start()
    for i in threads:
        i.join()
    
    print("Balance : %d" % balance)



run_experiment()




balance = 10000


lock = threading.Lock()
def fun():
    global balance
    with lock:
        if balance < 10:
            return 
        else:
            var = balance
            time.sleep(0.000001)
            var -= 10
            balance = var


run_experiment()