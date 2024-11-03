#Archivo para probar gráficas 1

# -- coding: utf-8 --
from math import *
import matplotlib.pyplot as plot
import matplotlib




def trapecio():
    print("\nMétodo Trapezoidal Compuesto")
    Especificaciones=["\nAntes de ingresar tu función, lee las siguientes especificaciones:","1. Introduce funciones que el programa math pueda leer y revisa que estén bien escritas.","2. Revisa bien tu intervalo, ya que necesitamos continuidad en la función.","3. Toma en cuenta que tu función debe estar en función de x.","En caso de no cumplir con lo anterior, el programa se cerrará o probablemente obtengamos un resultado erróneo." ]
    for v in Especificaciones:
        print(v)
        f = input("\nIngresa tu función: ")
    while True:
        a = pregunta_trapecio ("empiece")
        



def pregunta_trapecio(end):
	while True:
		try:
			print("\nRecuerda que puedes usar, por ejemplo. 'e', '97/4', '7.22'. uwu")
			return(float(eval(input(f"Dime donde quieres que {end} la integral. :3\nTú: Quiero que {end} en "))))
		except:
			print("\nEse no fue un número real. Uwu")







while True:
    while True:
      try:
        inferior=float(input("\nDame la frontera inferior del intervalo: "))
        break
      except ValueError:
        print("\nInserta únicamente números reales")
    while True:
      try:
        superior=float(input("\nDame la frontera superior del intervalo: "))
        break
      except ValueError:
        print("\nInserta únicamente números reales")
    if superior>=inferior:
      break
    else:
     print("\nEl valor de la frontera inferior debe ser menor o igual que el valor de la frontera superior, introduce nuevamente tus datos")

inferior=inferior
superior=superior

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
h=(superior-inferior)/n
Resultado=0
Resultado+=evaluando_copia_f(inferior)*(h/2)+evaluando_copia_f(superior)*(h/2)

for i in range(1,n):
    x=inferior+i*h
    Resultado+=evaluando_copia_f(x)*h

print ("\nLa aproximación del área bajo la curva de tu función, es = "+str( Resultado))

trapecio()