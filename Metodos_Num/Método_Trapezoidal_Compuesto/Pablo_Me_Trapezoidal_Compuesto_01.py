import math

"""
@author: Pablo Torres Venteño
"""

def f(x):
  remplazo = funcion.replace("x", str(x))
  resultado = eval(remplazo)
  return resultado


funcion = input("f = ")
a = int(input("a = "))
b = int(input("b = "))
n = int(input("n = "))
h = (b - a) / n

lista = []
aux = a
for i in range(0, n + 1):
  lista.append(aux)
  aux = aux + h

lista2 = []
for i in lista:
  valor = f(i)
  lista2.append(valor)

suma = 0
for i in range(1, len(lista2)-1):
  suma += lista2[i]

area = (h / 2) * (lista2[0] + (suma * 2) + lista2[-1])
print("El área es de " + str(area))