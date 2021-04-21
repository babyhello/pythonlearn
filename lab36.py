import json

x1 = ['100', 50, 3.14, None, [3, 5]]
d1 = json.dumps(x1)
print(type(x1), x1)
print(type(d1), d1)

x2 = {'name': "Mark", 'age': 45, 'taught': ['Java', 'CPP', "Python"]}
d2 = json.dumps(x2)
print(type(x2), x2)
print(type(d2), d2)

x3 = json.loads(d1)
print(type(x3), x3)

x4 = json.loads(d2)
print(type(x4), x4)

print(x1 == x3)
print(x2 == x4)