Algoritmo division
	Definir dividendo,divisor Como Entero
	Definir cociente, resto Como Real
	Escribir "ingrese el valor del dividendo"
	Leer dividendo
	Escribir "ingrese el valor del divisor"
	leer divisor
	
	cociente=dividendo/divisor
	resto=dividendo%divisor
	
	Escribir "el resultado entre el valor = ",dividendo," y el valor ",divisor
	si resto==0 Entonces
		Escribir "la division es exacta"
		Escribir "cociente= ",cociente
		Escribir "restoo= ",resto
	SiNo
		
		Escribir "la division no es exacta"
		Escribir "cociente= ",cociente
		Escribir "restoo= ",resto
	FinSi
		
FinAlgoritmo
