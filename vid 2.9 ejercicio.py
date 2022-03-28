# escribir un programa que permita el ingreso de dos numeros y muestre por pantalla
# True si es el primer numero es divisible para el segundo, False caso contrario
"""
ejemplo de salida del programa:
ingrese numero 1: 10
ingrese numero2: 5
¿10 es divisible entre 5? True

"""

num1=int(input("Ingrese numero1: "))
num2=int(input("Ingrese numero2: "))
residuo=num1%num2
condicion= residuo == 0
print("¿",num1, "es divisible entre",num2,"?",condicion)

