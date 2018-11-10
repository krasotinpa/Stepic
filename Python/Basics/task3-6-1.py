import requests

fname = "dataset_24476_3 (1).txt"
URL = 'http://numbersapi.com/{}/math'
params = {'json': 'true'}

with open(fname) as f:
    for num in f:
        res = requests.get(URL.format(num.rstrip()), params=params)
        print('Interesting' if res.json()['found'] else 'Boring')
        

