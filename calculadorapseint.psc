Algoritmo calculadora
	Definir n1,n2 Como Entero
	Definir caracte Como Caracter
	Escribir "escriba el primer valor = "
	Leer n1
	Escribir "escriba el segundo valor = "
	Leer n2
	Escribir "ingrese el simbolo de la operacion que desea realizar (+ , - , * , /)"
	leer caracte
	
	suma="+"
	resta="-"
	division="/"
	multipli="*"
	si caracte==suma Entonces
		suma1=n1+n2
		Escribir "el resultado de la suma es = ",suma1
	FinSi
	si caracte==resta Entonces
		resta1=n1-n2
		Escribir "el resultado de la resta es = ",resta1
	FinSi
	si caracte==division Entonces
		division1=n1/n2
		Escribir "el resultado de la division es = ",division1
	FinSi
	si caracte==multipli Entonces
		multipli1=n1*n2
		Escribir "el resultado de la multiplicacion es = ",multipli1
	FinSi
	
	
	
	
FinAlgoritmo
