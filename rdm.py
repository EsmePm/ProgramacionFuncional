import random

def fun():
    x = random.randint(1, 100)
    students = ['Ana', 'Roberto', 'Enrique', 'Maria']
    #aleatorios = [random.randint(1,10) for i in range (1,11)]
    #print(aleatorios)
    l = [(name, random.randint(1,10)) for name in students]
    t = tuple([(name, random.randint(1,10)) for name in students])
    d = { name: random.randint(1,10) for name in students }
    c = {(name, random.randint(1,10)) for name in students}
    print(l)
    print(t)
    print(d)
    print(c)

if __name__ == '__main__':
    fun()