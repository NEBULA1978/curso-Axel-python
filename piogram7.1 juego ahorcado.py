"""
cree un programa que simule el juego del ahorcado
su programa debe seleccionar una palabra aleatoria
de una lista de palabras,
ejemplo si la palabra es "POLLOS" entonces muestra
una pista "P___ _S"
el usuario debe ingresar una palabra y si es igual
a la palabra aleatoria
entonces el programa mostrara True,caso contrario
False
"""
import random as rd
palabras=["Capuchino","Cafe","Oreo","Pollos","programacion"]

#num=len(palabras)asi o como abajo 3 lineas
#indice=rd.randint(0,num-1)
indice=rd.randint(0,len(palabras)-1)
pal=palabras[indice]
palMayus=pal.upper()
letraPri=palMayus[0]
letraUlt=palMayus[-1]
n=len(palMayus)-2
subGuio=n * " _ "
pista= letraPri + subGuio +letraUlt
print(pista)
palUser=input("Adivine la palabra: ").upper()
cond= palUser == palMayus
print("¿Gano?: ",cond)