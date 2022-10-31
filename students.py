from statistics import mean

def run(): 
    students = (
        ('Jairo', [4.5, 3.2, 6.1], 21, 'H'),
        ('Yaneth', [5.4, 2.3, 1.6], 19, 'M'),
        ('Carlos', [8.5, 8.2, 8.1], 23, 'H'),
        ('Anabel', [9.5, 9.2, 8.1], 17, 'M'),
        ('Roberto', [7.5, 7.2, 7.1], 16, 'H'),
    )

    #solution = {i[0]: i for i in students if i[2] >= 18}   #mayor de 18
    #solution = {i[0]: i for i in students if i[2] <= 18  if i[3] =='M'}    #menor a 18 y que sea m
    solution = {i[0]: {'cal': i[1], 'edad':i[2], 'sexo' : i[3]} for i in students}

    print(solution)

if __name__ == '__main__':
    run()