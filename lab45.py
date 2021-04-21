import requests
from pprint import pprint
import time

BASE_URL = "https://pythonpractice-b27a8-default-rtdb.firebaseio.com/%s.json"

url1 = BASE_URL % "demo1"
url2 = BASE_URL % "demo2"
url3 = BASE_URL % "demo3"
url4 = BASE_URL % "demo4"

url5 = BASE_URL % "demo5"
url6 = BASE_URL % "demo6"

urls = [url1, url2, url3, url4, url5, url6]

for u in urls:
    time.sleep(1)
    res = requests.delete(u)
    print(res.status_code)