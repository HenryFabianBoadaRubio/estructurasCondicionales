#ejercicio 9 
#El joven periodista Solarrabietas debe relatar un partido de tenis,
#pero no conoce las reglas del deporte. En particular, no ha logrado aprender cómo saber si un set ya terminó, y quién lo ganó.

#Un partido de tenis se divide en sets. Para ganar un set, un jugador debe ganar 6 juegos,
#pero además debe haber ganado por lo menos dos juegos más que su rival. 
#Si el set está empatado a 5 juegos, el ganador es el primero que llegue a 7.
# Si el set está empatado a 6 juegos, el set se define en un último juego, en cuyo caso el resultado final es 7-6.
#Sabiendo que el jugador A ha ganado m juegos, y el jugador B, n juegos, al periodista le gustaría saber:

#si A ganó el set, o
#si B ganó el set, o
#si el set todavía no termina, o
#si el resultado es inválido (por ejemplo, 8-6 o 7-3).
#Desarrolle un programa que solucione el problema de Solarrabietas:

A = int(input("Ingrese puntaje de A:\n"))
B = int(input("Ingrese puntaje de B:\n"))

if (A == 4 and B == 5):
    print("Aun no termina")
elif (B >= 4 and B == 7):
    print("Gana B")
elif (A == 5 and B == 6):
    print("Aun no termina")
elif (A == 3 and B == 7):
    print("Invalido")
elif (A <= 6 and B <= 4):
    print("Gana A")