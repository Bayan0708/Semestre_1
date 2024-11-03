#Diseño (diagrama de flujo) e Implementación (lenguaje Python) del Método Trapezoidal Compuesto
# -- coding: utf-8 --

from math import*
def E (x):
  C=fun.copy()
  for k in range(len(C)):
    if C[k]=="x":
      C[k]==x
  return eval("".join(C))
fun=list(input("fun "))
a=float(input("a "))
b=float(input("b "))
n=int(input("n "))
s=b-a
h=s/n
A=0
for k in range(1,n):
    x=a+k*h
    A+=2*E(x)
A+=E(a)
A+=E(b)
A=A*(h/2)
print (f"Area={A}")