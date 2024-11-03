from tkinter import *
from tkinter import messagebox

ventanaAlegebra = Tk()
ventanaAlegebra.geometry("200x300")
ventanaAlegebra.title("Sub Menu de Álgebra")
ventanaAlegebra.config(bg = "#248DFF") #color de fondo
miFrameAlgebra = Frame (ventanaAlegebra, width = 1200, height = 600)
miFrameAlgebra.pack ()
miFrameAlgebra.config(bg = "#248DFF") #color de fondo


#---------------------------------- Funciones --------------------------------------


def me2doGrado ():
    messagebox.showinfo("Ec. de 2do. grado", "En desarrollo")

def meNewtonRaphson ():
    messagebox.showinfo("Newton - Raphson", "En desarrollo")

def meBiseccion ():
    messagebox.showinfo("Bisección", "En desarrollo")


def Salir ():
    ventanaAlegebra.destroy()

#---------------------------------- Mensajes --------------------------------------

subMenuAlgebra = Label(miFrameAlgebra, text = "Sub Menu de Álgebra", font = ("Courier", 12))
subMenuAlgebra.grid (row = 0,column = 0)
subMenuAlgebra.config(bg = "#248DFF") #color de fondo


#---------------------------------- Botones --------------------------------------

boton2doGrado = Button(miFrameAlgebra, text = "Ec. de 2do. grado", command = me2doGrado) 
boton2doGrado.grid (row = 1,column = 0, padx = 30, pady = 10)
boton2doGrado.config (cursor = "hand2")

botonNewtonRaphson = Button(miFrameAlgebra, text = "Newton - Raphson",command = meNewtonRaphson)
botonNewtonRaphson.grid (row = 2,column = 0, padx = 30, pady = 10)
botonNewtonRaphson.config (cursor = "hand2")


botonBiseccion = Button(miFrameAlgebra, text = "Bisección", command = meBiseccion)
botonBiseccion.grid (row = 3,column = 0, padx = 30, pady = 10)
botonBiseccion.config (cursor = "hand2")


botonaSalir = Button(miFrameAlgebra, text = "Salir", command = Salir)
botonaSalir.grid (row = 4,column = 0, padx = 30, pady = 10)
botonaSalir.config (cursor = "hand2")







#---------------------------------- mainloop --------------------------------------

ventanaAlegebra.mainloop()