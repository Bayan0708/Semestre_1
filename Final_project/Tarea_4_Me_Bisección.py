'''
@author: Sebastián González Juárez
Universidad Nacional Autónoma de México 
Facultad de Ciencias
Computación
Método de Bisección
'''
from math import *
import matplotlib
import matplotlib.pyplot as plt
    
def f(x):
    return eval(ec)

ec=input("\nIngrese la función: ") 
x1=float(input("\na: "))
x2=float(input("\nb: "))
Criteriodeconvergencia=float(input("\nCriterio de convergencia: "))
Criteriodeexactitud=float(input("\nCriterio de exactitud: "))
iteraciones = float(input("\nNúmero de intervalos: "))
x3 = float(input('\n-x: '))
x4 = float(input('\nx: '))

if x1 > x2:
    print ("tu valor de x inicial debe ser menor a x final")

else:
    i = 0
    while i <= iteraciones :
        i=i+1
        xmed=(x1+x2)/2
        fxmed=f(xmed)
        if f(x1)==0.0:
            xmed=x1
            break
        if f(x2)==0.0:
            xmed=x2
            break
        if fxmed==0.0:
            break
    
        if (f(x1)*f(xmed))<0:
            x1=x1
            x2=xmed
        else:
            x1=xmed
            x2=x2
        error1=abs(x2-x1)
        error2=abs(f(xmed))
        if error1<Criteriodeconvergencia and error2<Criteriodeexactitud:
            break
    print ("La raíz se ubica en x =" + str(xmed) + " y las iteraciones fueron " + str(i-1))

    n = 10000
    m = (x4-x3)/n
    listax = []
    listay = []
    for k in range (n+1):
        x4 = x3 + m*k
        listax.append (x4)
        listay.append (f(x4))   
    fig, grafica = plt.subplots()
    grafica.hlines(y=0,xmin=listax[0],xmax=listax[-1],color='k')
    grafica.plot (listax,listay,'indigo')
    plt.xlabel('Eje X') # Etiqueta del eje X
    plt.ylabel('Eje Y') # Etiqueta del eje Y
    plt.title("La raíz se ubica en x =" + str(xmed) + " y las iteraciones fueron " + str(i-1))
    plt.grid() # se activa la malla
    plt.show() # Se manda crear la gráfica