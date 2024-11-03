from tkinter import *
from math import *
import matplotlib
import matplotlib.pyplot as plt
from math import *
import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

ventanaEcuaciones2doGrado = Tk()
ventanaEcuaciones2doGrado.title("Ecuaciones 2do Grado")

def Calcular ():

    def evaluando (x,f):
        return eval (f)

    a = int (coeficientea.get())
    b = int (coeficienteb.get())
    c = int (coeficientec.get())
    x_i = float (xinicial.get()) #valor inicial
    x_f = float (xfinal.get()) #valor final
    y_i = float (yinicial.get()) #valor inicial
    y_f = float (yfinal.get()) #valor final

    if a==0:
        mensaje = "El coeficiente a no puede ser igual a cero, ingresa otros datos"
        MensaEcuaciones2doGrado.config(text = mensaje)
    else:
        discriminante = b**2 - 4 * a * c
        if discriminante >= 0:
            if discriminante == 0:
                x = -b / (2 * a)
                mensaje = "La raíz única es =" + str(x)
                MensaEcuaciones2doGrado.config(text = mensaje)
                f = f"{a}*x**2+{b}*x+{c}"
                n = 100 # x_f - x_0
                m = (x_f-x_i)/n
                listax = []
                listay = []
                for k in range (n+1):
                    x_0 = x_i + m*k
                    listax.append (x_0)
                    listay.append (evaluando(x_0,f))
                figura = Figure()
                subfigura = figura.add_subplot (111)
                subfigura.plot (listax, listay)
                subfigura.set(xlabel = 'Eje X', ylabel = 'Eje Y', title = "La raíz única es =" + str(x))
                subfigura.legend ()
                subfigura.grid ()
                subfigura.set_ylim(y_i,y_f)
                canvas = FigureCanvasTkAgg (figura, master = ventanaEcuaciones2doGrado)
                canvas.get_tk_widget().grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "nsew", columnspan = 10)
                canvas.draw ()
                toolbar = NavigationToolbar2Tk(canvas, ventanaEcuaciones2doGrado, pack_toolbar=False)
                toolbar.grid(row=5, column=0, padx=5, pady=5, sticky="nsew", columnspan=8)



            else:
                x1 = (-b + (discriminante**0.5)) / (2 * a)
                x2 = (-b - (discriminante**0.5)) / (2 * a)
                mensaje = "Las raíces reales son: x1 = " + str(x1) + "  y  " + "x2 = " + str(x2)
                MensaEcuaciones2doGrado.config(text = mensaje)
                f = f"{a}*x**2+{b}*x+{c}"
                n = 100 # x_f - x_0
                m = (x_f-x_i)/n
                listax = []
                listay = []
                for k in range (n+1):
                    x_0 = x_i + m*k
                    listax.append (x_0)
                    listay.append (evaluando(x_0,f))
                figura = Figure()
                subfigura = figura.add_subplot (111)
                subfigura.plot (listax, listay)
                subfigura.set(xlabel = 'Eje X', ylabel = 'Eje Y', title = "Las raíces reales son: x1 = " + str(x1) + "  y  " + "x2 = " + str(x2))
                subfigura.legend ()
                subfigura.grid ()
                subfigura.set_ylim(y_i,y_f)
                canvas = FigureCanvasTkAgg (figura, master = ventanaEcuaciones2doGrado)
                canvas.get_tk_widget().grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "nsew", columnspan = 10)
                canvas.draw ()
                toolbar = NavigationToolbar2Tk(canvas, ventanaEcuaciones2doGrado, pack_toolbar=False)
                toolbar.grid(row=5, column=0, padx=5, pady=5, sticky="nsew", columnspan=8)
        else:
            discriminante = abs(discriminante)
            parteReal = -b / (2 * a)
            parteImaginaria =(discriminante**0.5) / (2 * a)
            mensaje = "Las raíces complejas son: x1 =" + str(parteReal) + "   y   " + "x2 = " + str(parteImaginaria) + "i"
            MensaEcuaciones2doGrado.config(text = mensaje) 
            f = f"{a}*x**2+{b}*x+{c}"
            n = 100 # x_f - x_0
            m = (x_f-x_i)/n
            listax = []
            listay = []
            for k in range (n+1):
                x_0 = x_i + m*k
                listax.append (x_0)
                listay.append (evaluando(x_0,f))
            figura = Figure()
            subfigura = figura.add_subplot (111)
            subfigura.plot (listax, listay)
            subfigura.set(xlabel = 'Eje X', ylabel = 'Eje Y', title = "Las raíces complejas son: x1 = " + str(parteReal) + "   y   " + "x2 = " + str(parteImaginaria) + "i")
            subfigura.legend ()
            subfigura.grid ()
            subfigura.set_ylim(y_i,y_f)
            canvas = FigureCanvasTkAgg (figura, master = ventanaEcuaciones2doGrado)
            canvas.get_tk_widget().grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "nsew", columnspan = 10)
            canvas.draw ()
            toolbar = NavigationToolbar2Tk(canvas, ventanaEcuaciones2doGrado, pack_toolbar=False)
            toolbar.grid(row=5, column=0, padx=5, pady=5, sticky="nsew", columnspan=8)    
                     


def Regresar ():
    ventanaEcuaciones2doGrado.destroy()

#---------------------------------- Textos me2doGrado -------------------------------------

estructura = Label (ventanaEcuaciones2doGrado, text = "Este programa encuentra las raíces de ecuaciones con la forma: ax^2+bx+c", font = ("Courier", 11))
estructura.grid (row = 0,column = 0, padx = 30, pady = 10, columnspan = 8)


Me2doGrado_x_i = Label (ventanaEcuaciones2doGrado, text = "-x: ")
Me2doGrado_x_i.grid (row = 1,column = 0, padx = 10, pady = 10)

Me2doGrado_x_f = Label (ventanaEcuaciones2doGrado, text = "x:")
Me2doGrado_x_f.grid (row = 1,column = 2, padx = 10, pady = 10)

Me2doGrado_y_i = Label (ventanaEcuaciones2doGrado, text = "-y: ")
Me2doGrado_y_i.grid (row = 1,column = 4, padx = 10, pady = 10)

Me2doGrado_y_f = Label (ventanaEcuaciones2doGrado, text = "y: ")
Me2doGrado_y_f.grid (row = 1,column = 6, padx = 10, pady = 10)


Primero2doGrado = Label (ventanaEcuaciones2doGrado, text = "Coeficiente a:")
Primero2doGrado.grid (row = 2,column = 0, padx = 10, pady = 10)

Segundo2doGrado = Label (ventanaEcuaciones2doGrado, text = "Coeficiente b:")
Segundo2doGrado.grid (row = 2,column = 2, padx = 10, pady = 10)

Tercero2doGrado = Label (ventanaEcuaciones2doGrado, text = "Coeficiente c:")
Tercero2doGrado.grid (row = 2,column = 4, padx = 10, pady = 10)





#---------------------------------- Entradas me2doGrado -------------------------------------
# Colocamos entry para poder tener la entrada del usuario

xinicial = Entry (ventanaEcuaciones2doGrado, justify = "center")
xinicial.grid (row = 1,column = 1, padx = 10, pady = 10,)

xfinal = Entry (ventanaEcuaciones2doGrado, justify = "center")
xfinal.grid (row = 1,column = 3, padx = 10, pady = 10,)

yinicial = Entry (ventanaEcuaciones2doGrado, justify = "center")
yinicial.grid (row = 1,column = 5, padx = 10, pady = 10,)

yfinal = Entry (ventanaEcuaciones2doGrado, justify = "center")
yfinal.grid (row = 1,column = 7, padx = 10, pady = 10,)


coeficientea = Entry (ventanaEcuaciones2doGrado, justify = "center")
coeficientea.grid (row = 2,column = 1, padx = 10, pady = 10,)

coeficienteb = Entry (ventanaEcuaciones2doGrado, justify = "center")
coeficienteb.grid (row = 2,column = 3, padx = 10, pady = 10)

coeficientec = Entry (ventanaEcuaciones2doGrado, justify = "center")
coeficientec.grid (row = 2,column = 5, padx = 10, pady = 10)


#---------------------------------- Salidas me2doGrado -------------------------------------
# Etiqueta para mostrar el mensaje

MensaEcuaciones2doGrado = Label (ventanaEcuaciones2doGrado)
MensaEcuaciones2doGrado.grid(row = 3,column = 0, padx = 30, pady = 10, columnspan = 8)

#---------------------------------- Botones me2doGrado -------------------------------------

btnCalcular = Button (ventanaEcuaciones2doGrado, text = "Calcular", command = Calcular)
btnCalcular.grid  (row = 2,column = 7, padx = 30, pady = 10, columnspan = 6)
btnCalcular.config (cursor = "hand2")

botonRegresar = Button(ventanaEcuaciones2doGrado, text = "Regresar", command = Regresar)
botonRegresar.grid (row = 6,column = 0, padx = 30, pady = 10)
botonRegresar.config (cursor = "hand2")

#---------------------------------- Fin me2doGrado -------------------------------------


ventanaEcuaciones2doGrado.mainloop ()
