'''
@author: Sebastián González Juárez
'''
#Calcular raíces de ecuaciones de segundo grado
import math
import cmath

print ("Método de 2do grado")

while True:
    try:
        a = float(input("Ingrese coeficiente a: "))
        b = float(input("Ingrese coeficiente b: "))
        c = float(input("Ingrese coeficiente c: "))
        if a==0:
            print("El coeficiente a no puede ser igual a cero, inserta nuevamente tus datos")
        else:
            discriminante = b**2-4*a*c
            if discriminante >= 0:
                if discriminante == 0:
                    x = -b / (2 * a)
                    print("La raíz única x es"+str(x))
                    break
                else:
                    x1=(-b+math. sqrt(discriminante))/2*a
                    x2=(-b-math. sqrt(discriminante))/2*a
                    print("La raíz real x1 es "+str(x1),"y la raíz real x2 es "+str(x2))
                    break
            else:
                x1=(-b+cmath. sqrt(discriminante))/2*a
                x2=(-b-cmath. sqrt(discriminante))/2*a
                print("La raíz imaginaria x1 es "+str(x1),"y la raíz imaginaria x2 es "+str(x2))
                break
    except (ValueError):
        print("Por favor ingresa un números válidos, vuelve a empezar")