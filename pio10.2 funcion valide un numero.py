def mensaje():
    print("Bienvenido Ramon")
def mensaje2(nombre):
    print("Bienvenido",nombre)
def mensajes3(nombre):
    cadena= "Bienvenido " + nombre
    return cadena
def lenN(cadena):
    cont=0
    for caract in cadena:
        cont+=1
    return  cont

def validar_numero(cadena):
    while not cadena.isdigit():
        cadena=input("Error , Ingrese un numero: ")
    return  int(cadena)


def validar_numero(cadena):
    while not cadena.isdigit():
        cadena=input("Error, Ingrese un numero: ")
        return int(cadena)
cadena=input("Ingrese un numero: ")
numero=validar_numero(cadena)
print(numero)