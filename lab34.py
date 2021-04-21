import itertools

a1 = ['a', 'b', 'c', 'd', 'e']
a2 = [1, 2, 3, 4, 5]

c1 = itertools.chain(a1, a2)
print(type(c1), [x for x in c1])
print([x for x in c1])
l1 = a1 + a2
print(l1)

l2 = list(itertools.chain(a1, a1, a2))
print(l2)
print(l2)
print([l for l in zip(a1, a2)])
c2 = tuple(itertools.combinations(a1, 3))
print(len(c2), c2)
p2 = tuple(itertools.permutations(a1, 3))
print(len(p2), p2)