from statistics import mean

def run():
    t = (
        ('Jario', [4.5, 3.2, 6.1], 21, 'H'),
        ('Yaneth', [5.4, 2.3, 1.6], 19, 'M'),
        ('Carlos', [8.5, 8.2, 8.1], 23, 'H'),
        ('Anabel', [9.5, 9.2, 8.1], 17, 'M'),
        ('Roberto', [7.5, 7.2, 7.1], 16, 'H')
    )

    students2 = { i[0]: {'Calificación': i[1], 'Edad': i[2], 'Sexo':i[3]} for i in t}
    print(students2)

if __name__ == '__main__':
    run()