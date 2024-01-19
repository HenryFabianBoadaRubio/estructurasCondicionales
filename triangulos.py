#ejercicio 10

#Los tres lados a, b y c de un triángulo deben satisfacer la desigualdad triangular:
#cada uno de los lados no puede ser más largo que la suma de los otros dos.

#Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:

#si acaso el triángulo es inválido; y
#si no lo es, qué tipo de triángulo es.

L1=float(input("Ingrese lado 'a' del triangulo: \n"))
L2=float(input("Ingrese lado 'b' del triangulo: \n"))
L3=float(input("Ingrese lado 'c' del triangulo: \n"))
lado1=L1+L2
lado2=L1+L3
lado3=L2+L3
if lado1<L3:
    print("No es un triangulo valido")
elif lado2<L2:
    print("No es un triangulo válido")
elif lado3<L1:
    print("No es un triangulo valido")
else:
    if L1==L2==L3:
        print("Es un triangulo equilatero")
    elif L1==L2 or L2==L3 or L1==L3:
        print("Es un triangulo isósceles")
    else:
        print("Es un triangulo escaleno")