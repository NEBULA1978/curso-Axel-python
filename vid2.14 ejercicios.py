"""
escriba un programa que evalue el siguiente polinomio para un valor de x ingresadop por teclado:

4x** + 3/2 x -5
resultado en pantalla:
Ingrese el valo de x: 2
El resutado es: 14.0
"""

x=int(input("Igrese el valor de x: "))
termino1= 4*(x**2)
termino2= (3/2) * x
y=termino1 + termino2 - 5
print(y)