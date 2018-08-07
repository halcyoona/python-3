import time

%time v = [ i**2 for i in range(10000000)] #list #stays in memory
print(v[:20])


%time g = (i**2 for i in range(10000000))  #generator not just loaded to the memory called when specifically needed and generator is always with parathesis
print(next(g))


#Simple way

wwwlog = open("access-log")
for line in wwwlog:
    print (line)
    break

wwwlog = open("access-log")
total = 0

for line in wwwlog:
    bytestr = line.rsplit(None, 1)[1]
    if bytestr != '-':
        total += int(bytestr)
    
print ("Total = ",total )


# Generator 

wwwlog = open("access-log")
bytecolumn = (line.rsplit(None, 1)[1] for line in wwwlog)
bytes = (int(x) for x in bytecolumn if x != '-')

print('Total = ', sum(bytes))