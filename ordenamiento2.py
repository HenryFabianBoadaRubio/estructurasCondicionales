#A continuación, escriba otro programa que haga lo mismo con tres números
n1=int(input("ingrese el primer valor\n"))
n2=int(input("ingrese el segundo valor\n"))
n3=int(input("ingrese el tercer valor\n"))

numeros=[n1,n2,n3]
orden=sorted(numeros, reverse=True)
print("los numeros organizados de mayor de menos",orden)