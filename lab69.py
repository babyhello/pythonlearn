def func69():
    a = 1
    b = 2
    yield a
    a += b
    yield a


print(type(func69), type(func69()))

f1 = func69()
f2 = func69()
print(next(f1))
print(next(f1))
print(next(f2))
print(next(f2))
for _ in range(10):
    print(next(func69()))

f3 = func69()
print([x for x in f3])