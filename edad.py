#ejercicio 8 
#Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:

from time import localtime
dia=int(input("Dia = "))
mes=int(input("mes = "))
año=int(input("año = "))
ahora=localtime()

if ahora.tm_mon>=mes and ahora.tm_mday>=dia:
    años=ahora.tm_year-año
    print(f" en este momento tienes {años} años")
else:
    años=ahora.tm_year-año-1
    print(f"en este momento tienes {años} años")