from sunau import Au_read
from tkinter import *
from tkinter import *
from math import *
import matplotlib
import matplotlib.pyplot as plt


ventanaEcuaciones2doGrado = Tk()
ventanaEcuaciones2doGrado.title("Ecuaciones 2do Grado")



def Calcular ():

    def evaluando (x,f):
        return eval (f)

    a = int (coeficientea.get())
    b = int (coeficienteb.get())
    c = int (coeficientec.get())
    
    if a==0:
        mensaje = "El coeficiente a no puede ser igual a cero, ingresa otros datos"
        MensaEcuaciones2doGrado.config(text = mensaje)
    else:
        discriminante = b**2 - 4 * a * c
        if discriminante >= 0:
            if discriminante == 0:
                x = -b / (2 * a)
                mensaje = "La raíz única es {:.3f}".format(x)
                MensaEcuaciones2doGrado.config(text = mensaje)
                f = f"{a}*x**2+{b}*x+{c}"
                x_i = float (ninicial.get()) #valor inicial
                x_f = float (nfinal.get()) #valor final
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
                plt.title("La raíz única es {:.3f}".format(x))
                plt.grid() # se activa la malla
                plt.show() # Se manda crear la gráfica

            else:
                x1 = (-b + (discriminante**0.5)) / (2 * a)
                x2 = (-b - (discriminante**0.5)) / (2 * a)
                mensaje = "Las raíces reales son: x1 = {:.3f}".format(x1) + "   y   " + "x2 = {:.3f}".format(x2)
                MensaEcuaciones2doGrado.config(text = mensaje)
                f = f"{a}*x**2+{b}*x+{c}"
                x_i = int (ninicial.get()) #valor inicial
                x_f = int (nfinal.get())#valor final
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
                plt.title("Las raíces reales son: x1 = {:.3f}".format(x1) + "   y   " + "x2 = {:.3f}".format(x2))
                plt.grid() # se activa la malla
                plt.show() # Se manda crear la gráfica
        else:
            discriminante = abs(discriminante)
            parteReal = -b / (2 * a)
            parteImaginaria =(discriminante**0.5) / (2 * a)
            mensaje = "Las raíces complejas son: x1 = {:.3f} + {:.3f}i".format(parteReal, parteImaginaria) + "   y   " + "x2 = {:.3f} - {:.3f}i".format(parteReal, parteImaginaria)
            MensaEcuaciones2doGrado.config(text = mensaje) 
            f = f"{a}*x**2+{b}*x+{c}"
            x_i = int (ninicial.get()) #valor inicial
            x_f = int (nfinal.get()) #valor final
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
            plt.title("Las raíces complejas son: x1 = {:.3f} + {:.3f}i".format(parteReal, parteImaginaria) + "   y   " + "x2 = {:.3f} - {:.3f}i".format(parteReal, parteImaginaria))
            plt.grid() # se activa la malla
            plt.show() # Se manda crear la gráfica
    
                     




def Regresar ():
    ventanaEcuaciones2doGrado.destroy()

#---------------------------------- Textos me2doGrado -------------------------------------

estructura = Label (ventanaEcuaciones2doGrado, text = "Este programa encuentra las raíces de ecuaciones con la forma: ax^2+bx+c", font = ("Courier", 11))
estructura.grid (row = 0,column = 0, padx = 30, pady = 10, columnspan = 6)

Primero2doGrado = Label (ventanaEcuaciones2doGrado, text = "Coeficiente a:")
Primero2doGrado.grid (row = 1,column = 0, padx = 10, pady = 10)

Segundo2doGrado = Label (ventanaEcuaciones2doGrado, text = "Coeficiente b:")
Segundo2doGrado.grid (row = 1,column = 2, padx = 10, pady = 10)

Tercero2doGrado = Label (ventanaEcuaciones2doGrado, text = "Coeficiente c:")
Tercero2doGrado.grid (row = 1,column = 4, padx = 10, pady = 10)

Cuarto2doGrado = Label (ventanaEcuaciones2doGrado, text = "-x: ")
Cuarto2doGrado.grid (row = 2,column = 2, padx = 10, pady = 10)

Cuarto2doGrado = Label (ventanaEcuaciones2doGrado, text = "x:")
Cuarto2doGrado.grid (row = 2,column = 4, padx = 10, pady = 10)



#---------------------------------- Entradas me2doGrado -------------------------------------
# Colocamos entry para poder tener la entrada del usuario

coeficientea = Entry (ventanaEcuaciones2doGrado, justify = "center")
coeficientea.grid (row = 1,column = 1, padx = 10, pady = 10,)

coeficienteb = Entry (ventanaEcuaciones2doGrado, justify = "center")
coeficienteb.grid (row = 1,column = 3, padx = 10, pady = 10)

coeficientec = Entry (ventanaEcuaciones2doGrado, justify = "center")
coeficientec.grid (row = 1,column = 5, padx = 10, pady = 10)

ninicial = Entry (ventanaEcuaciones2doGrado, justify = "center")
ninicial.grid (row = 2,column = 3, padx = 10, pady = 10,)

nfinal = Entry (ventanaEcuaciones2doGrado, justify = "center")
nfinal.grid (row = 2,column = 5, padx = 10, pady = 10,)

#---------------------------------- Salidas me2doGrado -------------------------------------
# Etiqueta para mostrar el mensaje

MensaEcuaciones2doGrado = Label (ventanaEcuaciones2doGrado)
MensaEcuaciones2doGrado.grid(row = 4,column = 0, padx = 30, pady = 10, columnspan = 6)

#---------------------------------- Botones me2doGrado -------------------------------------

btnCalcular = Button (ventanaEcuaciones2doGrado, text = "Calcular", command = Calcular)
btnCalcular.grid  (row = 3,column = 0, padx = 30, pady = 10, columnspan = 6)
btnCalcular.config (cursor = "hand2")

botonRegresar = Button(ventanaEcuaciones2doGrado, text = "Regresar", command = Regresar)
botonRegresar.grid (row = 5,column = 0, padx = 30, pady = 10)
botonRegresar.config (cursor = "hand2")

#---------------------------------- Fin me2doGrado -------------------------------------


ventanaEcuaciones2doGrado.mainloop ()
