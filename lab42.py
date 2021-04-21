import requests

BASE_URL = "https://pythonpractice-b27a8-default-rtdb.firebaseio.com/%s.json"

url6 = BASE_URL % "demo6"

for i in range(10):
    aRecord = {"name": "Mark", "quantity": 40 + 10 * i}
    r6 = requests.post(url6, json=aRecord)
    print(r6.status_code, r6.content)