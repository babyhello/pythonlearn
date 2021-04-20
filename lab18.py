import collections
from pprint import pprint
from functools import reduce

course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])
vue = course(name='vue', field='frontend', attendee=10, remote=True)
poop = course(name='poop', field='python', attendee=10, remote=False)
bdpy = course(name='bdpy', field='python', attendee=15, remote=True)
pykt = course(name='pykt', field='python', attendee=20, remote=True)
aiocv = course(name='aiocv', field='python', attendee=5, remote=False)
andbiz = course(name='andbiz', field='android', attendee=10, remote=True)
bcic = course(name='bcic', field='blockchain', attendee=10, remote=True)
nojs = course(name='nodejs', field='js', attendee=12, remote=True)
react = course(name='react', field='frontend', attendee=20, remote=False)
courses = (vue, poop, bdpy, pykt, aiocv, andbiz, bcic, nojs, react)


def reducer(acc, val):
    acc.setdefault(val.field, [])
    acc[val.field].append(val.name)
    return acc


course_by_field = reduce(reducer, courses, {})
pprint(course_by_field)


import collections
from pprint import pprint
from functools import reduce
import itertools

course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])
vue = course(name='vue', field='frontend', attendee=10, remote=True)
poop = course(name='poop', field='python', attendee=10, remote=False)
bdpy = course(name='bdpy', field='python', attendee=15, remote=True)
pykt = course(name='pykt', field='python', attendee=20, remote=True)
aiocv = course(name='aiocv', field='python', attendee=5, remote=False)
andbiz = course(name='andbiz', field='android', attendee=10, remote=True)
bcic = course(name='bcic', field='blockchain', attendee=10, remote=True)
nojs = course(name='nodejs', field='js', attendee=12, remote=True)
react = course(name='react', field='frontend', attendee=20, remote=False)
courses = (vue, poop, bdpy, pykt, aiocv, andbiz, bcic, nojs, react)
pprint(courses)
print("---sort---")
sorted_courses = sorted(courses, key=lambda x: x.field)
pprint(sorted_courses)
for c in itertools.groupby(sorted_courses, lambda x: x.field):
    # print(type(c), len(c))
    # print(type(c[0]), type(c[1]))
    print("now handling %s" % c[0])
    pprint([p for p in c[1]])
course_by_field = [(c[0], list(c[1]))
                   for c in itertools.groupby(sorted_courses, lambda x: x.field)]
pprint(course_by_field)
course_by_field2 = {c[0]: list(c[1])
                    for c in itertools.groupby(sorted_courses, lambda x: x.field)}
pprint(course_by_field2)