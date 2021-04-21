import json
import requests

URL1 = "https://bugzilla.mozilla.org/rest/bug/35"

res = requests.get(URL1)
print(type(res), res.status_code)
print(type(res.text), res.text[:50])
print(type(res.json()), res.json())
firstBug = res.json()["bugs"][0]
print(firstBug["summary"])
print(firstBug["assigned_to_detail"]["real_name"])
print(firstBug["cc_detail"][0])