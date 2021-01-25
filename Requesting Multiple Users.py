import requests
import json
r = requests.get('https://randomuser.me/api/?results=50')
data = r.json()['results']
for i in data:
    print(i['name']['first'])
