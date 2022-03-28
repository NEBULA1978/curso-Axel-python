"""
escriba un programa que permita al usuario ingresar las medidas
 del cateto a y b de un triangulo rectangulo,supprograma debera
 calcular la hipotenusa c del triangulo a partir de la formula
 del teorema de pitagoras.
 mostrar el ¡resultado con tres decimales

 ejemplo de salida del progrma:
 Ingrese medida del cateto a(en cm): 15.7
 Ingrese medida del cateto b(en cm): 17.7
 La medida de la hipotenusa es: 23.595
"""

num1=float(input("Ingrese Cateto a: "))
num2=float(input("Ingrese Cateto b: "))
hipote=( (num1**2)+(num2**2))**(1/2)
print("La medida de la Hipotenusa es: {:.3f}".format(hipote))


