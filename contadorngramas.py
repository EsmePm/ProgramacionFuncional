#### Programa que obtiene los conjuntos de n-gramas frecuentes de cadenas de texto a partir de un archivo de entrada.


import nltk

def generador(entrada, grama):
    if len(entrada) >= grama:
        yield [tuple(entrada[i:i+grama]) for i in range(len(entrada)-(grama-1))]
            
def leerTxt(entrada):
    with open(entrada,"r") as file:
        texto = []
        for line in file:
            lista = line.strip('\n').split('=')
            if lista[1] != '':
                texto += lista[1].split(',')
    return texto

def escribirTxt(salida,lista):
    f = open(salida,"w")
    f.write('['+str(lista[0][0])+'] '+lista[0][1])
    for x in lista[1:]:
        f.write('\n'+'['+str(x[0])+'] '+x[1])
    f.close

if __name__ == "__main__":
    entrada = leerTxt(input("Ingrese el nombre el archivo de entrada: "))
    umbral = int(input("Ingrese el umbral de frecuencia: "))
    grama = int(input('Ingrese el tamaño del n-grama: '))
    salida = input("Ingrese el nombre el archivo de salida: ")

    lista2 = []
    for i in generador(entrada, grama):
        lista2 += i

    freq = nltk.FreqDist(lista2)
    
    lista = []
    for cadena, contador in freq.items():
        if contador >= umbral:
            lista.append((contador,','.join(cadena)))

    lista = sorted(lista, key = lambda x : x[0], reverse = True)
    escribirTxt(salida, lista)
    