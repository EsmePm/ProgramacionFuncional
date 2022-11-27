import utils

def run():
    t = (
        ('Jairo', [4.5, 3.2, 6.1], 21, 'H'),
        ('Yaneth', [5.4, 2.3, 1.6], 19, 'M'),
        ('Carlos', [8.5, 8.2, 8.1], 23, 'H'),
        ('Anabel', [9.5, 9.2, 8.1], 17, 'M'),
        ('Roberto', [7.5, 7.2, 7.1], 16, 'H'),
        ('Angel', [6.5, 6.2, 6.1], 22, 'H'),
        ('Denisse', [9.5, 8.2, 7.1], 15, 'M'),
        ('Octavio', [4.5, 5.2, 6.1], 18, 'H'),
        ('Maria', [4.5, 6.2, 8.1], 20, 'M'),
        ('Mario', [9.5, 3.2, 6.1], 24, 'H'),
    )

    print("Todos\n", t)
    print("Nombre ascendente\n",utils.nameAsc(t))
    print("Nombre descendente\n",utils.nameDesc(t))
    print("Promedio\n",utils.prom(t))
    print("Edad ascendente\n",utils.ageAsc(t))
    print("Edad descendemte\n",utils.ageDesc(t))

if __name__ == '__main__':
    run()