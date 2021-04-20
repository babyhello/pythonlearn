print({'a': 0, 'b': 1})
print({'a': 0, 'b': 1, 'a': 0 + 500, 'b': 1 + 500})
l1 = ['a', 'b'] + ['c']
print(l1)
d1 = {'a': ['apple'], 'b': ['banana']}
d2 = {'c': ['cookie'], 'b': ['banana', 'beef']}
print({**d1, **d2})