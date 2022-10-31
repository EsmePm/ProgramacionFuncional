
colors = ['red', 'blue', 'white', 'yellow', 'orange']
print(colors)
fruits = {'apple', 'banana', 'cherry', 'orange', 'pear'}
favorite_fruits = {'apple', 'banana', 'cherry', 'orange', 'pear', 'apple'}
numbers = {1, 5, 7, 9, 3}
things = {"abc", 34, True, 40, "male"}
print(things)

"""
#tamaño de un conjunto
fruits = {'apple', 'banana', 'cherry', 'orange', 'pear'}
print(len(fruits))
"""
"""
#ciclos con conjuntos
fruits = {"apple", "banana", "cherry"}

for fruit in fruits:
  print(fruit)
"""

"""
#Verificar si un elemento esta en el conjunto
fruits = {"apple", "banana", "cherry"}
print('banana' in fruits)
"""

"""
#Agregar un elemento al conjunto
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
"""

"""
#Agregar un conjunto al conjunto
fruits = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

fruits.update(tropical)
print(fruits)
"""

"""
#Agregar cualquier iterable al conjunto
fruits = {"apple", "banana", "cherry"}
tropical = ["kiwi", "orange"]

fruits.update(tropical)
print(fruits)
"""

"""
#Eliminar elementos de un conjunto
fruits = {"apple", "banana", "cherry"}
fruits.remove('banana')
print(fruits)

fruits = {"apple", "banana", "cherry"}
fruits.remove('banana')
print(fruits)
"""

"""
#Eliminar el último elemento
fruits = {"apple", "banana", "cherry"}
new_fruits = fruits.pop()

print(fruits)
print(new_fruits)
"""

"""
#Vaciar el conjunto con clear()
fruits = {"apple", "banana", "cherry"}
fruits.clear()

print(fruits)
"""

"""
#Eliminar el conjunto con del

fruits = {"apple", "banana", "cherry"}
del fruits

print(fruits)
"""

"""
#Unión de dos conjuntos

letters = {"a", "b" , "c"}
numbers = {1, 2, 3}

alophanumerics = letters.union(numbers)
print(alophanumerics)
"""

"""
#Intersección de dos conjuntos con intersection_update()

fruits = {"apple", "banana", "cherry"}
logos = {"google", "microsoft", "apple"}

fruits.intersection_update(logos)

print(fruits)
"""

"""
#Intersección de dos conjuntos con intersection()

fruits = {"apple", "banana", "cherry"}
logos = {"google", "microsoft", "apple"}

my_set = fruits.intersection(logos)

print(my_set)
"""
"""
#Mantener a todos menos a los duplicados con simmetric_difference_update()

fruits = {"apple", "banana", "cherry"}
logos = {"google", "microsoft", "apple"}

fruits.symmetric_difference_update(logos)

print(fruits)
"""
"""
#Mantener a todos menos a los duplicados simmetric_difference()

fruits = {"apple", "banana", "cherry"}
logos = {"google", "microsoft", "apple"}

x = fruits.symmetric_difference(logos)

print(x)
"""