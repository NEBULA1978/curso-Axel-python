#todas la tablas de multiplicar



for n in range(1,10):
    print("---Tabla "+str(n)+"---")
    for i in range(10):
        resultado= i*n
        print(i,"x",n,"=",resultado)