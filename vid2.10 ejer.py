# ejercicio
#ingresar dos numeros y sacar la media de dos notas y decir verdadero TRue o falso False

nota1=float(input("Ingrese nota1: "))
nota2=float(input("Ingrese nota2: "))
promedio=(nota1 + nota2)/2
print("El promedio es: "+str(promedio))

cond = promedio >=60
print("¿Aprobo la materia", cond)
