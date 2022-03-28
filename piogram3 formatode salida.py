"""
nombre="Ramon"
edad=42
print("Mi nombre es:")
print(nombre)
print("y tengo: ")
print(edad)
print("años")

"""

"""
nombre="Ramon"
edad=42
print("Mi nombre es:",nombre,"y tengo",edad,"años")
print("Mi nombre es: "+nombre+" y tengo ",str(edad)," años")
print("Hola" + "Mundo")
print("Hola" , "Mundo")
print("Hola" + " " + "Mundo")
print("Hola" + "" + "Mundo")
"""

"""
#multiples valores concadenar

nombre="Ramon"
edad=42
print("Mi nombre es: "+nombre+" y tengo "+str(edad)+" años")

nombre="Axel"
edad=22
texto="Mi nombre es: "+nombre+" y tengo "+str(edad)+" años"
print(texto)

nombre="Ramonet"
edad=42
print("Mi nombre es: {} y tengo {} años".format(nombre,edad))

"""

#Format n decimales
producto="Capuchino"
valor=2.60
iva=0.12
total = valor + (valor*iva)
print("-Producto:",producto,"-Precio final:",total)
print("-Producto:{} -Precio final: {:.2f}".format(producto,total))