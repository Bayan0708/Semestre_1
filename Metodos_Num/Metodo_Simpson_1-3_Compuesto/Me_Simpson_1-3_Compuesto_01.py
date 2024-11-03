#Diseño (diagrama de flujo) e Implementación (lenguaje Python) del Método Simpson 1/3 Compuesto
# -- coding: utf-8 --

from math import*

def evaluación (x):
  copia=función.copy()
  for j in range(len(copia)):
    if copia[j]=="x":
      copia[j]==x
  return eval("".join(copia))

función=list(input("Escribe tu función>"))
a=float(input("Límite inferior a >"))
b=float(input("Límite superior b >"))
n=int(input("¿En cuántos intervalos quieres dividir?>"))

h=(b-a)/n

total=0

for i in range(1,n):
  x=a+i*h
  if i%2==0:
    total+=2*evaluación(x)
  else:
    total+=4*evaluación(x)

total+=evaluación(a)+evaluación(b)
total=total*(h/3)

print (f"Resultado={total}")