import requests
import json
r = requests.get('https://randomuser.me/api/?results=50')
data = r.json()['results'][0]
print(data)
