def func70():
    x = 123
    y = 45
    z = 67
    y = yield x
    yield y + z

f1 = func70()
print(next(f1))
print(f1.send(100))