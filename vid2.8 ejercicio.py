# elabore un programa en python que pida al usuario una cantidad de segundos y
# muestre cuantas horas,minutos y segundos son

segundos=int(input("Ingrese cantidad de seundos: "))
#segundos=int(segundos) asi tambien es valido o como arriba

horas=segundos//3600

sobrante1=segundos%3600

minutos=sobrante1//60

sobrante2= sobrante1%60

print("Horas")
print(horas)

print("Minutos")
print(minutos)

print("Segundos")
print(sobrante2)

