Algoritmo ordenamiento2
	Definir n1, n2, n3 Como Entero
    Escribir "Ingrese el primer numero: "
    Leer n1
    Escribir "Ingrese el segundo numero: "
    Leer n2
    Escribir "Ingrese el tercer numero: "
    Leer n3
    Si n1>n2 
        temp <- n1
        n1 <- n2
        n2 <- temp
    FinSi
    Si n2>n3
        temp <- n1
        n2 <- n3
        n3 <- temp
    FinSi
    Si n1>n2
        temp <- n1
        n1 <- n2
        n2 <- temp
    FinSi
    Escribir n1 " " n2 " " n3 
	
	

FinAlgoritmo
