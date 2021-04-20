class Foo:
    def __init__(self, id, name, eName, duration):
        self.id = id
        self.name = name
        self.eName = eName
        self.duration = duration

    def __str__(self):
        return f"course name={self.name}, english name={self.eName}, duration={self.duration}"

    def __repr__(self):
        return f"[id={self.id},name={self.name},eName={self.eName},duration={self.duration}]"


print(Foo)
course1 = Foo("bdpy","資料處理實戰演練","python & Big Data", "35hr")
print(course1, course1)
print("%s,\n%r"%(course1, course1))
print("{0!s},\n{0!r},\n{0!a}".format(course1))