import time

def ToH(n , A, B, C):
    if n==1:
        print("Disco", n, "de '", A, "' hacia '", B, "'")
        return 
    ToH(n-1, A, C, B)
    print("Disco", n, "de '", A, "' hacia '", B, "'")
    ToH(n-1, C, B, A)


if __name__ == '__main__':
    start = time.time()
    n = int(input("Ingrese un número de discos: "))
    ToH(n,'A','B','C')
    end = time.time()
    print("tiempo: ", end - start)