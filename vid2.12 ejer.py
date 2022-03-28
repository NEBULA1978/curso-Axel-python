"""
Escriba un programa que pèrmita al usuario ingresar el rado(cm) y
la altura(cm) de un termo con forma cilindrica,su
programa debera calcular el volumen del termo y mostrar True si
el usuario puede llenar el termo con 300ml de agua,
False caso contrario

"""

radio = float(input("Ingresa el radio del termo: "))
altura = float(input("Ingresa la altura del termo: "))
pi=3.14
volumen=pi*(radio**2)*altura
print("El volumen del termo es:",volumen,"cm")
cond=volumen>=300
print("¿Se puede llenar el termo con 300ml de agua?:",cond)
