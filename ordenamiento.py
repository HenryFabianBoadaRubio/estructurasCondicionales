#ejercicio 5 
#Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a mayor:
n1=int(input("ingrese el primer valor\n"))
n2=int(input("ingrese el segundo valor\n"))
if n1>n2:
    print("los numeros ingresados de mayor a menor serian =",n1,n2)
else:
    print("los numeros ingresados de mayor a menor serian =",n2,n1)
    
#_________________________________________    
     #A continuación, escriba otro programa que haga lo mismo con tres números
n1=int(input("ingrese el primer valor\n"))
n2=int(input("ingrese el segundo valor\n"))
n3=int(input("ingrese el tercer valor\n"))

numeros=[n1,n2,n3]
orden=sorted(numeros, reverse=True)
print("los numeros organizados de mayor de menos",orden)

#________________________________

#Finalmente, escriba un tercer programa que ordene cuatro números:
n1=int(input("ingrese el primer valor\n"))
n2=int(input("ingrese el segundo valor\n"))
n3=int(input("ingrese el tercer valor\n"))
n4=int(input("ingrese el cuarto valor\n"))

numeros=[n1,n2,n3,n4]
orden=sorted(numeros, reverse=True)
print("los numeros organizados de mayor de menos",orden)