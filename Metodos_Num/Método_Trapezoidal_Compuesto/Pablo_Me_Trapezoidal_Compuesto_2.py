from math import *

"""
@author: Pablo Torres Venteño
"""

def funcionMetodoTrapezoidal(x):
  remplazo = funcion.replace("x", str(x))
  resultado = eval(remplazo)
  return resultado


funcion = input("Función $")
a = float(input("Primer intervalo $"))
b = float(input("Segundo intervalo $"))
n = int(input("No. intervalos a dividir $"))
h = (b - a) / n

listaInicial = []
aux = a
for i in range(0, n + 1):
  listaInicial.append(aux)
  aux = aux + h

listaEvaluada = []
for i in listaInicial:
  valor = funcionMetodoTrapezoidal(i)
  listaEvaluada.append(valor)

suma = 0
for i in range(1, len(listaEvaluada)-1):
  suma += listaEvaluada[i]

area = (h / 2) * (listaEvaluada[0] + (suma * 2) + listaEvaluada[-1])
print("El área es de " + str(area))