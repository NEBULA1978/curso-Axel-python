
"""
imprimir solo las vocales abiertas
vocales abiertas : a,e,o
vocalescerradas: i,u

"""

cadena=input("Ingrese palñabra: ").lower()#Arco
for caracter in cadena:
    if caracter in "aeo":
       print(caracter)