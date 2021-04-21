import requests

BASE_URL = "https://pythonpractice-b27a8-default-rtdb.firebaseio.com/%s.json"
url4 = BASE_URL % "demo4"
# r4 = requests.put(url4, json=["hello", "中文", 500, None, 3.14])
# print(r4.status_code, r4.content)
patchObject = {'0':"Hello World",'3':'後來加入的資料','5':'final data','10':"extra data"}
p4 = requests.patch(url4, json=patchObject)
print(p4.status_code, p4.content)

url5 = BASE_URL % "demo5"
patchObject2 = {'name':"Mark Ho", "location":"taipei"}
p5 = requests.patch(url5, json=patchObject2)
print(p5.status_code, p5.content)
# r5 = requests.put(url5, json={'name': 'Mark', 'age': 45, 'field': ['mobile', 'app']})
# print(r5.status_code, r5.content)