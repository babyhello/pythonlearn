lab26_demo_module.py
def foo(a, b):
    return "[foo]result:" + str(a + b)


def bar(a, b):
    return "[bar]result:" + str(a * b)


print(foo(1, 2))
print(bar(3, 4))