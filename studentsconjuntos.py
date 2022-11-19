import random
from statistics import mean
def fun():
    x = random.randint(1, 100)
    d = set()
    t = set()
    students = (
        ('Jairo', [4.5, 3.2, 6.1], 21, 'H'),
        ('Yaneth', [5.4, 2.3, 1.6], 19, 'M'),
        ('Carlos', [8.5, 8.2, 8.1], 23, 'H'),
        ('Anabel', [9.5, 9.2, 8.1], 17, 'M'),
        ('Roberto', [7.5, 7.2, 7.1], 16, 'H'),
    )
    #aleatorios = [random.randint(1,10) for i in range (1,11)]
    #print(aleatorios)
    l = {i[0] for i in students}
    t.add(tuple([(i[0], i[2]) for i in students if  i[2] >= 18]))
    d.add(tuple([(i[0], i[3]) for i in students if  i[2] < 18 and i[3]=='M']))
    p = {i[0] for i in students if mean(i[1])>=6.0}
    # = {(name, random.randint(1,10)) for name in students}
    #print(l)
    #print(t)
    #print(d)
    print(p)

if __name__ == '__main__':
    fun()