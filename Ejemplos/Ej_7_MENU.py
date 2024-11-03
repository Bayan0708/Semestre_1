# -*- coding: utf-8 -*-

print("Opciones de calculo de areas")
print("Area de triangulo, usa la opcion '1'")
print("Area de rectangulo, usa la opcion '2'")
print("Salir, usa la opcion '3'")
opcion=""

while(opcion != "3"):
    opcion = input("Seleciona la opcion desada ")
    if(opcion == "2"):
        print("Calculo de area de rectangulo")
        print("Vamos a calcular el area de un rectangulo")
        print("Por favor, proporciona la base")
        base=int(input())
        print("Por favor, proporciona la altura")
        altura=int(input())
        resultado= base * altura
        print("base["+str(base)+"]altura["+str(altura)+"]Area=["+str(resultado)+"]")
        print(f"base[{base}]altura[{altura}]Area=[{resultado}]")
        print("base=",base,"altura=",altura,"area=",resultado)
    elif(opcion == "1"):
        print("Calculo de area de un triangulo")
        print("Vamos a calcular el area de un triangulo")
        base=int(input("Por favor, proporciona la base del triangulo $ "))
        altura=int(input("Por favor, proporciona la altura $ "))
        resultado= (base * altura)/2
        print("base["+str(base)+"]altura["+str(altura)+"]Area=["+str(resultado)+"]")
        print(f"base[{base}]altura[{altura}]Area=[{resultado}]")
        print("base=",base,"altura=",altura,"area=",resultado)
    elif(opcion == "3"):
        print("Adios")