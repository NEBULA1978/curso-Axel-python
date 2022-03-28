"""
esciba un programa que pregunte cuantos
numeros se van a introducir ,permita el
ingreso de dichos numero y muestre
por pantalla cuantos numeros son
 pares y la suma de los impares

"""
veces=int(input("¿Cuantos numeros deseas ingresar?"))
cont=0
acum=0
for i in range (veces):
    print("---Ciclo "+str(i+1)+"---")
    num=int(input("ingrese un numero: "))
    if num%2==0:
        cont+=1
    else:
        acum+=num
print("La cantidad de numeros pares es:", cont)
print(("La suma total de numeros impares es:",acum))