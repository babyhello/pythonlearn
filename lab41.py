import requests

BASE_URL = "https://pythonpractice-b27a8-default-rtdb.firebaseio.com/%s.json"

url1 = BASE_URL % "demo1"
r1 = requests.put(url1, json="hello firebase from python!!!")
print(r1.status_code, r1.content)


url1 = BASE_URL % "demo1"
r1 = requests.put(url1, json="hello firebase from python!!!")
print(r1.status_code, r1.content)

url2 = BASE_URL % "demo2"
r2 = requests.put(url2, json=13579)
print(r2.status_code, r2.content)

url3 = BASE_URL % "demo3"
r3 = requests.put(url3, json="是否可以支援中文!!!")
print(r3.status_code, r3.content)

url4 = BASE_URL % "demo4"
r4 = requests.put(url4, json=["hello", "中文", 500, None, 3.14])
print(r4.status_code, r4.content)

url5 = BASE_URL % "demo5"
r5 = requests.put(url5, json={'name': 'Mark', 'age': 45, 'field': ['mobile', 'app']})
print(r5.status_code, r5.content)