import tempfile
import shutil 
import os
from contextlib import contextmanager

try:
    name = tempfile.mkdtemp()
    print("created temp directory : %s" %name)
    
    filename = os.path.join(name,"somefile.txt")
    
    
    #Do something
    
    with open(filename, "w") as f:
        print("opened file : %s" %filename)
        f.write("Dummy Text")
        
        
finally:
    print("deleting directory: %s" %name)
    shutil.rmtree(name)





@contextmanager
def tempdr(filename):
    try:
        name = tempfile.mkdtemp()
        print("created temp directory : %s" %name)

        filename = os.path.join(name,"somefile.txt")


        #Do something

        with open(filename, "w") as f:
            print("opened file : %s" %filename)
            yield f
    finally:
        print("deleting directory: %s" %name)
        shutil.rmtree(name)

    

with tempdr("mehmood") as f:
    print("doing something with the file")
    
