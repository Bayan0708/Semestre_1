#Diseño (diagrama de flujo) e Implementación (lenguaje Python) del Método Simpson 1/3 Compuesto
# -*- coding: utf-8 -*-
from math import*
def evaluación (x):
  copia=f.copy()
  for j in range(len(copia)):
    if copia[j]=="x":
      copia[j]==x
  return eval("".join(copia))
opcion=""
print("\nMétodo Simpson 1/3 Compuesto")
lista = ["\nAntes de ingresar tu función, lee las siguentes sugerencias:","1. Introduce solo funciones que el programa math pueda leer.","2. Revisa bien tu intervalo, ya que necesitamos continuidad en la función.","En caso de no cumplir con lo anterior, el programa se cerrará." ]
for v in lista:
  print(v)
f=list(input("\nDame la función: "))
while (opcion==""):
    while True:
      try:
        a=float(input("\nDame la frontera inferior del intervalo: "))
        break
      except ValueError:
        print("\nInserta unicamente números reales")
    while True:
      try:
        b=float(input("\nDame la frontera superior del intervalo: "))
        break
      except ValueError:
        print("\nInserta únicamente números reales")
    if b>=a:
      break
    else:
     print("\nEl valor de la frontera inferior debe ser menor que el valor de la frontera superior, introduce nuevamente tus datos")
a=a
b=b
while (opcion==""):
    while True:
      try:
        n=int(input("\nDame el número de intervalos: "))
        break
      except ValueError:
        print("\nInserta unicamente números enteros pares mayores a 0")
    if n%2==0 and n>0:
        break
    else:
        print("\nInserta unicamente números enteros pares mayores a 0")
n=n
h=(b-a)/n
Resultado=0
for i in range(1,n):
  x=a+i*h
  if i%2==0:
    Resultado+=2*evaluación(x)
  else:
    Resultado+=4*evaluación(x)
Resultado+=evaluación(a)+evaluación(b)
Resultado=Resultado*(h/3)
print ("\nLa aproximación del área bajo la curva de tu función, es = "+str( Resultado))