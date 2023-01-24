def genera2(it, n):
    for x in it:
        yield [tuple(x[i:i+n]) for i in range(len(x)-(n-1))]

def leerTxt(s):
    with  open(s,"r") as file:
        texto = []
        for line in file:
            texto.append(line.strip('\n').split(','))
    return texto
    
def busca(it, s):
    for a in it:
        s2 = 0
        cadena =','.join(a)
        for i in s:
            cadena2 = ','.join(i)
            s2 += cadena2.count(cadena)   
        print(cadena,s2)   
        

if __name__ == "__main__":
    s = leerTxt('prueba.txt')
    print(s,'\n')
    conta = 0
    for i in genera2(s, 2):
        #print(i, '\n') 
        busca(i,s)