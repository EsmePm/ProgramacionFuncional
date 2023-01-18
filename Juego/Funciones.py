import random
from typing import List, Tuple
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
# Funcion primordial del juego
def principal(AHORCADO: List[str], letraIncorrecta: List[str], letraCorrecta: List[str], palabraSecreta: str):
    print(AHORCADO[len(letraIncorrecta)]) # Imprime el dibujo dependiendo de los errores
    print ("")
    fin = " "
    print ('Letras incorrectas:', fin)
    #Imprime las letras incorrectas
    for letra in letraIncorrecta:
        print (letra, fin)
    print ("")
    espacio = '_' * len(palabraSecreta)
    for i in range(len(palabraSecreta)): # Remplaza los espacios en blanco por la letra bien escrita
        if palabraSecreta[i] in letraCorrecta:
            espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:] #Slices
    for letra in espacio: # Mostrará la palabra secreta con espacios entre letras
        print (letra, fin)
    print ("")

# Funcion que devuelve True si el jugador quiere volver a jugar, de lo contrario devuelve False
def empezar():
    print ('Quieres jugar de nuevo? (Si o No)')
    return input().lower().startswith('s')

# Funcion que retorna una palabra aleatoria.
def buscarPalabraAleatoria(listaPalabras: List[str])-> str:
    return listaPalabras[random.randint(0, len(listaPalabras) - 1)]

# Funcion que devuelve la letra que el jugador ingreso. 
# Esta funcion hace que el jugador ingrese una letra y no cualquier otra cosa
def elijeLetra(correcto: List[str], incorrecto: List[str])-> str:
    while True:
        print ('Adivina una letra:')
        letra = input()
        letra = letra.lower() # Devuelve la letra en minuscula
        if len(letra) != 1:
            print ('Introduce una sola letra.') 
        elif letra in correcto or letra in incorrecto:
            print ('\nYa has elegido esa letra, prueba con otra letra.')
        elif letra not in 'abcdefghijklmnñopqrstuvwxyz':
            print ('Elije una letra.')
        else:
            return letra

 