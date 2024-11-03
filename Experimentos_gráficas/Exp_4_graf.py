'''
@author: Sebastián González Juárez
'''

'''

'''


from math import *
import matplotlib

import matplotlib.pyplot as plt



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

X = lista
Y = lista2

lista3 = lista
lista3.insert(0,a)
lista3.append (b)

lista4 = lista2
lista4.insert(0,0)
lista4.append (0)

PX = lista3 
PY = lista4
plt.plot (X,Y,'r')
plt.fill(PX, PY, 'g', alpha=0.5)
plt.xlabel('Eje X') # Etiqueta del eje X

plt.ylabel('Eje Y') # Etiqueta del eje Y

plt.title('Relleno del área bajo la curva')

plt.grid() # se activa la malla

plt.show() # Se manda crear la gráfica

