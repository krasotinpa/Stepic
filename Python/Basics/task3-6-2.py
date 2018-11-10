# Name	pka
# Client Id	70327988f931bc3c2322
# Client Secret	01482c02b532eb31f439614cc38d9385
import requests
import json
from operator import itemgetter

client_id = '70327988f931bc3c2322'
client_secret = '01482c02b532eb31f439614cc38d9385'
URL = 'https://api.artsy.net/api/artists/{}'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

artists = []
with open('dataset_24476_4.txt') as f:
    for id in f:
        # инициируем запрос с заголовком
        r = requests.get(URL.format(id.rstrip()), headers=headers)
        r.encoding = 'utf-8'
        # разбираем ответ сервера
        j = json.loads(r.text)
        artists.append((j['sortable_name'],int(j['birthday'])))
        #print(j['sortable_name'],j['birthday'])

[print(i[0]) for i in sorted(artists, key=itemgetter(1,0))]

