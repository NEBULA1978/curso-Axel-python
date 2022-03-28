#funcion para saber el numero de caracteres de una palablra:

def mensaje():
    print("Bienvenido Axell")

def mensaje2(nombre):#nombre = cad
    print("Bienvenido",nombre)

def mensaje3(nombre):# nombre = nom
    cadena= "Bienvenido " + nombre
    return cadena
def lenN(cadena):
    cont = 0
    for caract in cadena:
        cont += 1
    return cont

producto= "capuchino"
cuantos= lenN(producto)
print(cuantos)
