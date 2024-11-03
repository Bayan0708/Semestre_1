#Calcular raicez de ecuaciones de segundo grado
import math
import cmath

print ("Metodo de 2do grado")

try:
    a = float(input("Ingrese coeficiente a: "))
    b = float(input("Ingrese coeficiente b: "))
    c = float(input("Ingrese coeficiente c: "))
except (ValueError):
    exit("Por favor ingresa un número válido")
if a==0:
    print("El coeficiente a no puede ser igual a cero")
else:
    discriminante = b**2-4*a*c
    if discriminante >= 0:
        if discriminante == 0:
            x = -b / (2 * a)
            print("La raíz única x es"+str(x))
        else:
            x1=(-b+cmath. sqrt(discriminante))/2*a
            x2=(-b+cmath. sqrt(discriminante))/2*a
            print("La raíz real x1 es "+str(x1),"y la raíz real x2 es "+str(x2))
    else:
        x1=(-b+cmath. sqrt(discriminante))/2*a
        x2=(-b+cmath. sqrt(discriminante))/2*a
        print("La raíz imaginaria x1 es "+str(x1),"y la raíz imaginaria x2 es "+str(x2))