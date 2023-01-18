from typing import List
from Funciones import * 
# Palabras que el juego utiliza al asar.
palabras = 'amistad moneda comida juego python web silla telefono dinero balon futbol curso lapiz libro audifono estrella periodico mochila agua fruta computadora monitor señal mirada'.split()

# Funcion principal de juego
if __name__ == '__main__':
    print ('A H O R C A D O')
    letraIncorrecta : List[str] = []   #annotations
    letraCorrecta : List[str] = []  
    palabraSecreta = buscarPalabraAleatoria(palabras[:])
    finJuego = False
    while True:
        principal(AHORCADO[:], letraIncorrecta[:], letraCorrecta[:], palabraSecreta)
        # El usuario elije una letra.
        letra = elijeLetra(letraIncorrecta[:], letraCorrecta[:])
        if letra in palabraSecreta:
            letraCorrecta.append(letra)
            # Se fija si el jugador ganó
            letrasEncontradas = True
            for i in range(len(palabraSecreta)):
                if palabraSecreta[i] not in letraCorrecta:
                    letrasEncontradas = False
                    break
            if letrasEncontradas:
                print ('\n¡Felicidades! \nLa palabra secreta es "' + palabraSecreta + '"! \n¡Has ganado!')
                letraCorrecta.clear()
                letraIncorrecta.clear()
                finJuego = True
        else:
            letraIncorrecta.append(letra)
            # Comprueba la cantidad de letras que ha ingresado el jugador y si perdió
            if len(letraIncorrecta) == len(AHORCADO) - 1:
                principal(AHORCADO[:], letraIncorrecta[:], letraCorrecta[:], palabraSecreta)
                print ('¡Se ha quedado sin letras!\nDespues de ' + str(len(letraIncorrecta)) + ' letras erroneas y ' + str(len(letraCorrecta)) + ' letras correctas. \nLa palabra era "' + palabraSecreta + '"')
                letraCorrecta.clear()
                letraIncorrecta.clear()
                finJuego = True
        if finJuego:
            if empezar():
                letraIncorrecta.clear()
                letraCorrecta.clear() 
                finJuego = False
                palabraSecreta = buscarPalabraAleatoria(palabras[:])
            else:
                break