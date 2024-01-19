#ejercicio 11
#El riesgo de que una persona sufra enfermedades coronarias depende de su edad y su índice de masa corporal:

# 	edad < 45	edad ≥ 45
#IMC < 22.0	bajo	medio
#IMC ≥ 22.0	medio	alto
#El índice de masa corporal es el cuociente entre el peso del individuo en kilos
#y el cuadrado de su estatura en metros.

#Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona,
#y le entregue su condición de riesgo.
import math
PESO= float(input("Ingrese su peso= \n"))
ALTURA= float(input("Ingrese su altura= \n"))
EDAD = int(input("Ingrese su edad= \n"))
IMC=(PESO/(ALTURA**2))
if EDAD < 45 and IMC < 22.0:
    print("El riesgo de que sufra enfermedades es Bajo")
elif EDAD >= 45 and IMC < 22.0:
    print("El riesgo de que sufra enfermedades es Medio")
elif EDAD < 45 and IMC >= 22.0:
    print("El riesgo de que sufra enfermedades es Medio")
else:
    print("El riesgo de que sufra enfermedades es Alto")