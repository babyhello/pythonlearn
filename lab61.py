class MyClass(object):
    pass


m1 = MyClass()
print(type(MyClass), type(m1), m1.__class__)
print(type(m1) == m1.__class__)
print(m1.__class__.__bases__)


class MySubclass(MyClass):
    pass
m2 = MySubclass()
print(type(m2), m2.__class__)
print(m2.__class__.__bases__)