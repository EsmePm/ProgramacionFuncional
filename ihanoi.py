
import sys

# Estrutura para representar una pila
class Stack:
    # Constructor para establecer los datos de
    # nodo de árbol recién creado
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.array = [0]*capacity
 
# función para crear una pila de capacidad determinada.
def createStack(capacity):
    stack = Stack(capacity)
    return stack
  
# La pila está llena cuando top es igual al último índice.
def isFull(stack):
    return (stack.top == (stack.capacity - 1))
   
# La pila está vacía cuando top es igual a -1.
def isEmpty(stack):
    return (stack.top == -1)
   
# Función para añadir un elemento a la pila.
# Aumenta top en 1
def push(stack, item):
    if(isFull(stack)):
        return
    stack.top+=1
    stack.array[stack.top] = item
   
# Función para eliminar un elemento de la pila.
# Decrementa top en 1
def Pop(stack):
    if(isEmpty(stack)):
        return -sys.maxsize
    Top = stack.top
    stack.top-=1
    return stack.array[Top]
   
# Movimiento entre dos barras
def moveDisksBetweenTwoPoles(src, dest, s, d):
    pole1TopDisk = Pop(src)
    pole2TopDisk = Pop(dest)
 
    # Si barra 1 está vacía
    if (pole1TopDisk == -sys.maxsize):
        push(src, pole2TopDisk)
        moveDisk(d, s, pole2TopDisk)
       
    # Si barra 2 está vacía
    elif (pole2TopDisk == -sys.maxsize):
        push(dest, pole1TopDisk)
        moveDisk(s, d, pole1TopDisk)
       
    # Si el disco superior de la barra 1 > el disco superior de la barra 2
    elif (pole1TopDisk > pole2TopDisk):
        push(src, pole1TopDisk)
        push(src, pole2TopDisk)
        moveDisk(d, s, pole2TopDisk)
       
    # Si el disco superior de la barra 1 < el disco superior de la barra 2
    else:
        push(dest, pole2TopDisk)
        push(dest, pole1TopDisk)
        moveDisk(s, d, pole1TopDisk)
   
# Función para mostrar el moviemiento de los discos
def moveDisk(fromPeg, toPeg, disk):
    print("Move the disk", disk, "from '", fromPeg, "' to '", toPeg, "'")
    
   
# Función para el rompecabezas de torres de hanoi
def tohIterative(num_of_disks, src, aux, dest):
    s, d, a = 'S', 'D', 'A'
   
    # Si el número de discos es par, entonces intercambia 
    # polo de destino y polo auxiliar
    if (num_of_disks % 2 == 0):
        temp = d
        d = a
        a = temp
    total_num_of_moves = int(pow(2, num_of_disks) - 1)
   
    # Los discos más grandes serán empujados primero
    for i in range(num_of_disks, 0, -1):
        push(src, i)
   
    for i in range(1, total_num_of_moves + 1):
        if (i % 3 == 1):
            moveDisksBetweenTwoPoles(src, dest, s, d)
   
        elif (i % 3 == 2):
            moveDisksBetweenTwoPoles(src, aux, s, a)
   
        elif (i % 3 == 0):
            moveDisksBetweenTwoPoles(aux, dest, a, d)


if __name__ == '__main__':
    # Número de discos
    num_of_disks = 3
    
    # Crear 3 pilas de tamño num_of_disks
    src = createStack(num_of_disks)
    dest = createStack(num_of_disks)
    aux = createStack(num_of_disks)
    
    tohIterative(num_of_disks, src, aux, dest)