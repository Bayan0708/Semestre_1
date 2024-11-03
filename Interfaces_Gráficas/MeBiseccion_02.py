from tkinter import *
from tkinter import *
from math import *
import matplotlib
import matplotlib.pyplot as plt


ventanaBiseccion = Tk()
ventanaBiseccion.title("Metodo de Bisección")

def Calcular ():
    
    def f(x):
        return eval(ec)

    ec=(funBiseccion.get())  
    x1=float(xinicialBiseccion.get())
    x2=float(xfinalBiseccion.get())
    Criteriodeconvergencia=float(EntryCriteriodeconvergencia.get())
    Criteriodeexactitud=float(EntryCriteriodeexactitud.get())
    iteraciones = float(Eintervalos.get())
    x3 = float(xinicial.get())
    x4 = float(xfinal.get())



    if x1 > x2:
        mensaje = "tu valor de x inicial debe ser menor a x final"
        MensaBiseccion.config(text = mensaje)  
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
        mensaje = "La raíz se ubica en x = {:.3f} y las iteraciones fueron  {:.3f}".format(xmed, i-1)
        MensaBiseccion.config(text = mensaje)

        n = 100
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
        plt.title("La raíz se ubica en x = {:.3f} y las iteraciones fueron  {:.3f}".format(xmed, i-1))
        plt.grid() # se activa la malla
        plt.show() # Se manda crear la gráfica
    return

def Regresar ():
    ventanaBiseccion.destroy()

#---------------------------------- Textos me2doGrado -------------------------------------

estructura = Label (ventanaBiseccion, text = "Este programa encuentra las raíces de ecuaciones", font = ("Courier", 11))
estructura.grid (row = 0,column = 0, padx = 30, pady = 10, columnspan = 8)

BiseccionFuncionL = Label (ventanaBiseccion, text = "Escribe tu funcion:")
BiseccionFuncionL.grid (row = 1,column = 0, padx = 10, pady = 10)

BiseccionInicialL = Label (ventanaBiseccion, text = "x inicial:")
BiseccionInicialL.grid (row = 2,column = 0, padx = 10, pady = 10)

BiseccionFinalL = Label (ventanaBiseccion, text = "x final:")
BiseccionFinalL.grid (row = 2,column = 2, padx = 10, pady = 10)

Tercero2doGrado = Label (ventanaBiseccion, text = "Criterio de convergencia:")
Tercero2doGrado.grid (row = 2,column = 4, padx = 10, pady = 10)

Tercero2doGrado = Label (ventanaBiseccion, text = "Criterio de exactitud:")
Tercero2doGrado.grid (row = 2,column = 6, padx = 10, pady = 10)

Biseccion_nL = Label (ventanaBiseccion, text = "-x: ")
Biseccion_nL.grid (row = 1,column = 2, padx = 10, pady = 10)

Biseccion_fL = Label (ventanaBiseccion, text = "x:")
Biseccion_fL.grid (row = 1,column = 4, padx = 10, pady = 10)

Biseccion_IntervalosL = Label (ventanaBiseccion, text = "Interaciones: ")
Biseccion_IntervalosL.grid (row = 1,column = 6, padx = 10, pady = 10)




#---------------------------------- Entradas me2doGrado -------------------------------------
# Colocamos entry para poder tener la entrada del usuario

funBiseccion = Entry (ventanaBiseccion, justify = "center")
funBiseccion.grid (row = 1,column = 1, padx = 10, pady = 10,)

xinicialBiseccion = Entry (ventanaBiseccion, justify = "center")
xinicialBiseccion.grid (row = 2,column = 1, padx = 10, pady = 10,)

xfinalBiseccion = Entry (ventanaBiseccion, justify = "center")
xfinalBiseccion.grid (row = 2,column = 3, padx = 10, pady = 10)

EntryCriteriodeconvergencia = Entry (ventanaBiseccion, justify = "center")
EntryCriteriodeconvergencia.grid (row = 2,column = 5, padx = 10, pady = 10)

EntryCriteriodeexactitud = Entry (ventanaBiseccion, justify = "center")
EntryCriteriodeexactitud.grid (row = 2,column = 7, padx = 10, pady = 10,)


Eintervalos = Entry (ventanaBiseccion, justify = "center")
Eintervalos.grid (row = 1,column = 7, padx = 10, pady = 10)


xinicial = Entry (ventanaBiseccion, justify = "center")
xinicial.grid (row = 1,column = 3, padx = 10, pady = 10,)

xfinal = Entry (ventanaBiseccion, justify = "center")
xfinal.grid (row = 1,column = 5, padx = 10, pady = 10,)

#---------------------------------- Salidas me2doGrado -------------------------------------
# Etiqueta para mostrar el mensaje

MensaBiseccion = Label (ventanaBiseccion)
MensaBiseccion.grid(row = 4,column = 0, padx = 30, pady = 10, columnspan = 10)

#---------------------------------- Botones me2doGrado -------------------------------------

btnCalcular = Button (ventanaBiseccion, text = "Calcular", command = Calcular)
btnCalcular.grid  (row = 3,column = 1, padx = 30, pady = 10, columnspan = 10)
btnCalcular.config (cursor = "hand2")

botonRegresar = Button(ventanaBiseccion, text = "Regresar", command = Regresar)
botonRegresar.grid (row = 5,column = 0, padx = 30, pady = 10)
botonRegresar.config (cursor = "hand2")

#---------------------------------- Fin me2doGrado -------------------------------------


ventanaBiseccion.mainloop ()