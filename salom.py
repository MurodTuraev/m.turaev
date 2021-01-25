import requests
import json
r = requests.get('https://randomuser.me/api/')
data = r.json()['results']
print(data)
