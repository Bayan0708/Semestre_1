from tkinter import *
from tkinter import *
from math import *
import matplotlib
import matplotlib.pyplot as plt





def evaluando (x,f):
    return eval (f)




# print ("Metodo de 2do grado")
# a = float(input("Ingrese coeficiente a: "))
# b = float(input("Ingrese coeficiente b: "))
# c = float(input("Ingrese coeficiente c: "))

# f = f"{a}*x**2+{b}*x+{c}"

# x_i = -10 #valor inicial
# x_f = 10 #valor final

# n = 20 # x_f - x_0


# m = (x_f-x_i)/n

# listax = []
# listay = []

# for k in range (n+1):
#     x_0 = x_i + m*k
#     listax.append (x_0)
#     listay.append (evaluando(x_0,f))



# plt.hlines(y=0,xmin=listax[0],xmax=listax[-1],color='k')
# plt.plot (listax,listay,'indigo')
# plt.xlabel('Eje X') # Etiqueta del eje X
# plt.ylabel('Eje Y') # Etiqueta del eje Y
# plt.title("El área bajo la curva es de ")
# plt.grid() # se activa la malla
# plt.show() # Se manda crear la gráfica





# if a==0:
#     print("El coeficiente a no puede ser igual a cero")
# else:
#     discriminante = b**2 - 4 * a * c
#     if discriminante >= 0:
#         if discriminante == 0:
#             x = -b / (2 * a)
#             print("La raíz única es {:.3f}".format(x))
#         else:
#             x1 = (-b + (discriminante**0.5)) / (2 * a)
#             x2 = (-b - (discriminante**0.5)) / (2 * a)
#             print("La raíz real x1 es {:.3f}".format(x1))
#             print("La raíz real x2 es {:.3f}".format(x2))
#     else:
#         discriminante = abs(discriminante)
#         parteReal = -b / (2 * a)
#         parteImaginaria =(discriminante**0.5) / (2 * a)
#         print("La raíz compleja x1 es {:.3f} + {:.3f}i".format(parteReal, parteImaginaria))
#         print("La raíz compleja x2 es {:.3f} - {:.3f}i".format(parteReal, parteImaginaria))





print ("Metodo de 2do grado")
a = float(input("Ingrese coeficiente a: "))
b = float(input("Ingrese coeficiente b: "))
c = float(input("Ingrese coeficiente c: "))

f = f"{a}*x**2+{b}*x+{c}"

x_i = -10 #valor inicial
x_f = 10 #valor final

n = 20 # x_f - x_0


m = (x_f-x_i)/n

listax = []
listay = []

for k in range (n+1):
    x_0 = x_i + m*k
    listax.append (x_0)
    listay.append (evaluando(x_0,f))

fig, grafica = plt.subplots()


grafica.hlines(y=0,xmin=listax[0],xmax=listax[-1],color='k')
grafica.plot (listax,listay,'indigo')
plt.xlabel('Eje X') # Etiqueta del eje X
plt.ylabel('Eje Y') # Etiqueta del eje Y
plt.title("El área bajo la curva es de ")
plt.grid() # se activa la malla
plt.show() # Se manda crear la gráfica



# En vez de fig, grafica = plt.subplots() poner:
#figura = matplotlib.figure.Figure()
#grafica = figura.add_subplot()



if a==0:
    print("El coeficiente a no puede ser igual a cero")
else:
    discriminante = b**2 - 4 * a * c
    if discriminante >= 0:
        if discriminante == 0:
            x = -b / (2 * a)
            print("La raíz única es {:.3f}".format(x))
        else:
            x1 = (-b + (discriminante**0.5)) / (2 * a)
            x2 = (-b - (discriminante**0.5)) / (2 * a)
            print("La raíz real x1 es {:.3f}".format(x1))
            print("La raíz real x2 es {:.3f}".format(x2))
    else:
        discriminante = abs(discriminante)
        parteReal = -b / (2 * a)
        parteImaginaria =(discriminante**0.5) / (2 * a)
        print("La raíz compleja x1 es {:.3f} + {:.3f}i".format(parteReal, parteImaginaria))
        print("La raíz compleja x2 es {:.3f} - {:.3f}i".format(parteReal, parteImaginaria))



