

"""
cree un programa que simule el juego del ahorcado
su programa debe seleccionar una palabra aleatoria
de una lista de palabras, luego seleccionar una letra
aleatoria de una lista de palbras,luego selccionar una
letra aleatoria de esa palabra para poeder mostrar una
(pista)
ejemplo
si la palabra selecciona es "ESPOL" yla letra aleaoria es "P"
entonces el programa debaria mostrar al usuario "__P__"
El usuario debe inrgesar una palbra y si es igual a la
palabra aleatoria entonces el programa mostrara True,
caso contrario False.

"""
import random as rd
palabras=["Capuchino","Cafe","Oreo","Pollos","programacion"]
pal=rd.choice(palabras)#"Pollos"
palMayus=pal.upper()#"POLLOS"
indice=rd.randint(0,len(palMayus)-1)#2
letra=palMayus[indice]#"P"
nPri=len(palMayus[:indice])# ""0
nUlt=len(palMayus[indice+1:])# 5
pista= (nPri*" _ ") +letra+ (nUlt*" _ ")#P_____
print(pista)
palUser=input("Adivine la palabra: ").upper()
cond= palUser == palMayus
print("¿Gano?: ",cond)
