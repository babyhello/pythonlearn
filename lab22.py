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

course_by_field = reduce(lambda acc, val: {**acc, **{val.field: acc[val.field] + [val.name]}}
                         , courses, {'python': [], 'android': [], 'blockchain': [],
                                     'js': [], 'frontend': []})
pprint(course_by_field)