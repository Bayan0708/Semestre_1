# -*- coding: utf-8 -*-
#area de un rectangulo
print("Vamos a calcular el area de un rectangulo")
print("Por favor, proporciona la base")
base=int(input())
print("Por favor, proporciona la altura")
altura=int(input())
resultado= base * altura
print("base["+str(base)+"]altura["+str(altura)+"]Area=["+str(resultado)+"]")

print(f"base[{base}]altura[{altura}]Area=[{resultado}]")

print("base=",base,"altura=",altura,"area=",resultado)

#area de un triangulo
print("Vamos a calcular el area de un triangulo")
base=int(input("Por favor, proporciona la base del triangulo $ "))
altura=int(input("Por favor, proporciona la altura $ "))
resultado= (base * altura)/2
print("base["+str(base)+"]altura["+str(altura)+"]Area=["+str(resultado)+"]")

print(f"base[{base}]altura[{altura}]Area=[{resultado}]")

print("base=",base,"altura=",altura,"area=",resultado)