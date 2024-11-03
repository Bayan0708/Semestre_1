from tkinter import *
from math import *
import matplotlib.pyplot as plt


raiz = Tk()
raiz.title("Método Trapezoidal")

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
        lblMensaje.config(text = mensaje)              

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
        lblMensaje.config(text = mensaje)   
        #Se crean 2 listas que nos ayudan a gráficar.
        lista3 = lista
        lista3.insert(0,a)
        lista3.append (b)
        lista4 = lista2
        lista4.insert(0,0)
        lista4.append (0)

        #Datos de la gráfica.
        plt.plot (lista,lista2,'indigo')
        plt.fill(lista3 , lista4, 'darkviolet', alpha=0.5)
        plt.xlabel('Eje X') # Etiqueta del eje X
        plt.ylabel('Eje Y') # Etiqueta del eje Y
        plt.title("El área bajo la curva es de " + str(area))
        plt.grid() # se activa la malla
        plt.show() # Se manda crear la gráfica




def SalirTotal ():
    raiz.destroy()

def Regresar ():
    raiz.destroy()

#Textos


estructura = Label (raiz, text = "Este programa aproxima el área bajo la curva de intervalos de funciones, usando el Método Trapezoidal Compuesto", font = ("Courier", 14))
estructura.grid (row = 0,column = 0, padx = 30, pady = 10, columnspan = 4)

Trapezoidali1 = Label (raiz, text = "Antes de ingresar tu función, lee las siguientes especificaciones:",font = (14))
Trapezoidali1.grid (row = 1,column = 0, padx = 10, pady = 10, columnspan = 4)
Trapezoidali2 = Label (raiz, text = "1. Introduce funciones que el programa math pueda leer y revisa que estén bien escritas.      2. Revisa bien tu intervalo, ya que necesitamos continuidad en la función.      3. Toma en cuenta que tu función debe estar en función de x.")
Trapezoidali2.grid (row = 2,column = 0, padx = 10, pady = 10, columnspan = 4)

Trapezoidali5 = Label (raiz, text = "En caso de no cumplir con lo anterior, el programa tendrá un error o probablemente obtengamos un resultado erróneo.")
Trapezoidali5.grid (row = 3,column = 0, padx = 10, pady = 10, columnspan = 4)


Trapezoidalf = Label (raiz, text = "Dame la función:")
Trapezoidalf.grid (row = 4,column = 1, padx = 10, pady = 10)

Trapezoidala = Label (raiz, text = "Frontera inferior:")
Trapezoidala.grid (row = 5,column = 1, padx = 10, pady = 10)

Trapezoidalb = Label (raiz, text = "Frontera Superior:")
Trapezoidalb.grid (row = 6,column = 1, padx = 10, pady = 10)

Trapezoidaln = Label (raiz, text = "Número de intervalos:")
Trapezoidaln.grid (row = 7,column = 1, padx = 10, pady = 10)


# Colocamos entry para poder tener la entrada del usuario

Trapezoidalfun = Entry (raiz, justify = "center")
Trapezoidalfun.grid (row = 4,column = 2, padx = 10, pady = 10,)

Trapezoidala = Entry (raiz, justify = "center")
Trapezoidala.grid (row = 5,column = 2, padx = 10, pady = 10)

Trapezoidalb = Entry (raiz, justify = "center")
Trapezoidalb.grid (row = 6,column = 2, padx = 10, pady = 10)

Trapezoidaln = Entry (raiz, justify = "center")
Trapezoidaln.grid (row = 7,column = 2, padx = 10, pady = 10)



# Etiqueta para mostrar el mensaje

lblMensaje = Label (raiz)
lblMensaje.grid(row = 9,column = 0, padx = 30, pady = 10, columnspan = 6)

btnCalcular = Button (raiz, text = "Clacular", command = Calcular)
btnCalcular.grid  (row = 8,column = 0, padx = 30, pady = 10, columnspan = 6)
btnCalcular.config (cursor = "hand2")


botonSalirTotal = Button(raiz, text = "Salir", command = SalirTotal)
botonSalirTotal.grid (row = 10,column = 3, padx = 30, pady = 10)
botonSalirTotal.config (cursor = "hand2")

botonRegresar = Button(raiz, text = "Regresar", command = Regresar)
botonRegresar.grid (row = 10,column = 0, padx = 30, pady = 10)
botonRegresar.config (cursor = "hand2")


raiz.mainloop ()
