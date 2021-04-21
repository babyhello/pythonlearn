import math
import random

print(math.pi)
print(math.sqrt(100), math.sqrt(10), )  # math.sqrt(-1)
print((-1) ** 0.5)
for _ in range(10):
    print(random.randint(1, 10))
lunchs = ['KFC', '7-11', 'Fami', 'Macdonald', "noodle"]
for _ in range(10):
    print(random.choice(lunchs))
cards = ['A', 'K', 'Q', "j", '10', '9']
for _ in range(10):
    random.shuffle(cards)
    print(cards)


