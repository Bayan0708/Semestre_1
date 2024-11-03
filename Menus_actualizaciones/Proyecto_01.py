'''
@author: Sebastián González Juárez
Universidad Nacional Autónoma de México 
Facultad de Ciencias
Computación
Programa de una interfaz gráfica con tkinter para hacer un menu matemático
'''

#---------------------------------- Paqueterías --------------------------------------

#Paquetería tkinter, permite hacer el interfaz
from tkinter import *
from tkinter import messagebox


#Paquetería math, permite hacer operaciones y demás funciones matemáticas
from math import *

#Paquetería matplotlib, permite gráficar
import matplotlib.pyplot as plt



#---------------------------------- Portada --------------------------------------
Portada = Tk ()
Portada.title("Menu Matemático Sebastián González Juárez") #pone titulo
Portada.resizable(False,False) #ancho y alto (en 0,0 no nos dejara cambiar el tamaño de la ventana)
Portada.geometry("375x300") #tamaño de pestaña
Portada.config(bd = 20) #Tamaño del borde de la raiz
Portada.config (relief = "groove") #Estilo del borde de la raiz
Portada.config(bg = "#74E9A5") #color de fondo

#---------------------------------- Funciones en Portada --------------------------------------

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

    #---------------------------------- Funciones Menu Mate--------------------------------------

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

            ventanaEcuaciones2doGrado = Tk()
            ventanaEcuaciones2doGrado.title("Ecuaciones 2do Grado")


            #---------------------------------- Funciones me2doGrado -------------------------------------

            def Calcular ():
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
                        else:
                            x1 = (-b + (discriminante**0.5)) / (2 * a)
                            x2 = (-b - (discriminante**0.5)) / (2 * a)
                            mensaje = "Las raíces reales son: x1 = {:.3f}".format(x1) + "   y   " + "x2 = {:.3f}".format(x2)
                            MensaEcuaciones2doGrado.config(text = mensaje)
                    else:
                        discriminante = abs(discriminante)
                        parteReal = -b / (2 * a)
                        parteImaginaria =(discriminante**0.5) / (2 * a)
                        mensaje = "Las raíces complejas son: x1 = {:.3f} + {:.3f}i".format(parteReal, parteImaginaria) + "   y   " + "x2 = {:.3f} - {:.3f}i".format(parteReal, parteImaginaria)
                        MensaEcuaciones2doGrado.config(text = mensaje)          

            def Regresar ():
                ventanaEcuaciones2doGrado.destroy()

            #---------------------------------- Textos me2doGrado -------------------------------------

            estructura = Label (ventanaEcuaciones2doGrado, text = "Este programa encuentra las raíces de ecuaciones con la forma: ax^2+bx+c", font = ("Courier", 11))
            estructura.grid (row = 0,column = 0, padx = 30, pady = 10, columnspan = 6)

            Primero = Label (ventanaEcuaciones2doGrado, text = "Coeficiente a:")
            Primero.grid (row = 1,column = 0, padx = 10, pady = 10)


            Segundo = Label (ventanaEcuaciones2doGrado, text = "Coeficiente b:")
            Segundo.grid (row = 1,column = 2, padx = 10, pady = 10)

            Tercero = Label (ventanaEcuaciones2doGrado, text = "Coeficiente c:")
            Tercero.grid (row = 1,column = 4, padx = 10, pady = 10)


            #---------------------------------- Entradas me2doGrado -------------------------------------
            # Colocamos entry para poder tener la entrada del usuario

            coeficientea = Entry (ventanaEcuaciones2doGrado, justify = "center")
            coeficientea.grid (row = 1,column = 1, padx = 10, pady = 10,)

            coeficienteb = Entry (ventanaEcuaciones2doGrado, justify = "center")
            coeficienteb.grid (row = 1,column = 3, padx = 10, pady = 10)

            coeficientec = Entry (ventanaEcuaciones2doGrado, justify = "center")
            coeficientec.grid (row = 1,column = 5, padx = 10, pady = 10)

            #---------------------------------- Salidas me2doGrado -------------------------------------
            # Etiqueta para mostrar el mensaje

            MensaEcuaciones2doGrado = Label (ventanaEcuaciones2doGrado)
            MensaEcuaciones2doGrado.grid(row = 3,column = 0, padx = 30, pady = 10, columnspan = 6)

            #---------------------------------- Botones me2doGrado -------------------------------------

            btnCalcular = Button (ventanaEcuaciones2doGrado, text = "Calcular", command = Calcular)
            btnCalcular.grid  (row = 2,column = 0, padx = 30, pady = 10, columnspan = 6)
            btnCalcular.config (cursor = "hand2")

            botonRegresar = Button(ventanaEcuaciones2doGrado, text = "Regresar", command = Regresar)
            botonRegresar.grid (row = 4,column = 0, padx = 30, pady = 10)
            botonRegresar.config (cursor = "hand2")

            #---------------------------------- Fin me2doGrado -------------------------------------


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
        ventanaCalculoIntegral.config(bg = "#FF5151") #color de fondo
        miFrameCalculoIntegral = Frame (ventanaCalculoIntegral, width = 1200, height = 600)
        miFrameCalculoIntegral.pack ()
        miFrameCalculoIntegral.config(bg = "#FF5151") #color de fondo

        #---------------------------------- Funciones Calculo --------------------------------------
        def meTrapezoidalCompuesto ():
            ventanaMetodoTrapezoidal = Tk()
            ventanaMetodoTrapezoidal.title("Método Trapezoidal")
            #Funciones
            def Calcular ():
                
                def funcion_Replace_Eval(x):
                    remplazo = f.replace("x", str(x))
                    resultado = eval(remplazo)
                    return resultado
                
                f = (Trapezoidalfun.get())
                a = float (Trapezoidala.get())
                b = float (Trapezoidalb.get())
                n = int (Trapezoidaln.get())
            
                h = (b - a) / n

                if a > b:
                    mensaje = "El valor de la frontera inferior debe ser menor o igual que el valor de la frontera superior, introduce nuevamente tus datos"
                    MensajeMetodoTrapezoidal.config(text = mensaje)              

                else:
                    #Se crea una lista donde se metan los valores de x.
                    lista = []
                    aux = a
                    for i in range(0, n + 1):
                        lista.append(aux)
                        aux = aux + h

                    #Se crea una lista donde se metan los valores de y.
                    lista2 = []
                    for i in lista:
                        valor = funcion_Replace_Eval(i)
                        lista2.append(valor)

                    #Se incia una suma de la lista 2.
                    suma = 0
                    for i in range(1, len(lista2)-1):
                        suma += lista2[i]

                    #Calculo del área bajo la curva, usa la fórmula.
                    area = (h / 2) * (lista2[0] + (suma * 2) + lista2[-1])
                    mensaje = "El área bajo la curva es de " + str(area)
                    MensajeMetodoTrapezoidal.config(text = mensaje)   
                    #Se crean 2 listas que nos ayudan a gráficar.
                    lista3 = lista
                    lista3.insert(0,a)
                    lista3.append (b)
                    lista4 = lista2
                    lista4.insert(0,0)
                    lista4.append (0)

            #---------------------------------- Datos de la gráfica Método Trapezoidal -----------------

                    #Creamos la gráfica
                    plt.plot (lista,lista2,'indigo')
                    plt.fill(lista3 , lista4, 'darkviolet', alpha=0.5)
                    plt.xlabel('Eje X') # Etiqueta del eje X
                    plt.ylabel('Eje Y') # Etiqueta del eje Y
                    plt.title("El área bajo la curva es de " + str(area))
                    plt.grid() # se activa la malla
                    plt.show() # Se manda crear la gráfica

            def Regresar ():
                ventanaMetodoTrapezoidal.destroy()

            #Textos

            #---------------------------------- Textos Método Trapezoidal -------------------------------------

            estructura = Label (ventanaMetodoTrapezoidal, text = "Este programa aproxima el área bajo la curva de intervalos de funciones, usando el Método Trapezoidal Compuesto", font = ("Courier", 14))
            estructura.grid (row = 0,column = 0, padx = 30, pady = 10, columnspan = 4)

            Trapezoidali1 = Label (ventanaMetodoTrapezoidal, text = "Antes de ingresar tu función, lee las siguientes especificaciones:",font = (14))
            Trapezoidali1.grid (row = 1,column = 0, padx = 10, pady = 10, columnspan = 4)
            Trapezoidali2 = Label (ventanaMetodoTrapezoidal, text = "1. Introduce funciones que el programa math pueda leer y revisa que estén bien escritas.      2. Revisa bien tu intervalo, ya que necesitamos continuidad en la función.      3. Toma en cuenta que tu función debe estar en función de x.")
            Trapezoidali2.grid (row = 2,column = 0, padx = 10, pady = 10, columnspan = 4)

            Trapezoidali5 = Label (ventanaMetodoTrapezoidal, text = "En caso de no cumplir con lo anterior, el programa tendrá un error o probablemente obtengamos un resultado erróneo.")
            Trapezoidali5.grid (row = 3,column = 0, padx = 10, pady = 10, columnspan = 4)


            Trapezoidalf = Label (ventanaMetodoTrapezoidal, text = "Dame la función:")
            Trapezoidalf.grid (row = 4,column = 1, padx = 10, pady = 10)

            Trapezoidala = Label (ventanaMetodoTrapezoidal, text = "Frontera Inferior:")
            Trapezoidala.grid (row = 5,column = 1, padx = 10, pady = 10)

            Trapezoidalb = Label (ventanaMetodoTrapezoidal, text = "Frontera Superior:")
            Trapezoidalb.grid (row = 6,column = 1, padx = 10, pady = 10)

            Trapezoidaln = Label (ventanaMetodoTrapezoidal, text = "Número de intervalos:")
            Trapezoidaln.grid (row = 7,column = 1, padx = 10, pady = 10)

            Trapezoidalg = Label (ventanaMetodoTrapezoidal, text = "Una vez graficada la función, deberás regresar al menú para poder graficar otra.")
            Trapezoidalg.grid (row = 11,column = 1, padx = 10, pady = 10)


            #---------------------------------- Entradas Método Trapezoidal -------------------------------------
            # Colocamos entry para poder tener la entrada del usuario

            Trapezoidalfun = Entry (ventanaMetodoTrapezoidal, justify = "center")
            Trapezoidalfun.grid (row = 4,column = 2, padx = 10, pady = 10,)

            Trapezoidala = Entry (ventanaMetodoTrapezoidal, justify = "center")
            Trapezoidala.grid (row = 5,column = 2, padx = 10, pady = 10)

            Trapezoidalb = Entry (ventanaMetodoTrapezoidal, justify = "center")
            Trapezoidalb.grid (row = 6,column = 2, padx = 10, pady = 10)

            Trapezoidaln = Entry (ventanaMetodoTrapezoidal, justify = "center")
            Trapezoidaln.grid (row = 7,column = 2, padx = 10, pady = 10)


            #---------------------------------- Salidas Método Trapezoidal -------------------------------------
            # Etiqueta para mostrar el mensaje

            MensajeMetodoTrapezoidal = Label (ventanaMetodoTrapezoidal)
            MensajeMetodoTrapezoidal.grid(row = 9,column = 0, padx = 30, pady = 10, columnspan = 6)

            #---------------------------------- Botones Método Trapezoidal -------------------------------------

            btnCalcular = Button (ventanaMetodoTrapezoidal, text = "Calcular", command = Calcular)
            btnCalcular.grid  (row = 8,column = 0, padx = 30, pady = 10, columnspan = 6)
            btnCalcular.config (cursor = "hand2")


            botonRegresar = Button(ventanaMetodoTrapezoidal, text = "Regresar", command = Regresar)
            botonRegresar.grid (row = 10,column = 0, padx = 30, pady = 10)
            botonRegresar.config (cursor = "hand2")

            #---------------------------------- Fin Método Trapezoidal -------------------------------------


        def meSimpson1 ():
            messagebox.showinfo("Simpson 1/3", "En desarrollo")

        def meSimpson3 ():
            messagebox.showinfo("Simpson 3/8", "En desarrollo")


        def SalirSubMenuCalculoIntegral ():
            ventanaCalculoIntegral.destroy()


        #---------------------------------- Mensajes Calculo --------------------------------------

        subMenuAlgebra = Label(miFrameCalculoIntegral, text = "Sub Menu de Cálculo Integral", font = ("Courier", 12))
        subMenuAlgebra.grid (row = 0,column = 0)
        subMenuAlgebra.config(bg = "#FF5151") #color de fondo

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
        ventanaAlegebraLineal.config(bg = "#EE71FF") #color de fondo
        miFrameAlegebraLineal = Frame (ventanaAlegebraLineal, width = 1200, height = 600)
        miFrameAlegebraLineal.pack ()
        miFrameAlegebraLineal.config(bg = "#EE71FF") #color de fondo

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
        subMenuAlgebraLineal.config(bg = "#EE71FF") #color de fondo

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
        ventanaEstadistica.config(bg = "#FFF490") #color de fondo
        miFrameEstadistica = Frame (ventanaEstadistica, width = 1200, height = 600)
        miFrameEstadistica.pack ()
        miFrameEstadistica.config(bg = "#FFF490") #color de fondo

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
        subMenuEstadistica.config(bg = "#FFF490") #color de fondo

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

    #---------------------------------- Mensajes Menu Mate --------------------------------------
    Bienvenidos = Label(miMenuMate, text = "¡Bienvenidos al menu matemático!", font = ("Comic Sans MS", 24))
    Bienvenidos.grid (row = 0,column = 0,columnspan = 4)
    #Bienvenidos.config(bg = "#FF4141") #color de fondo
    Hacer = Label(miMenuMate, text = "¿Qué deseas hacer?", font = ("Courier", 12))
    Hacer.grid (row = 1,column = 0,columnspan = 4)
    #Hacer.config(bg = "#FF4141") #color de fondo


    #---------------------------------- Botones Menu Mate --------------------------------------
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



#---------------------------------- Textos en Portada --------------------------------------

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


#---------------------------------- Botones Portada --------------------------------------

botonEstadistica = Button(Portada, text = "Iniciar", command = vMenuMate)
botonEstadistica.grid (row = 4,column = 0, padx = 30, pady = 10)
botonEstadistica.config (cursor = "hand2")

#---------------------------------- mainloop --------------------------------------
Portada.mainloop()