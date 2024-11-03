from math import *

original =input()
valor=float(input())
remplazo = original.replace("x", str(valor))

print("Funcion original = " + original)
print("Funcion con valores = " + remplazo)

resultado = eval(remplazo)

print("Resultado = ", resultado)