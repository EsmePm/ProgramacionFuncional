def miles_2_kilo (m):
    return m*1.60

def in_2_cm (m):
    return m*2.54

def ft_2_cm (m):
    return m*30.48

def yd_2_cm (m):
    return m*91.4

def convert (values, f):
    return f(values)
5
def run():
    menu = """
    1.- Millas a kilómetros
    2.- Pulgadas a centímetros
    3.- Pies a centímetros
    4.- Yardas a centímetros
    """
    print (menu)
    opt = int(input('Ingresar opción:'))

    if opt == 1:
        m = int(input('Ingresar millas:'))
        print(f"Millas {m} a kilómetros {convert(m, miles_2_kilo)}")
    
    elif opt == 2:
        m = int(input('Ingresar pulgadas:'))
        print(f"Pulgadas {m} a centímetros {convert(m, in_2_cm)}")

    elif opt == 3:
        m = int(input('Ingresar pies:'))
        print(f"Pies {m} a centímetros {convert(m, ft_2_cm)}")
    
    elif opt == 4:
        m = int(input('Ingresar yardas:'))
        print(f"Yardas {m} a centímetros {convert(m, yd_2_cm)}")
    
    else:
        print('Opción incorrecta')

if __name__ == '__main__':
    run()