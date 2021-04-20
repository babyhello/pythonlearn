class Person:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age


x = 5
y = Person(5)
print(hex(id(x)))
print("y", hex(id(y)), "y.age", hex(id(y.age)))
print(x is y.age, x == y.age)
x = 6
y.age = 6
print(hex(id(x)))
print('y', hex(id(y)), "y.age", hex(id(y.age)))
print(x is y.age, x == y.age)
z = y
print(z is y, z == y)
t = Person(6)
print(t is y, t == y)