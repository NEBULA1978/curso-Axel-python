frutas=["Mora","Fresa","Sandia","Piña","Uva"]

preciox1b=[0.50,1.00,1.55,1.20,2.00]
print("Lista de frutas con precio menor a 1.50")
for i in range(len(frutas)):#0-4
    fruta=frutas[i]
    precio=preciox1b[i]
    if precio < 1.50:
        print(fruta)
