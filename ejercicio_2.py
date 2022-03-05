##programar un componente que le pida el mes del año y pueda recibir 
mes=input("ingrese el mes del año: ").lower()

#caminos para clasificar el mes 

if (mes=="diciembre"or mes =="enero"or mes=="febrero" or mes =="marzo"):
    print("Estasn en Invierno")
elif(mes=="junio"or mes=="julio"or mes=="agosto"):
    print("estas en verano")
elif(mes=="mayo"or mes=="abril"):
    print("estas en Primavera")
elif(mes=="septiembe"or mes=="octubre"or mes=="noviembre"):
    print("estas en otoño")
else:
    print("el mes digitado no existe")
