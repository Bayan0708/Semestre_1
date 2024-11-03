from tkinter import *
from math import *
import matplotlib
import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure
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
    y1 = float(yinicial.get())
    y2 = float(yfinal.get())



    if x1 > x2:
        mensaje = "tu valor de a inicial debe ser menor b final"
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
        mensaje = "La raíz se ubica en x =" + str(xmed) + " y las iteraciones fueron " + str(i-1)
        MensaBiseccion.config(text = mensaje)

        n = 100000
        m = (x4-x3)/n
        listax = []
        listay = []
        for k in range (n+1):
            x4 = x3 + m*k
            listax.append (x4)
            listay.append (f(x4))  

        figura = Figure()
        subfigura = figura.add_subplot (111)
        subfigura.plot (listax, listay)
        subfigura.set(xlabel = 'Eje X', ylabel = 'Eje Y', title = "La raíz se ubica en x =" + str(xmed) + " y las iteraciones fueron " + str(i-1))
        subfigura.legend ()
        subfigura.grid ()
        subfigura.set_ylim(y1,y2)
        canvas = FigureCanvasTkAgg (figura, master = ventanaBiseccion)
        canvas.get_tk_widget().grid(row = 5, column = 0, padx = 5, pady = 5, sticky = "nsew", columnspan = 10)
        canvas.draw ()
        toolbar = NavigationToolbar2Tk(canvas, ventanaBiseccion, pack_toolbar=False)
        toolbar.grid(row=6, column=0, padx=5, pady=5, sticky="nsew", columnspan=10)

    return

def Regresar ():
    ventanaBiseccion.destroy()

#---------------------------------- Textos Bisección -------------------------------------

estructura = Label (ventanaBiseccion, text = "Este programa encuentra una raíz de ecuaciones", font = ("Courier", 11))
estructura.grid (row = 0,column = 0, padx = 30, pady = 10, columnspan = 10)

BiseccionFuncionL = Label (ventanaBiseccion, text = "Escribe tu funcion:")
BiseccionFuncionL.grid (row = 1,column = 0, padx = 10, pady = 10)

Biseccion_xiL = Label (ventanaBiseccion, text = "-x: ")
Biseccion_xiL.grid (row = 1,column = 2, padx = 10, pady = 10)

Biseccion_xfL = Label (ventanaBiseccion, text = "x:")
Biseccion_xfL.grid (row = 1,column = 4, padx = 10, pady = 10)

Biseccion_yiL = Label (ventanaBiseccion, text = "-y: ")
Biseccion_yiL.grid (row = 1,column = 6, padx = 10, pady = 10)

Biseccion_yfL = Label (ventanaBiseccion, text = "y:")
Biseccion_yfL.grid (row = 1,column = 8, padx = 10, pady = 10)



BiseccionInicialL = Label (ventanaBiseccion, text = "a:")
BiseccionInicialL.grid (row = 2,column = 0, padx = 10, pady = 10)

BiseccionFinalL = Label (ventanaBiseccion, text = "b:")
BiseccionFinalL.grid (row = 2,column = 2, padx = 10, pady = 10)

Tercero2doGrado = Label (ventanaBiseccion, text = "Criterio de convergencia:")
Tercero2doGrado.grid (row = 2,column = 4, padx = 10, pady = 10)

Cuarto2doGrado = Label (ventanaBiseccion, text = "Criterio de exactitud:")
Cuarto2doGrado.grid (row = 2,column = 6, padx = 10, pady = 10)

Biseccion_IntervalosL = Label (ventanaBiseccion, text = "Interaciones: ")
Biseccion_IntervalosL.grid (row = 2,column = 8, padx = 10, pady = 10)




#---------------------------------- Entradas Bisección -------------------------------------
# Colocamos entry para poder tener la entrada del usuario

funBiseccion = Entry (ventanaBiseccion, justify = "center")
funBiseccion.grid (row = 1,column = 1, padx = 10, pady = 10,)

xinicial = Entry (ventanaBiseccion, justify = "center")
xinicial.grid (row = 1,column = 3, padx = 10, pady = 10,)

xfinal = Entry (ventanaBiseccion, justify = "center")
xfinal.grid (row = 1,column = 5, padx = 10, pady = 10,)

yinicial = Entry (ventanaBiseccion, justify = "center")
yinicial.grid (row = 1,column = 7, padx = 10, pady = 10,)

yfinal = Entry (ventanaBiseccion, justify = "center")
yfinal.grid (row = 1,column = 9, padx = 10, pady = 10,)


xinicialBiseccion = Entry (ventanaBiseccion, justify = "center")
xinicialBiseccion.grid (row = 2,column = 1, padx = 10, pady = 10,)

xfinalBiseccion = Entry (ventanaBiseccion, justify = "center")
xfinalBiseccion.grid (row = 2,column = 3, padx = 10, pady = 10)

EntryCriteriodeconvergencia = Entry (ventanaBiseccion, justify = "center")
EntryCriteriodeconvergencia.grid (row = 2,column = 5, padx = 10, pady = 10)

EntryCriteriodeexactitud = Entry (ventanaBiseccion, justify = "center")
EntryCriteriodeexactitud.grid (row = 2,column = 7, padx = 10, pady = 10,)


Eintervalos = Entry (ventanaBiseccion, justify = "center")
Eintervalos.grid (row = 2,column = 9, padx = 10, pady = 10)



#---------------------------------- Salidas Bisección -------------------------------------
# Etiqueta para mostrar el mensaje

MensaBiseccion = Label (ventanaBiseccion)
MensaBiseccion.grid(row = 4,column = 0, padx = 30, pady = 10, columnspan = 10)

#---------------------------------- Botones Bisección -------------------------------------

btnCalcular = Button (ventanaBiseccion, text = "Calcular", command = Calcular)
btnCalcular.grid  (row = 3,column = 1, padx = 30, pady = 10, columnspan = 10)
btnCalcular.config (cursor = "hand2")

botonRegresar = Button(ventanaBiseccion, text = "Regresar", command = Regresar)
botonRegresar.grid (row = 7,column = 0, padx = 30, pady = 10)
botonRegresar.config (cursor = "hand2")

#---------------------------------- Fin Bisección -------------------------------------


ventanaBiseccion.mainloop ()