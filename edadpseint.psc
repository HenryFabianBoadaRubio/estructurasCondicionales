Algoritmo cedad
	Definir diaNacimiento, mesNacimiento, a�oNacimiento, diaActual, mesActual, a�oActual, edad como Entero
	
    Escribir "Ingrese su fecha de nacimiento:"
    Escribir "D�a: "
    Leer diaNacimiento
    Escribir "Mes: "
    Leer mesNacimiento
    Escribir "A�o: "
    Leer a�oNacimiento
	Escribir "ingrese el dia actual: "
	leer diaActual
	Escribir "ingrese el mesActual: "
	leer mesActual
	
	Escribir " ingrese el a�o actual: "
	leer a�oActual
    edad <- a�oActual - a�oNacimiento
	
    Si mesNacimiento > mesActual O (mesNacimiento == mesActual Y diaNacimiento > diaActual) Entonces
        edad <- edad - 1
    Fin Si
	
    Escribir "Usted tiene ", edad, " a�os."
Finalgoritmo