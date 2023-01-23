# functor
#pip install oslash en env
from oslash import Just, Nothing, List
from operator import neg

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

l = List[1, 2, 3]
print(l)
print(type(l))

ln = neg % l
print(ln)