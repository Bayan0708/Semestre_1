#Hacer el menu matematico

from tkinter import *
from tkinter import messagebox


raiz = Tk ()
raiz.title("Menu Matemático Sebastián González Juárez") #pone titulo
raiz.resizable(True,True) #ancho y alto (en 0,0 no nos dejara cambiar el tamaño de la ventana)
raiz.geometry("650x350") #tamaño de pestaña
raiz.config(bd = 20) #Tamaño del borde de la raiz
raiz.config (relief = "groove") #Estilo del borde de la raiz


#---------------------------------- Funciones --------------------------------------


def vAlgebra ():
    ventanaAlegebra = Toplevel()
    ventanaAlegebra.geometry("400x400")
    ventanaAlegebra.title("Sub Menu de Álgebra")
    miFrameAlgebra = Frame (ventanaAlegebra, width = 1200, height = 600)
    miFrameAlgebra.pack ()
    boton2=Button(miFrameAlgebra,text="Aceptar").pack()



def vCalculoIntegral ():
    ventanaCalculoIntegral = Toplevel()
    ventanaCalculoIntegral.geometry("400x400")
    ventanaCalculoIntegral.title("Sub Menu de Cálculo Integral")

def vAlgebraLineal ():
    ventanaAlegebraLineal = Toplevel()
    ventanaAlegebraLineal.geometry("400x400")
    ventanaAlegebraLineal.title("Sub Menu de Álgebra Lineal")

def vEstadistica ():
    ventanaAlegebra = Toplevel()
    ventanaAlegebra.geometry("400x400")
    ventanaAlegebra.title("Bienvenido otra vez")



#---------------------------------- Mi Frame --------------------------------------

miFrame = Frame (raiz, width = 1200, height = 600)
miFrame.pack ()


#---------------------------------- Mensajes --------------------------------------

Bienvenidos = Label(miFrame, text = "¡Bienvenidos al menu matemático!", font = ("Comic Sans MS", 24))
Bienvenidos.grid (row = 0,column = 0,columnspan = 4)

Hacer = Label(miFrame, text = "¿Que deseas hacer?", font = ("Courier", 12))
Hacer.grid (row = 1,column = 0,columnspan = 4)


#---------------------------------- Botones --------------------------------------

botonAlgebra = Button(miFrame, text = "Álgebra", command = vAlgebra) #Ponemos un Label
botonAlgebra.grid (row = 2,column = 0, sticky = "e", padx = 30, pady = 10) #Ubicamos el label
botonAlgebra.config (cursor = "hand2")

botonCalculoIntegral = Button(miFrame, text = "Cálculo Integral", command = vCalculoIntegral)
botonCalculoIntegral.grid (row = 2,column = 1,sticky = "e", padx = 30, pady = 10)
botonCalculoIntegral.config (cursor = "hand2")


botonAlgebraLineal = Button(miFrame, text = "Álgebra Lineal", command = vAlgebraLineal)
botonAlgebraLineal.grid (row = 2,column = 2,sticky = "e", padx = 30, pady = 10)
botonAlgebraLineal.config (cursor = "hand2")


botonEstadistica = Button(miFrame, text = "Estadística", command = vEstadistica)
botonEstadistica.grid (row = 2,column = 3,sticky = "e", padx = 30, pady = 10)
botonEstadistica.config (cursor = "hand2")

#---------------------------------- mainloop --------------------------------------

foto = PhotoImage (file = "Semestre_01\Foto_python.png")
Label (raiz, image = foto).pack()



#---------------------------------- mainloop --------------------------------------

raiz.mainloop()