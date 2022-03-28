"""
Imprimir por pantalla todas las personas que imprimieron mora y la cantidad

"""

frutas=["Mora","Fresa","Sandia","Piña","Uva"]

cantidad=[ 5, 10 , 3 , 5 , 10 ]

clientes=["Axell","Zarinna","Luis","Joel","Kevin"]
for fruta in frutas:
    pos=frutas.index(fruta)#0
    if fruta=="Mora":
        can=cantidad[pos]
        cli=clientes[pos]
        print(cli,can)