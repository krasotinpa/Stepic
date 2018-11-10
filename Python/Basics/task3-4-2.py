import requests
import re

URL = input()
#URL = 'http://pastebin.com/raw/hfMThaGb'

site_pattern = re.compile(r'<a[^>]*?href=["\'](?:[a-z]+://)?([^\.]{2}[^:/"\']+).*?["\'][^>]*?>', flags=re.I)
t = requests.get(URL).text

'''
print(t)
with open("inp.txt", "w", encoding='utf8') as f:
    f.write(t)
'''

print('\n'.join(sorted(set(site_pattern.findall(t)))))

'''
http://pastebin.com/raw/hfMThaGb
'''