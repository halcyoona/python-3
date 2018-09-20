import re

text = """03-02-2025 10:22pm: My email address is testuser@gmail.com and I check
it often. You should send me an email!"""

haystack = "Date: 03-02-2025"

str_date = ".*?"      # You can also use: ".*\s"
str_day = "\d{2}"


# needle = ".*?\d{2}"
needle = str_date + str_day
res = re.match(needle, haystack)
if res:
    print("Found!")
    print(res.group(0))
else:
    print("Not found!")



haystack = text
print(haystack)

str_day = "\d{2}-\d{2}-\d{4}"

str_time = "\d{2}:\d{2}pm"

needle = str_day + "\s" + str_time

res = re.match(needle, haystack)
if res:
    print("Found!")
    print(res.group(0))
else:
    print("Not found!")


text = """03-02-2025 10:22am: My email address is testuser@gmail.com and I check
it often. You should send me an email!"""

haystack = text

str_day = "\d{2}-\d{2}-\d{4}"

str_time = "\d{2}:\d{2}pm"

needle = str_day + "\s" + str_time

res = re.match(needle, haystack)
if res:
    print("Found!")
    print(res.group(0))
else:
    print("Not found!")


text = """03-02-2025 10:22am: My email address is testuser@gmail.com and I check
it often. You should send me an email!"""

haystack = text

str_day = "\d{2}-\d{2}-\d{4}"

str_time = "\d{2}:\d{2}[apAP][mM]"

needle = str_day + "\s" + str_time

res = re.match(needle, haystack)
if res:
    print("Found!")
    print(res.group(0))
else:
    print("Not found!")




text = """03-02-2025 10:22am: My email address is testuser@gmail.com and I check
it often. You should send me an email!"""

haystack = text

str_prefix = ".*"

str_username = "[a-zA-Z0-9.]*"

str_domain = ".*\..*?"

str_email = str_username + "@" + str_domain

needle = str_prefix + "\s" + str_email +"\s"

res = re.match(needle, haystack)
if res:
    print("Found!")
    print(res.group(0))
else:
    print("Not found!")




print(needle)