"""
from random import *
n = randint(1,6)
n1= randrange(5)
print(n1)
print(n)
"""
from random import *
"""
estudiantes=["Axel","Gabi","Mel","Bryan","Karla"]
indice=randrange(len(estudiantes))
estudiante=estudiantes[indice]
print(indice,estudiante)
"""
"""
estudiantes=["Axel","Gabi","Mel","Bryan","Karla"]
indice=randint(0,len(estudiantes)-1)
estudiante=estudiantes[indice]
print(indice,estudiante)
"""
#tercer metodo
estudiantes=["Axel","Gabi","Mel","Bryan","Karla"]
elemento = choice(estudiantes)
print(elemento)

#metod sample
estudiantese=["Axel","Gabi","Mel","Bryan","Karla"]
lista = sample(estudiantese,2)
print(lista)
#stream aleatorio
nombre = "Axel"
lista = sample(nombre,3)
print(lista)

#suffle mezcla el orden aleatorio de los elementos de una lista
naipes = ["A","2","3","4","5","6","7","8","9","j","Q","K"]
shuffle(naipes)
print(naipes)

n1=random()
print(n1)

n3=uniform(1,10)
print(n3)

n=randrange(0,50,10)
print(n)