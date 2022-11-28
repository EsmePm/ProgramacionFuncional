
d = {}
def fibonacci(n : int) -> int:
    #print("Entrada a fibonacci con: ",n)
    if n in d:
        return d[n]
    elif n == 0 or n == 1:
        return n
    else:
        r = fibonacci(n-1) + fibonacci(n-2)
        d[n] = r
        return r

if __name__ == '__main__':
    x = int ( input ("Ingresa un número: "))
    print(fibonacci(x))