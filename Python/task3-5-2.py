import requests

with open('input.txt') as inf:
    URL = inf.readline().strip()

r = requests.get(URL)
while r.text[:2] != 'We':
    URL = r.text.strip()
    r = requests.get('https://stepik.org/media/attachments/course67/3.6.3/' + URL)

print(r.text)

