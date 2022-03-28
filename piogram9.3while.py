"""
ejercicio1 VALIDACION
Escribier un programa que permita el ingreso de un numero,
si el usuario no ingresa un numero entonces
vuelva a pedir hasta que ingrese correctamente.
"""
num=input("Ingrese un numero: ")
while not num.isdigit():
    print("Por favor ingrese correctamente")
    num=input("Ingrese un numero: ")
print("Programa Terminado")
