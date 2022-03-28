def mensaje():
    print("Bienvenido Axell")

def mensaje2(nombre):#nombre = cad
    print("Bienvenido",nombre)

def mensaje3(nombre):# nombre = nom
    cadena= "Bienvenido " + nombre
    return cadena
nom=input("Ingrese su nobre:")#Axell
cadenaRetorno=mensaje3(nom)#cadenaRetorno = cadena
print(cadenaRetorno)
