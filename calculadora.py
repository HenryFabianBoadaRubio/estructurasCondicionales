#ejercicio 7
#Escriba un programa que simule una calculadora básica, este puede realizar operación de suma,
#resta, multiplicación y división.
#El programa debe recibir como entrada 2 números reales y un operador, que puede ser +, -, * o /.
#La salida del programa debe ser el resultado de la operación.

n1=int(input("ingrese el primero valor\n"))
n2=int(input("ingrese el segundo valor\n"))
caracter=(input("ingrese el simbolo de la operacion que desea realizar (+ , - , * , /)\n"))

suma="+"
resta="-"
dividir="/"
multipli="*"

if (caracter==suma) :
    suma1=n1+n2
    print("el resultado de la suma es = ",suma1)
elif (caracter==resta):
    resta1=n1-n2
    print("el resultado de la resta es = ",resta1)
elif(caracter==dividir):
    dividir1=n1/n2
    print("el resultado de la division es = ",dividir1)
else:
    multipli1=n1*n2
    print("el resultado de la multiplicacion es = ",multipli1)