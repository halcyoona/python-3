text = """03-02-2025 10:22pm: My email address is testuser@gmail.com and I check
it often. You should send me an email!"""


haystack = "Date: 03-02-2025"

needle = "Da"

import re

re.match(needle, haystack)

match = re.match(needle, haystack)

match.group(0)

needle = 'Date: \d\d'   #\d matched any digit

res = re.match(needle, haystack)
if res:
    print("found!")
    print(res.group(0))
else:
    print("Not found")


needle = "......\d"   #dot matches any thing
res = re.match(needle, haystack)
if res:
    print("found!")
    print(res.group(0))
else:
    print("Not found")



needle = ".....\s\d\d"   #\s matches space
res = re.match(needle, haystack)
if res:
    print("found!")
    print(res.group(0))
else:
    print("Not found")



needle = ".{5}\s\d{2}"  
res = re.match(needle, haystack)
if res:
    print("found!")
    print(res.group(0))
else:
    print("Not found")




needle = ".*\d{2}"  #.* means any thing any number of time and two digits
res = re.match(needle, haystack)
if res:
    print("found!")
    print(res.group(0))
else:
    print("Not found")



needle = ".*?\d{2}"  #.*? means any thing any number of time but not too greedy
res = re.match(needle, haystack)
if res:
    print("found!")
    print(res.group(0))
else:
    print("Not found")
