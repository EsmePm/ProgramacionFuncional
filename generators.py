def alphabet():
    for c in 'abcde':
        yield c #yield es un generador

for x in alphabet():
    print(x)

g = alphabet()

x = next(g)
print(x)
x = next(g)
print(x)

def fiboncaci():
    c = 0
    n = 1
    while True:
        yield c
        c, n = n, c + n

for i in fiboncaci():
    print(i)
    if i > 100:
        break

def identity(it):
    for i in it:
        yield i

#un  generador es parecido a un iterable, hace lo mismo
for i in identity(range(4)):
    print(i)

def chain(it1, it2):
    for x in it1:
        yield x
    for x in it2:
        yield x

for i in chain(range(4), reversed(range(3))):
    print(i)

#generators comprehensions

a = [str(i) for i in range(100)]

a = (str(i) for i in range(100))

import math
m = map(math.sqrt, range(100))
m = map(lambda x : math.sqrt(x) + 1, range(100))

m2 = (math.sqrt(x) for x in range(100))
m2 = (math.sqrt(x)+1 for x in range(100))
