import math
#len 
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