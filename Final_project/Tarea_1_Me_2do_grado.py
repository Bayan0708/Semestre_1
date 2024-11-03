'''
@author: Sebastián González Juárez
Universidad Nacional Autónoma de México 
Facultad de Ciencias
Computación
Método de segundo grado
'''

import math
import cmath

#-Calcular raicez de ecuaciones de segundo grado
print ("Metodo de 2do grado")
a = float(input("Ingrese coeficiente a: "))
b = float(input("Ingrese coeficiente b: "))
c = float(input("Ingrese coeficiente c: "))
if a==0:
    print("El coeficiente a no puede ser igual a cero")
else:
    discriminante = b**2 - 4 * a * c
    if discriminante >= 0:
        if discriminante == 0:
            x = -b / (2 * a)
            print("La raíz única es =" + str(x))
        else:
            x1 = (-b + (discriminante**0.5)) / (2 * a)
            x2 = (-b - (discriminante**0.5)) / (2 * a)
            print("Las raíces reales son: x1 = " + str(x1) + "  y  " + "x2 = " + str(x2))
    else:
        x1 = (-b + cmath.sqrt(discriminante))/(2*a)
        x2 = (-b - cmath.sqrt(discriminante))/(2*a)
        print("Las raíces complejas son: x1 = " + str(x1) + "  y   x2 = "   + str(x2))
