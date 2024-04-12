VLanID = int(input("Ingrese el numero de la VLan: "))

if (1 <= VLanID <= 1005):
    print("El numero de VLan ingresado esta dentro del rango normal")
elif (1006 <= VLanID <= 4095):
    print("El numero VLan ingresado esta dentro del rango extendido")
else:
    print("El numero de VLan ingresado es desconocido")
