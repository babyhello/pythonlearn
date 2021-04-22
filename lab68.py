class MyTeam:
    def __init__(self, limit=10):
        # print("my team initialized")
        self.counter = 0
        self.limit = limit
        pass

    def __iter__(self):
        # print("begin to iterate")
        return self

    def __next__(self):
        # print("iterate")
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration


m1 = MyTeam(5)
print(m1.counter)
# for i in m1:
#     print(i)
print([x for x in m1])
m2 = MyTeam()
print(next(m2))
print(next(m2))
print(next(m2))
print(next(m2))
print(next(m2))
print(next(m2))
print(next(m2))
print(next(m2))
print(next(m2))
print(next(m2))
print(next(m2))