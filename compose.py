# es la continuacion de partial.py
# composición
from operator import add, mul
from functools import partial
from pymonad.tools import curry

x = 2
def compose2(f, g):
    def fn(x):
        return f(g(x))
    return fn
#opción 1
add(2, mul(3, x))

f = partial(add, 2)
g = partial(mul, 3)
#opción 2
f(g(x))
#opción 3
addmul1 = partial(add, 2)(partial(mul, 3)(x))
#opción 4
addmul2 = compose2(partial(add, 2), partial(mul, 3))

for i in reversed(range(10)):
    print(i)

countdown = compose2(reversed, range)
for i in countdown(10):
    print(i)

#p(q(r(s(x))))
#f = compose2(p, q)
#g = compose2(f, r)
#h = compose2(g, s)
#h(x)

# Como texto letras son numeros y compose es una suma 
# (((p + q) + r ) + s)
import functools
l = [1, 2, 3, 4]
my_add = functools.reduce(add, l)
print(my_add)

def compose(*f):
    def compose2(f, g):
        def fn(x):
           return f(g(x))
        return fn
    return functools.reduce(compose2, f, lambda x: x)

#queda de tarea probar compose
test = []

#composicion de funciones con pyMonad
@curry(1)
def reversedc(x):
    return reversed(x)

@curry(1)
def rangec(x):
    return range(x)
from pymonad.reader import Compose

countdown = Compose(range).then(reversed)
#countdown = reversedc * rangec
#countdown = compose2(reversed, range)

for i in countdown(7):
    print(i)

countdown2 = Compose(rangec). then(reversedc)

print("---")
for i in countdown2(5):
    print(i)