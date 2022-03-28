"""
Tipo Valor.
1.Vehiculo € 3.5
2.Camion € 12.00
3.Tractomula € 16.00
El valor a pagar por cada automotor que pase por el peaje
Total recaudado en el peaje en ese dia.
Total recaudado por cada tipo de automotor.
Cual es el tipo de Automotor que mas transita por el peaje

"""

"""
vehiculoCont=0
camioneCont=0
tractomulasCont=0
vehiculoAcum=0
camionesAcum=0
tractomulasAcum=0
"""

automotores=["Vehiculos","Camiones","Tractomulas"]
precios=[3.50,12.0,16.0]
contL=[0,0,0]
acumL=[0,0,0]
ingreso=int(input("Ingrese automotor: "))
while ingreso!=0:
    if (ingreso<=len(automotores)):
        precio=precios[ingreso-1]
        print("Debe pagar: ",precio)
        contL[ingreso-1]+=1
        acumL[ingreso-1]+=precio
        print(automotores)
        print(contL)
        print(acumL)
    else:
        print("Error de ingreso")
    ingreso = int(input("Ingrese automotor: "))
totalDia=sum(acumL)
print("Total reacudado en el dia fue:",totalDia)
print("Total recaudado por cada tipo de automotor")
for i in range(len(automotores)):
    auto=automotores[i]
    acum=acumL[i]
    print(auto,":",acum)
maxi=max(contL)
posMax=contL.index(maxi)
autoMax=automotores[posMax]
print("El automotor que mas paso fue:",autoMax)