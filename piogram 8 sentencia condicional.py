"""

print("inicio")

n=5
for i in range(n,8,2):
    print("Hola")
print("Fin")
"""
"""
presentar la tabla de multiplicar de un numero ingresado por wl usuario
0x2=0
1x2=2
.....
9x2=18

"""
n=int(input("ingrese un numero: "))
for i in range(10):
    resultado= i*n
    print(i,"x",n,"=",resultado)