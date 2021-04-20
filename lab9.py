import collections

course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])
print(type(course))
print(course)

poop = course(name='poop', field='python', attendee=10, remote=False)
print(poop)
print(poop.name, poop.field, poop.attendee)
# poop.name='aiocv'

l1 = ['a', 'b', 'c']
s1 = "abc"
l1[1] = 'B'
print(l1)
# s1[1]='B'