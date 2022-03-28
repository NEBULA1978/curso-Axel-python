"""
Cree un programa en python que solicite un numero de 3 digitos y un segundo numero de 1 digito
por teclado y muestre por pantalla True  si cumple las siguinetes condiciones,False caso contrario:
 los dos ultimos digitos del primer numero es divisible para el segundo numero
 el cuadrado del segundo numero es menor que los dos ultimos digitos del primer numero

ejemplosde salida del programa:
Ingrese primer numero (3 cifras):260
Ingrese segundo numero(1 cifra): 2
¿Cumplen lasdos condiciones?: True

Ingrese primer numero (3 cifras):200
Ingrese segundo numero(1 cifra): 9
¿Cumplen lasdos condiciones?: False

"""

num1= int(input("Ingrese primer numero: "))
num2= int(input("Ingrese segundo numero: "))
ulti2=num1%100#me da los dos ultimos gigitos del numero dos 00
cond1=ulti2%num2 == 0
cuadrado=num2**2
cond2=cuadrado < ulti2
respueta=cond1 and cond2
print("¿Cumplen las dos condiciones?:",respueta)
