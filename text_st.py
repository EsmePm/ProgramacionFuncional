new = "Health experts said it is too early to predict whether demand would match up with the 171 million doses of the new boosters the U.S. ordered for the fall."
new = new.split()
print(new)
lenghts = map(len, new)
avg = sum(lenghts)/len(new)
print(avg)

avg = sum(map(len, new))/len(new)
print(avg)

stop_words = ['of', 'the', 'to']
s = filter(lambda x: x not in stop_words, new)
#s = list(s)
#avg = sum(map(len, s))/len(s)
#print(avg)

def sumcount(it):
    sum = 0
    count = 0
    for x in it:
        sum += len(x)
        count += 1
    return sum, count

total, count = sumcount(s)
avg = total / count

s = filter(lambda x: x not in stop_words, new)
m = map(len, s)
e = enumerate(m, 1)
print(tuple(e))

import functools, operator

s = filter(lambda x: x not in stop_words, new)
m = map(len, s)
functools.reduce(operator.add, m)   #sum(m)

def opssumcount(a, b):
    return (b[0], a[1]+b[1])

s = filter(lambda x: x not in stop_words, new)
m = map(len, s)
count1, total = functools.reduce(opssumcount, enumerate(m, 1))
avg = total / count1
print(avg)