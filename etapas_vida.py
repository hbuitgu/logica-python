edad= int(input("cuantos años tienes: "))

if (edad <= 14 and edad >=0):
    print(f"eres un niño tienes {edad} años")
elif(edad >= 15 and edad < 28):
    print(f"eres un joven tienes {edad} años")
elif(edad >= 29 and edad <= 60):
    print(f"eres un adulto tienes {edad} años")
elif(edad >= 61):
    print(f"eres un adulto mayor tienes {edad} años")
else:
    print("el dato ingresado no es valido")