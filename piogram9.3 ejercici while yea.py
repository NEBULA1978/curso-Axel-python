"""
ejer2
Escribir un programa que permitael ingreso de n numeros.
Primero debe preguntar al usuario cuantos numero desea ingresar.
al final del programa presente la sumatoria de dichos numeros.
"""
acum=0
cuantos=int(input("¿Cuantos numero va a ingresar? "))
ciclo=0
while ciclo< cuantos:
    num=int(input("Ingrese un numero: "))
    acum+= num
    ciclo+=1
print("Total:",acum)
