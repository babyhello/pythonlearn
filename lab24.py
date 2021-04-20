import collections
import time
from pprint import pprint
#import multiprocessing
import concurrent.futures
import os

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


def transform(x):
    print(f"[{os.getpid()}]process record:{x.name}")
    time.sleep(3)
    r1 = {'name': x.name, 'revenue': x.attendee * 5000}
    print(f"[{os.getpid()}]done process record:{x.name}")
    return r1


if __name__ == '__main__':
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
    #with concurrent.futures.ProcessPoolExecutor() as executor:
        result = tuple(executor.map(transform, courses))
    end = time.time()

    print(f"---total time:{end - start:.2f} seconds---")
    pprint(result)