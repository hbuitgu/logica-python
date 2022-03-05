#importando librerias 
import math


#se debe crear una variable controladora , es la que detiene el proceso cuando se cumple la condicion 


##opcion=()

#declaro el bucle o el ciclo, repeticion, iteracion, loop, la vuelta el auto incremento se puede escribir numero+=1 es lo mismo que decir numero =numeor +1

# while(numero<=20):
#     print("no importa que equipo gane")
#     print(numero)
#     numero=numero+1
    


print("empanadas el Machetico")
print("******")
print("0. digita 0 para salir")
print("1. digita 0 para calcular la raiz de un numero: ")
print("2. digita 0 para calcular la potencia de 2 en un #")
opcion=()
while(opcion!=0):
    opcion=int(input("digita una opcion: "))
    ##pregunte por la opcion
    if (opcion==0):
        break
    elif(opcion==1):
        numero=int(input("digita un numero "))
        ##cuando necesite lebrerias debo importarlas, son codigos prefabricados 
        raiz=math.sqrt(numero)
        print(f"la raiz de {numero} es {raiz}")
    elif(opcion==2):
        numero=int(input("digita un numero "))
        potencia=math.pow(numero,2)
        print(f"la potencia de {numero} es {potencia}")
    else:
        print("opcion ingresada no es valida")
