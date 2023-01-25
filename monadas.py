# functor
#pip install oslash en env
from oslash import Just, Nothing, List
from operator import neg, add

a  = Just(3)
print(a)

print(neg(4)) #neg no reconoce just

b = a.map(neg)
print(b)

b = neg % a #significa lo mismo que b = a.map(neg)
print(b)

n = Nothing()
print(n)

nn = neg % n
print(nn)

l = [1, 2, 3]
print(l)
print(type(l))

# ln = neg % l
# print(ln)

#functors aplicativos
a = Just(3)
f = Just(neg)

b = f.apply(a)
# b = a * f

a = Just(2)
b = add % a
print(b)