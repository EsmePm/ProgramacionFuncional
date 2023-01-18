import math
from operator import itemgetter
#len solo se aplica en secuencias no en iterables 
l = [1, 2, 3]
print(len(l))

r = range(3, 100, 3)
print(len(r))

m = map(math.sqrt, l) #map es un iterador
#print(len(list(m))) #lo que da len solo se puede ocupar una vez

s = 'hello world'
print(len(s))

#sum
print(sum(l))
print(sum(r))
#print(list(m))
print(sum(map(math.sqrt, l), 10))
#print(sum(m))
#print(sum(s))

a =[[2, 4], [0, 0], [5, 3]]
print(sum(a, []))

l1 = [1, 2, 3]
l2 = [4, 5, 6]
lr = l1 + l2
print(lr)

r = sum(sum(a, []))
print(r)

t1 = (1, 2, 3)
t2 = (4, 5, 6)
tr = t1 + t2
print(sum(tr))

s1 = 'abc'
s2 = 'def'

sr = s1 + s2
print(sr)

s = ['abc', 'def', 'ghi']
sr = ''.join(s)
print(sr)

#min

a = [2, 5, 7, 1]
print(min(a))

m = map(math.sqrt, l)
print(min(m))

b = [[1, 2, 3], [1, 1, 5], [6, 7, 8], [1, 0, 5]]
print(min(b))

c = [1, 2, 3, 4, 5]
print(min(c, default=0)) #default solo lo arroja cuando se considere la excepción

print(min(b, default=0, key= lambda x: x[1]))
print(min(b, default=0, key= itemgetter(1)))

#max

#any
#si al menos uno de los elementos es True retorna un True y False si esta vacío
print(any([1, 0, 2]))
print(any(['a', '', 'b']))
print(any(['', 0, False]))
print(any([]))

#all
#retorna True si todos los elementos son True y si el iterable esta vacío
print(all([1, 0, 2]))
print(all(['a', '', 'b']))
print(all(['', 0, False]))
print(all([]))

import functools, operator
#reduce
#toma los dos primeros elementos y aplica la función, el resultado lo aplica con el siguiente elemento, así sucesivamente
a = [2, 3, 5, 2]
print(functools.reduce(operator.mul, a))
print(functools.reduce(lambda x, y:x*y, a, 10))

b = [2]
print(functools.reduce(lambda x, y:x*y, b, 10))

#practica
#