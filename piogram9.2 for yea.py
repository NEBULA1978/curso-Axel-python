

frutas=["Mora","Fresa","Sandia","Piña","Uva"]

cantidad=[ 5, 10 , 3 , 5 , 10 ]

clientes=["Axell","Zarinna","Luis","Joel","Kevin"]

#Imprimir por pantalla todas las personas que imprimieron mora y la cantidad

for i in range(len(frutas)):
    fruta=frutas[i]
    if fruta=="Mora":
        can=cantidad[i]
        cli=clientes[i]
        print(cli,can)