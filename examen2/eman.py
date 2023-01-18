import csv

def ejercicio2(s:str) -> tuple:
    with open(s) as csvfile:
        lis = []
        equipos = csv.reader(csvfile, delimiter = ',')
        columnas = next(equipos)
        for equipo in equipos:
            iterador = zip(columnas,equipo)
            lis.append(tuple(valor for clave, valor in iterador))
        return tuple(lis)

def ejercicio3(t):
    l = []
    for i in t:
        if i[5] == 'H':
            l.append(tuple(i))
    return tuple(l)

def ejercicio4(r):
    li = []
    for i in r:
        b = False
        for l in li:
            if l['HomeTeam'] == i[1]:
                l['Total FTHG'] += int(i[3])
                l['Total FTGA'] += int(i[4])
                b = True
        if b == False:
            li.append({'HomeTeam':i[2],'Total FTHG':int(i[3]),'Total FTGA':int(i[4])})
    print(li)

t = (ejercicio2('./soccer_df2.csv'))
#print("ejercicio 2\n",t)

r = (ejercicio3(t))
#print("Ejercicio 3\n",r)

s = (ejercicio4(r))