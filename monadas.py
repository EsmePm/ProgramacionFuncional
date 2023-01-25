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

l = List[1, 2, 3]
print(l)
print(type(l))

#probar a partir de aca en python 3.9

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

c = b * Just(6)
print(c)

def quad(a, b, c, x):
    return a*x*x + b*x +c

a = quad % Just(1) * Just(3) * Just(2) *Just(0)
print(a)

#monadas definen que se retorna de la función y functors 

def oneover(x):
    try:
        ret = 1/x
    except:
        return Nothing()
    return Just(ret)

a = Just(2).bind(oneover) #bind esta mas pensado a lo que devuelve la función
print(a)

a = Just(0).bind(oneover)
print(a)