"""
cree un programa que permita ingresar un numero,
se debera mostrar True si el numero no esta entre
10 y 100 (sin incluirlos ,intevalo abierto),muestre
False casoo contrario

"""

num=int(input("Ingrese un numero: "))
cond=not(num>10 and num<100)
#not(False and True)
#not(False)
#True
print("El numero no esta entre 10 y 100",cond)
