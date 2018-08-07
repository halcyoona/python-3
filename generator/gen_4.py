#Tailing file 


import time
def follow(thefile):
    thefile.seek(0,2)
    while True: 
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


logfile = open("test-log")

loglines = follow(logfile)

for line in loglines:
    print(line)
    if line[:1] == ".":
        break