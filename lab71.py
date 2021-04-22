def func71():
    a = 1
    for i in range(10):
        a += 1
        yield a
        #pass
    pass
f1 = func71()
print(next(f1))
print([i for i in f1])
f2 = func71()
print([j for j in f2])