class Emp:
    pass


class Engineer(Emp):
    pass


class PM(Emp):
    pass


class HR(Emp):
    pass


emp1 = Emp()
engineer1 = Engineer()
hr1 = HR()
pm1 = PM()
staffs = [(emp1, "Employee1"), (engineer1, "Engineer1"), (pm1, "PM1"), (hr1, "HR1")]
classes = [Emp, Engineer, PM, HR]

for staff, name in staffs:
    for emp_class in classes:
        isA = isinstance(staff, emp_class)
        message1 = 'is a' if isA else 'is not a'
        print(name, message1, emp_class.__name__)
for c1 in classes:
    for c2 in classes:
        isSubclass = issubclass(c1, c2)
        message2 = '{0} a subclass of'.format('is' if isSubclass else 'is not')
        print(c1.__name__, message2, c2.__name__)