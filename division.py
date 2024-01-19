#ejercicio 3
#Escriba un programa que pida dos números enteros y que calcule la división,
# indicando si la división es exacta o no.

dividendo=int(input("ingrese el valor del dividendo\n"))
divisor=int(input("ingrese el valor del divisor\n"))
cociente=dividendo//divisor
resto=dividendo%divisor
print("la division entre el valor ",dividendo," y el valor",divisor)
if resto==0:
   print("la division es exacta ")
   print("cociente = ",cociente)
   print("resto = ",resto)
else:
   print("la division no es exacta")
   print("cociente = ",cociente)
   print("resto = ",resto)