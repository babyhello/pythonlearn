class MyTeam:
    def __init__(self):
        # print("my team initialized")
        self.counter = 0
        pass

    def __iter__(self):
        # print("begin to iterate")
        return self

    def __next__(self):
        # print("iterate")
        if self.counter < 10:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration


m1 = MyTeam()
print(m1.counter)
# for i in m1:
#     print(i)
print([x for x in m1])