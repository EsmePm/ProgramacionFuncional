#parcialización o funciones parciales
#por medio de closer define primero a la funcion parcial
def maxn(n):
    def f(x):
        return max(n,x)
    return f

max0 = maxn(0)
print(max0(3))
print(max0(-1))

def max0(x):
    return max(0, x)

map(lambda x: max(0,x), [1, -3, 5, -7])

m = map(maxn(3), [1, 2, 3, 4, 5])

def quad(a, b, c, x):
    return a*x*x + b*x + c

def quad_abc(a, b, c):
    def f(x):
        return quad(a, b, c, x)
    return f

my_quad = quad_abc(1, -3, 2)
print(my_quad(0))
print(my_quad(1))
print(my_quad(2))

def quad_ab(a, b):
    def f(c, x):
        return quad(a, b, c, x)
    return f

my_quad = quad_ab(1, -3)
print(my_quad(2, 0))
print(my_quad(2, 1))
print(my_quad(2, 2))

from functools import partial

max0 = partial(max, 0)
print(max0(3))
print(max0(-1))

m = map(partial(max, 0), [1, 2, 3, 4, 5])

quad3 = partial(quad, 1, -3, 2)
print(quad3(0))
print(quad3(1))
print(quad3(3))

quad2 = partial(quad, 1, -3)
print(quad2(2, 0))
print(quad2(2, 1))
print(quad2(2, 3))

#quad_ac = partial(quad, 1, 2) #partial asocia los valores correspondientes a la definicion de la funcion

def quad_ac(a, c):
    def f(b, x):
        return quad(a, b, c, x)
    return f

def make_print(sep):
    def f(*args):
        return print(*args, sep= sep)
    return f

print_csv = make_print(", ")
print_csv(1, 2, 3)

print_colon = make_print(": ")
print_colon (1, 2, 3)

#currificación
#se instalo pymonad desde https://pypi.org/project/PyMonad/
from pymonad.tools import curry
#anotacion currificada para hacer anotaciones parciales
@curry
def quadc(a, b, c, x):
    return a*x*x + b*x + c

y = quadc(1, -3, 2, 0)
f = quadc(1, -3)
y = f(2, 0)

a = 1
b = 2
c = [1, 2, 3, 4 ,5]
x = [2, 4, 6, 7, 10]
# currificacion con pymonads
m = map(quadc(a, b), c, x)
# aplicación parcial con partial de functools
m = map(partial(quad, a, b), c, x)
# aplicacion parcial con clouser
m = map(quad_ab(a, b), c, x)

# composición
from operator import add, mul

add(2, mul(3, x))

f = partial(add, 2)
g = partial(mul, 3)

f(g(x))

partial(add, 2)(partial(mul, 3)(x))