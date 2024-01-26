#Finalmente, escriba un tercer programa que ordene cuatro números:
n1=int(input("ingrese el primer valor\n"))
n2=int(input("ingrese el segundo valor\n"))
n3=int(input("ingrese el tercer valor\n"))
n4=int(input("ingrese el cuarto valor\n"))

numeros=[n1,n2,n3,n4]
orden=sorted(numeros, reverse=True)
print("los numeros organizados de mayor de menos",orden)