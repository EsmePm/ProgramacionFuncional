# -*- coding: UTF-8 -*-

import random

#auto function: responsable del establecimiento de una secuencia de mazos
def auto():
    pokers=[]
    poker=[]
    for i in ['Heart','Spade','Diamond','Club']:
        for j in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
            poker.append(i)
            poker.append(j)
            pokers.append(poker)
            poker=[]
    return pokers

def poker_game():
    player_name = []
    for i in range(player_number):
        player_name.append("player"+str(i))
        print ('jugador total', player_number, 'nombre', 'respectivamente:', player_name)

    li={}
    for k in player_name:
        b = random.sample (poker, 2) # roba al azar dos cartas
        for s in b:
            poker.remove (s) # Las cartas de juego se sacan del mazo
            li.setdefault (k, b) #Las cartas de juego se distribuyen a los jugadores
            print ('Las cartas robadas por cada jugador son:', li)

    temp2 = 0

    dic = {}
    tt_name = []

    for i in player_name:
        temp = 0
        for each in li[i]:
            if each[1] == 'A':
                temp = temp + 1
            elif each[1] == 'J':
                temp = temp + 11
            elif each[1] == 'Q':
                temp = temp + 12
            elif each[1] == 'K':
                temp = temp + 13
            else:
                temp = temp + int(each[1])
                print ('jugador', i, 'total de puntos extraídos:', temp)
        if temp > temp2:
            temp2 = temp
            dic.setdefault(i, temp)
            tt_name.append(i)
            if temp == temp2: #Los puntos totales del jugador actual son tan grandes como los puntos totales máximos anteriores, registre primero
                dic.setdefault(i, temp)
                tt_name.append(i)

        for i in tt_name: #Borrar los puntos registrados anteriormente que no son los más grandes y sus nombres de jugador
            if dic[i] < temp2:
                del dic[i]
            print ('El nombre del jugador con más puntos y sus puntos son:', dic)

while True:
    try:
        print ("\n —————————————————— Comienza una nueva ronda de juegos —————————————————— \n")
        player_number = input("Ingrese el número de jugadores (ingrese el número 0 para finalizar el juego):")
        if player_number == 0:
            break
        else: # Excluyendo el rey del tamaño, hay 52 cartas, cada jugador reparte dos cartas y un máximo de 26 personas participan en el juego.
            poker = auto()
            print ('Antes de barajar:', poker)

            random.shuffle (poker) # shuffle

            print ('Después de barajar:', poker)
            poker_game()
    except:
        print ("\ n !!! Por favor ingrese un número entero mayor que 0 y menor que 27 !!!")