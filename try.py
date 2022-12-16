number = [1, 2, 3, 4]

for i in number:
    print(i)

n = iter(number)

try:
    print(next(n))
    print(next(n))
    print(next(n))
    print(next(n))
    print(next(n))
except:
    print("Fin del iterador")

print("Hola")

temperatures =[12.123, 11.3453, 9.9999999, 7.897879]
b = map(round, temperatures)
print(list(b))

print(chr(97))
numb = [97, 93, 45, 64, 65]
c = map(chr, numb)
print("".join(c))

def mult(x,y,z):
    return x*y*z

t = (3, 5, 7)
print(mult(3, 5, 7))
print(mult(*t))

def distance(a,b):
    print(a,b)


a = ((3, 5), (4, 5), (3, 9))
b = ((6, 9), (2, 9), (0, 3))
for i in a,:
    distance(a[i], b[i])