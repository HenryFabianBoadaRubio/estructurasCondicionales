#ejercicio 4
#Escriba un programa que pida al usuario dos palabras,
# y que indique cuál de ellas es la más larga y por cuántas letras lo es.

palabra1=input(" ingrese la primera palabra\n")
palabra2=input(" ingrese la segunda palabra\n")

if len(palabra1)>len(palabra2):
   print(f"la palabra 1: {palabra1} es mas larga que la palabra : {palabra2}")
   resta= len(palabra1)-(len(palabra2))
   print("la diferencia en caracteres entre las dos palabras es =",resta)
else:
    print(f"la palabra 2: {palabra2} es mas larga que la palabra : {palabra1}")
    resta= len(palabra2)-(len(palabra1))
    print("la diferencia en caracteres entre las dos palabras es =",resta)
