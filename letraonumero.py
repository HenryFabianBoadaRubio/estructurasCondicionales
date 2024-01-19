#ejercicio 6 
#Escriba un programa que determine si un caracter ingresado es letra, 
#número, o ninguno de los dos. En caso que sea letra, determine si es mayúscula o minúscula.

lectura=input("ingrese el caracter para determinar el tipo\n")
if lectura.isalpha():
        if lectura.isupper():
                print("el caracter ingresado es tipo lectura y esta en MAYUSCULA")
        elif lectura.islower():
                print("el caracter ingresado es tipo lectura y esta en miniscula")
elif lectura.isdigit():
        print("el caracter ingresado es tipo Numerico")
else:
        print("el caracter ingresado no es ni de letras ni numerico")