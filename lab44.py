import requests
from pprint import pprint

BASE_URL = "https://pythonpractice-b27a8-default-rtdb.firebaseio.com/%s.json"

url1 = BASE_URL % "demo1"
url2 = BASE_URL % "demo2"
url3 = BASE_URL % "demo3"
url4 = BASE_URL % "demo4"

url5 = BASE_URL % "demo5"
url6 = BASE_URL % "demo6"

g1 = requests.get(url1)
print(type(g1.json()), g1.json())
g2 = requests.get(url2)
print(type(g2.json()), g2.json())
g3 = requests.get(url3)
print(type(g3.json()), g3.json())
g4 = requests.get(url4)
print(type(g4.json()), g4.json())
g5 = requests.get(url5)
print(type(g5.json()), g5.json())

g6 = requests.get(url6)
print(type(g6.json()), g6.json())
resultDict = g6.json()

pprint([k for k in resultDict.keys()])
pprint([v for v in resultDict.values()])
pprint([f"{k}/{v}" for (k, v) in resultDict.items()])