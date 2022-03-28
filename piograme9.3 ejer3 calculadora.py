"""
Pedir al usuario que opcion desea usar
 sea 1 para duma ,dos para resta o 3 para salir del programa.
si el usuario ingresa 1 o 2,pida dos numeros y realice
la operacion.El programa debvera seguir mostrando el menu
hasta que el usuario coloque la opcion 3 de salir

"""
opcion=""
while opcion!="3":
    print("Bienvenido a tu calculadora")
    print("1.Suma")
    print("2.Resta")
    print("3.Salir")
    opcion=input("Ingrese una opcion: ")
    if(opcion=="1"):
        n1=int(input("Ingrese numero 1: "))
        n2 = int(input("Ingrese numero 2: "))
        total=n1+n2
        print("La suma de los dos numeros es:",total)
    elif (opcion=="2"):
        n1 = int(input("Ingrese numero 1: "))
        n2 = int(input("Ingrese numero 2: "))
        total = n1 - n2
        print("La resta de los dos numeros es:",total)
    elif (opcion==3):
        print("Gracias por usar tu calculadora")
    else:
        print("Ingrese una opcion correcta")