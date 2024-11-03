'''
@author: Sebastián González Juárez
Universidad Nacional Autónoma de México 
Facultad de Ciencias
Computación
Programa del método Trapezoidal Compuesto graficado
'''

#La siguiente paquetería permite obtener valores de varios tipos de funciones.
from math import *

#La siguiente paquetería permite la graficación.
import matplotlib.pyplot as plt


#La siguiente función remplaza los valores en forma de texto de x a la función que le demos, luego evaluara usando eval.
def funcion_Replace_Eval(x):
  remplazo = funcion.replace("x", str(x))
  resultado = eval(remplazo)
  return resultado

print("\nMétodo Trapezoidal Compuesto")

#Se introducen los datos para el funcionamiento del método.
Especificaciones=["\nAntes de ingresar tu función, lee las siguientes especificaciones:","1. Introduce funciones que el programa math pueda leer y revisa que estén bien escritas.","2. Revisa bien tu intervalo, ya que necesitamos continuidad en la función.","3. Toma en cuenta que tu función debe estar en función de x.","En caso de no cumplir con lo anterior, el programa se cerrará o probablemente obtengamos un resultado erróneo." ]
for v in Especificaciones:
  print(v)

funcion = input ("\nDame la función: ")

while True:
    while True:
      try:
        a = float(input("\nDame la frontera inferior del intervalo: "))
        break
      except ValueError:
        print("\nInserta únicamente números reales")
    while True:
      try:
        b = float(input("\nDame la frontera superior del intervalo: "))
        break
      except ValueError:
        print("\nInserta únicamente números reales")
    if a <= b:
      break
    else:
     print("\nEl valor de la frontera inferior debe ser menor o igual que el valor de la frontera superior, introduce nuevamente tus datos")
a = a
b = b

while True:
    while True:
      try:
        n=int(input("\nDame el número de intervalos: "))
        break
      except ValueError:
        print("\nInserta únicamente números enteros mayores a 0")
    if n>0:
        break
    else:
      print("\nInserta únicamente números enteros mayores a 0")
n=n

h = (b - a) / n


#Se crea una lista donde se metan los valores de x.
lista = []
aux = a
for i in range(0, n + 1):
  lista.append(aux)
  aux = aux + h

#Se crea una lista donde se metan los valores de y.
lista2 = []
for i in lista:
  valor = funcion_Replace_Eval(i)
  lista2.append(valor)

#Se incia una suma de la lista 2.
suma = 0
for i in range(1, len(lista2)-1):
  suma += lista2[i]

#Calculo del área bajo la curva, usa la fórmula.
area = (h / 2) * (lista2[0] + (suma * 2) + lista2[-1])
print("El área bajo la curva es de " + str(area))

#Se crean 2 listas que nos ayudan a gráficar.
lista3 = lista
lista3.insert(0,a)
lista3.append (b)
lista4 = lista2
lista4.insert(0,0)
lista4.append (0)

#Datos de la gráfica.
plt.plot (lista,lista2,'blue')
plt.fill(lista3 , lista4, 'blue', alpha=0.5)
plt.xlabel('Eje X') # Etiqueta del eje X
plt.ylabel('Eje Y') # Etiqueta del eje Y
plt.title('Función y área debajo de la curva')
plt.grid() # se activa la malla
plt.show() # Se manda crear la gráfica