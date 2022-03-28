"""

votar a el que mejor haya participado ymas le haya gustado a los estudiantes ,
tecla FIN para salir y ver el ganador

"""


pollos=["Angie","Andres","Gabriela","Oscar","Kevin","Gustavo","Annie","Maria"]
contL=[0]*len(pollos)# [0,0,0,0,0,....]

voto=input("Ingrese nombre estudiante a votar 'FIN': ")# Oscar
while voto!="FIN":
    votoMayus=voto.capitalize()
    if votoMayus in pollos:
        pos=pollos.index(votoMayus)
        contL[pos]+=1
    else:
        print("Voto no valido")
    voto=input("Imgrese nombre del estudiante a votar o ingrese 'FIN': ")#Fin
cantEst=sum(contL)
contMax=max(contL)
posCont=contL.index(contMax)
gana=pollos[posCont]
print("El total estudiantes que votaron fue: {}".format(cantEst))
print("Gana: {} con {} votos".format(gana,contMax))


