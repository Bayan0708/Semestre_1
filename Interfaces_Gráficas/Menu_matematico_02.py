'''
@author: Sebastián González Juárez
Universidad Nacional Autónoma de México 
Facultad de Ciencias
Computación
Programa de una interfaz gráfica con tkinter para hacer un menu matemático
'''

#Paquetería tkinter
from tkinter import *
from tkinter import messagebox

#---------------------------------- raiz --------------------------------------
Portada = Tk ()
Portada.title("Menu Matemático Sebastián González Juárez") #pone titulo
Portada.resizable(False,False) #ancho y alto (en 0,0 no nos dejara cambiar el tamaño de la ventana)
Portada.geometry("375x300") #tamaño de pestaña
Portada.config(bd = 20) #Tamaño del borde de la raiz
Portada.config (relief = "groove") #Estilo del borde de la raiz
Portada.config(bg = "#74E9A5") #color de fondo

#---------------------------------- Funciones en raiz --------------------------------------

def vMenuMate ():
    ventanaMenuMate = Toplevel()
    ventanaMenuMate.geometry("650x350")
    ventanaMenuMate.title("Menu Matemático Sebastián González Juárez")
    ventanaMenuMate.config(bd = 20) #Tamaño del borde de la raiz
    ventanaMenuMate.config (relief = "groove") #Estilo del borde de la raiz
    #ventanaMenuMate.config(bg = "#FF4141") #color de fondo
    miMenuMate = Frame (ventanaMenuMate, width = 1200, height = 600)
    miMenuMate.pack ()
    #miMenuMate.config(bg = "#FF4141") #color de fondo

    #---------------------------------- Funciones --------------------------------------

    #---------------------------------- Funcion Algebra --------------------------------------
    def vAlgebra ():
        ventanaAlegebra = Toplevel()
        ventanaAlegebra.geometry("300x300")
        ventanaAlegebra.title("Sub Menu de Álgebra")
        ventanaAlegebra.config(bg = "#248DFF") #color de fondo
        miFrameAlgebra = Frame (ventanaAlegebra, width = 1200, height = 600)
        miFrameAlgebra.pack ()
        miFrameAlgebra.config(bg = "#248DFF") #color de fondo

        #---------------------------------- Funciones Algebra --------------------------------------
        def me2doGrado ():
            messagebox.showinfo("Ec. de 2do. grado", "En desarrollo")

        def meNewtonRaphson ():
            messagebox.showinfo("Newton - Raphson", "En desarrollo")

        def meBiseccion ():
            messagebox.showinfo("Bisección", "En desarrollo")


        def SalirSubMenuAlgebra ():
            ventanaAlegebra.destroy()

        def SalirTotal ():
            Portada.destroy()

        #---------------------------------- Mensajes Algebra--------------------------------------

        subMenuAlgebra = Label(miFrameAlgebra, text = "Sub Menu de Álgebra", font = ("Courier", 12))
        subMenuAlgebra.grid (row = 0,column = 0)
        subMenuAlgebra.config(bg = "#248DFF") #color de fondo

        #---------------------------------- Botones Algebra--------------------------------------

        boton2doGrado = Button(miFrameAlgebra, text = "Ec. de 2do. grado", command = me2doGrado) 
        boton2doGrado.grid (row = 1,column = 0, padx = 30, pady = 10)
        boton2doGrado.config (cursor = "hand2")

        botonNewtonRaphson = Button(miFrameAlgebra, text = "Newton - Raphson",command = meNewtonRaphson)
        botonNewtonRaphson.grid (row = 2,column = 0, padx = 30, pady = 10)
        botonNewtonRaphson.config (cursor = "hand2")


        botonBiseccion = Button(miFrameAlgebra, text = "Bisección", command = meBiseccion)
        botonBiseccion.grid (row = 3,column = 0, padx = 30, pady = 10)
        botonBiseccion.config (cursor = "hand2")


        botonSalirSubMenuAlgebra = Button(miFrameAlgebra, text = "Regresar", command = SalirSubMenuAlgebra)
        botonSalirSubMenuAlgebra.grid (row = 4,column = 0, padx = 30, pady = 10)
        botonSalirSubMenuAlgebra.config (cursor = "hand2")

        botonSalirTotal = Button(miFrameAlgebra, text = "Salir", command = SalirTotal)
        botonSalirTotal.grid (row = 5,column = 0, padx = 30, pady = 10)
        botonSalirTotal.config (cursor = "hand2")


    #---------------------------------- Funcion Calculo --------------------------------------
    def vCalculoIntegral ():
        ventanaCalculoIntegral = Toplevel()
        ventanaCalculoIntegral.geometry("300x300")
        ventanaCalculoIntegral.title("Sub Menu de Cálculo")
        ventanaCalculoIntegral.config(bg = "#248DFF") #color de fondo
        miFrameCalculoIntegral = Frame (ventanaCalculoIntegral, width = 1200, height = 600)
        miFrameCalculoIntegral.pack ()
        miFrameCalculoIntegral.config(bg = "#248DFF") #color de fondo

        #---------------------------------- Funciones Calculo --------------------------------------
        def meTrapezoidalCompuesto ():
            messagebox.showinfo("Trapezoidal Compuesto", "En desarrollo")

        def meSimpson1 ():
            messagebox.showinfo("Simpson 1/3", "En desarrollo")

        def meSimpson3 ():
            messagebox.showinfo("Simpson 3/8", "En desarrollo")


        def SalirSubMenuCalculoIntegral ():
            ventanaCalculoIntegral.destroy()

        def SalirTotal ():
            Portada.destroy()

        #---------------------------------- Mensajes Calculo --------------------------------------

        subMenuAlgebra = Label(miFrameCalculoIntegral, text = "Sub Menu de Cálculo Integral", font = ("Courier", 12))
        subMenuAlgebra.grid (row = 0,column = 0)
        subMenuAlgebra.config(bg = "#248DFF") #color de fondo

        #---------------------------------- Botones Calculo --------------------------------------

        botonTrapezoidalCompuesto = Button(miFrameCalculoIntegral, text = "Trapezoidal Compuesto", command = meTrapezoidalCompuesto) 
        botonTrapezoidalCompuesto.grid (row = 1,column = 0, padx = 30, pady = 10)
        botonTrapezoidalCompuesto.config (cursor = "hand2")

        botonSimpson1 = Button(miFrameCalculoIntegral, text = "Simpson 1/3",command = meSimpson1)
        botonSimpson1.grid (row = 2,column = 0, padx = 30, pady = 10)
        botonSimpson1.config (cursor = "hand2")


        botonSimpson3 = Button(miFrameCalculoIntegral, text = "Simpson 3/8", command = meSimpson3)
        botonSimpson3.grid (row = 3,column = 0, padx = 30, pady = 10)
        botonSimpson3.config (cursor = "hand2")


        botonSalirSubMenuAlgebra = Button(miFrameCalculoIntegral, text = "Regresar", command = SalirSubMenuCalculoIntegral)
        botonSalirSubMenuAlgebra.grid (row = 4,column = 0, padx = 30, pady = 10)
        botonSalirSubMenuAlgebra.config (cursor = "hand2")

        botonSalirTotal = Button(miFrameCalculoIntegral, text = "Salir", command = SalirTotal)
        botonSalirTotal.grid (row = 5,column = 0, padx = 30, pady = 10)
        botonSalirTotal.config (cursor = "hand2")

    #---------------------------------- Funcion Algebra Lineal --------------------------------------

    def vAlgebraLineal ():
        ventanaAlegebraLineal = Toplevel()
        ventanaAlegebraLineal.geometry("300x300")
        ventanaAlegebraLineal.title("Sub Menu de Álgebra Lineal")
        ventanaAlegebraLineal.config(bg = "#248DFF") #color de fondo
        miFrameAlegebraLineal = Frame (ventanaAlegebraLineal, width = 1200, height = 600)
        miFrameAlegebraLineal.pack ()
        miFrameAlegebraLineal.config(bg = "#248DFF") #color de fondo

        #---------------------------------- Funciones Algebra Lineal --------------------------------------
        def meVectores ():
            messagebox.showinfo("Trapezoidal Compuesto", "En desarrollo")

        def meMatrices ():
            messagebox.showinfo("Simpson 1/3", "En desarrollo")

        def meSistemaEcuaciones ():
            messagebox.showinfo("Simpson 3/8", "En desarrollo")


        def SalirSubMenuAlgebraLineal ():
            ventanaAlegebraLineal.destroy()

        def SalirTotal ():
            Portada.destroy()

        #---------------------------------- Mensajes Algebra Lineal --------------------------------------

        subMenuAlgebraLineal = Label(miFrameAlegebraLineal, text = "Sub Menu de Álgebra Lineal", font = ("Courier", 12))
        subMenuAlgebraLineal.grid (row = 0,column = 0)
        subMenuAlgebraLineal.config(bg = "#248DFF") #color de fondo

        #---------------------------------- Botones Algebra Lineal --------------------------------------

        botonVectores = Button(miFrameAlegebraLineal, text = "Vectores", command = meVectores) 
        botonVectores.grid (row = 1,column = 0, padx = 30, pady = 10)
        botonVectores.config (cursor = "hand2")

        botonMatrices = Button(miFrameAlegebraLineal, text = "Matrices",command = meMatrices)
        botonMatrices.grid (row = 2,column = 0, padx = 30, pady = 10)
        botonMatrices.config (cursor = "hand2")


        botonSistemaEcuaciones = Button(miFrameAlegebraLineal, text = "Sistema de Ecuaciones", command = meSistemaEcuaciones)
        botonSistemaEcuaciones.grid (row = 3,column = 0, padx = 30, pady = 10)
        botonSistemaEcuaciones.config (cursor = "hand2")


        botonSalirSubMenuAlgebra = Button(miFrameAlegebraLineal, text = "Regresar", command = SalirSubMenuAlgebraLineal)
        botonSalirSubMenuAlgebra.grid (row = 4,column = 0, padx = 30, pady = 10)
        botonSalirSubMenuAlgebra.config (cursor = "hand2")

        botonSalirTotal = Button(miFrameAlegebraLineal, text = "Salir", command = SalirTotal)
        botonSalirTotal.grid (row = 5,column = 0, padx = 30, pady = 10)
        botonSalirTotal.config (cursor = "hand2")




    #---------------------------------- Funcion Estadistica --------------------------------------
    def vEstadistica ():
        ventanaEstadistica = Toplevel()
        ventanaEstadistica.geometry("300x300")
        ventanaEstadistica.title("Sub Menu de Álgebra Lineal")
        ventanaEstadistica.config(bg = "#248DFF") #color de fondo
        miFrameEstadistica = Frame (ventanaEstadistica, width = 1200, height = 600)
        miFrameEstadistica.pack ()
        miFrameEstadistica.config(bg = "#248DFF") #color de fondo

        #---------------------------------- Funciones Estadistica --------------------------------------
        def meMedia ():
            messagebox.showinfo("Media", "En desarrollo")

        def meDesviacion ():
            messagebox.showinfo("Desviación", "En desarrollo")

        def mePercil ():
            messagebox.showinfo("Simpson 3/8", "En desarrollo")


        def SalirSubMenuEstadistica ():
            ventanaEstadistica.destroy()

        def SalirTotal ():
            Portada.destroy()

        #---------------------------------- Mensajes Estadistica --------------------------------------

        subMenuEstadistica = Label(miFrameEstadistica, text = "Sub Menu de Estadística", font = ("Courier", 12))
        subMenuEstadistica.grid (row = 0,column = 0)
        subMenuEstadistica.config(bg = "#248DFF") #color de fondo

        #---------------------------------- Botones Estadistica --------------------------------------

        botonMedia = Button(miFrameEstadistica, text = "Media", command = meMedia) 
        botonMedia.grid (row = 1,column = 0, padx = 30, pady = 10)
        botonMedia.config (cursor = "hand2")

        botonDesviacion = Button(miFrameEstadistica, text = "Percíl",command = meDesviacion)
        botonDesviacion.grid (row = 2,column = 0, padx = 30, pady = 10)
        botonDesviacion.config (cursor = "hand2")


        botonPercil = Button(miFrameEstadistica, text = "Percíl", command = mePercil)
        botonPercil.grid (row = 3,column = 0, padx = 30, pady = 10)
        botonPercil.config (cursor = "hand2")


        botonSalirSubMenuAlgebra = Button(miFrameEstadistica, text = "Regresar", command = SalirSubMenuEstadistica)
        botonSalirSubMenuAlgebra.grid (row = 4,column = 0, padx = 30, pady = 10)
        botonSalirSubMenuAlgebra.config (cursor = "hand2")

        botonSalirTotal = Button(miFrameEstadistica, text = "Salir", command = SalirTotal)
        botonSalirTotal.grid (row = 5,column = 0, padx = 30, pady = 10)
        botonSalirTotal.config (cursor = "hand2")



    #---------------------------------- Funcion Salir --------------------------------------

    def SalirTotal ():
        Portada.destroy()

    #---------------------------------- Mensajes --------------------------------------
    Bienvenidos = Label(miMenuMate, text = "¡Bienvenidos al menu matemático!", font = ("Comic Sans MS", 24))
    Bienvenidos.grid (row = 0,column = 0,columnspan = 4)
    #Bienvenidos.config(bg = "#FF4141") #color de fondo
    Hacer = Label(miMenuMate, text = "¿Qué deseas hacer?", font = ("Courier", 12))
    Hacer.grid (row = 1,column = 0,columnspan = 4)
    #Hacer.config(bg = "#FF4141") #color de fondo


    #---------------------------------- Botones --------------------------------------
    botonAlgebra = Button(miMenuMate, text = "Álgebra", command = vAlgebra) #Ponemos un Label
    botonAlgebra.grid (row = 2,column = 0, padx = 30, pady = 10) #Ubicamos el label
    botonAlgebra.config (cursor = "hand2")

    botonCalculoIntegral = Button(miMenuMate, text = "Cálculo Integral", command = vCalculoIntegral)
    botonCalculoIntegral.grid (row = 2,column = 1, padx = 30, pady = 10)
    botonCalculoIntegral.config (cursor = "hand2")


    botonAlgebraLineal = Button(miMenuMate, text = "Álgebra Lineal", command = vAlgebraLineal)
    botonAlgebraLineal.grid (row = 2,column = 2, padx = 30, pady = 10)
    botonAlgebraLineal.config (cursor = "hand2")


    botonEstadistica = Button(miMenuMate, text = "Estadística", command = vEstadistica)
    botonEstadistica.grid (row = 2,column = 3, padx = 30, pady = 10)
    botonEstadistica.config (cursor = "hand2")

    botonSalirTotal = Button(miMenuMate, text = "Salir", command = SalirTotal)
    botonSalirTotal.grid (row = 5,column = 0, padx = 30, pady = 10,columnspan = 4)
    botonSalirTotal.config (cursor = "hand2")



#---------------------------------- Textos en raiz --------------------------------------

Bienvenidos = Label(Portada, text = "Menu Matemático", font = ("Comic Sans MS", 24))
Bienvenidos.grid (row = 0,column = 0)
Bienvenidos.config(bg = "#74E9A5", padx = 30, pady = 30) #color de fondo
Nombre = Label(Portada, text = "Sebastián González Juárez", font = ("Courier", 12))
Nombre.grid (row = 1,column = 0, padx = 30, pady = 10)
Nombre.config(bg = "#74E9A5") #color de fondo
Escuela = Label(Portada, text = "UNAM - Facultad de Ciencias", font = ("Courier", 12))
Escuela.grid (row = 2,column = 0)
Escuela.config(bg = "#74E9A5") #color de fondo
Materia = Label(Portada, text = "Cómputo", font = ("Courier", 12))
Materia.grid (row = 3,column = 0, padx = 30, pady = 10)
Materia.config(bg = "#74E9A5") #color de fondo


#---------------------------------- Botones raiz --------------------------------------

botonEstadistica = Button(Portada, text = "Iniciar", command = vMenuMate)
botonEstadistica.grid (row = 4,column = 0, padx = 30, pady = 10)
botonEstadistica.config (cursor = "hand2")

#---------------------------------- mainloop --------------------------------------
Portada.mainloop()