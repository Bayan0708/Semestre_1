#Diseño (diagrama de flujo) e Implementación (lenguaje Python) del Método Trapezoidal Compuesto
# -- coding: utf-8 --

from math import*

def evaluación (x):
  copia=f.copy()
  for j in range(len(copia)):
    if copia[j]=="x":
      copia[j]==x
  return eval("".join(copia))
opcion=""
print("\nMétodo Trapezoidal Compuesto")
lista = ["\nAntes de ingresar tu función, lee las siguentes sugerencias:","1. Introduce solo funciones que el programa math pueda leer.","2. Revisa bien tu intervalo, ya que necesitamos continuidad en la función.","En caso de no cumplir con lo anterior, el programa se cerrará." ]
for v in lista:
  print(v)
f=list(input("Dame la función: "))

while (opcion!="A"):
    while True:
      try:
        a=float(input("Dame la frontera inferior del intervalo: "))
        break
      except ValueError:
        print("Inserta únicamente números reales")
    while True:
      try:
        b=float(input("Dame la frontera superior del intervalo: "))
        break
      except ValueError:
        print("\nInserta únicamente números reales")
    if b>=a:
      opcion="A"
    else:
     print("El valor de la frontera inferior debe ser menor que el valor de la frontera superior, introduce nuevamente tus datos")
a=a
b=b
while (opcion==""):
    while True:
      try:
        n=int(input("\nDame el número de intervalos: "))
        break
      except ValueError:
        print("\nInserta únicamente números enteros pares mayores a 0")
    if n>0:
        break
    else:
        print("\nInserta únicamente números enteros pares mayores a 0")
n=n
h=(b-a)/n
Resultado=0
for i in range(1,n):
  x=a+i*h
  Resultado+=2*evaluación(x)
Resultado+=evaluación(a)+evaluación(b)
Resultado=Resultado*(h/2)
print ("\nLa aproximación del área bajo la curva de tu función, es = "+str( Resultado))