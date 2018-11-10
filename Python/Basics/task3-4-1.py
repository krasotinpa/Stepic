import requests
import re

urlA, urlB = input(), input()
URLpattern = r"<a\s+href=\"([^\"]+)\".*>"

found = "No"
res = requests.get(urlA).text
for u in re.findall(URLpattern, res):
    res = requests.get(u).text
    if urlB in re.findall(URLpattern, res):
        found = "Yes"
        break

print(found)
