Algoritmo cedad
	Definir diaNacimiento, mesNacimiento, añoNacimiento, diaActual, mesActual, añoActual, edad como Entero
	
    Escribir "Ingrese su fecha de nacimiento:"
    Escribir "Día: "
    Leer diaNacimiento
    Escribir "Mes: "
    Leer mesNacimiento
    Escribir "Año: "
    Leer añoNacimiento
	Escribir "ingrese el dia actual: "
	leer diaActual
	Escribir "ingrese el mesActual: "
	leer mesActual
	
	Escribir " ingrese el año actual: "
	leer añoActual
    edad <- añoActual - añoNacimiento
	
    Si mesNacimiento > mesActual O (mesNacimiento == mesActual Y diaNacimiento > diaActual) Entonces
        edad <- edad - 1
    Fin Si
	
    Escribir "Usted tiene ", edad, " años."
Finalgoritmo