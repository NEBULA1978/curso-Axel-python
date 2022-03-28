"""
La empresa SoftChicken cuenta con informacion de sus productos
repartidos en dos listas

productos=["monitor","mouse","teclado","microfono","camara"...]
precios=[200,15,25,5,40...]

La primera lista contiene los nombres de los productos,
la segunda lista contiene los precios de esos productos.
Ejemplo:el producto Monitor cuesta 200€,un mouse15€,etc.
La empresa requiere la siguiente informacion:
A)El nombre del producto con menor precio
B)El precio de un mouse
C)Presentar un top5 de productos en orden de mayor a menor segun su precio
ejemplo:

Producto Precio
monitor 200
camara 40
teclado 25
mouse 15
microfono 5
"""
#LISTAS PARALELAs:

productos=["monitor","mouse","teclado","microfono","camara","audifonos"]
precios=[200,15,25,5,40,80]
#A)El nombre del producto con menor precio
minimo=min(precios)#5
pos=precios.index(minimo)# 3
product=productos[pos]
print(product)

#B)El precio de un mouse
posPro=productos.index("mouse")
precio=precios[posPro]
print(precio)
#Si conozco la posicion puedo conocer el elementocon indexacion
#Si conozco el elemento puedo conocer la posicion con la funcion index

#C)Presentar un top5 de productos en orden de mayor a menor segun su precio
i=0
print("{:<15} {:<15}".format("Precio","Producto"))
while i<5:
    maxi=max(precios)
    posMax=precios.index(maxi)
    nombre=productos[posMax]
    print("{:<15} {:<15}".format("nombre","maxi"))
    del productos[posMax]
    del precios[posMax]
    i+=1

