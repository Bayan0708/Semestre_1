from tkinter import *
from tkinter import messagebox
from math import *
import matplotlib.pyplot as plt
import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure



ventanaMetodoSimpson1 = Tk()
ventanaMetodoSimpson1.title("Método Simpson 1/3")

#Funciones


def Calcular ():
    
    def evaluando_copia_f (x):
        copia_f=f.copy()
        for i in range(len(copia_f)):
            if copia_f[i]=="x":
                copia_f[i]==x
        return eval("".join(copia_f))


    f = list(Simpsonfun.get())

    a = float (Simpsona.get())

    b = float (Simpsonb.get())

    n = int (Simpsonn.get())
        
    h = (b - a) / n

    x3 = float(xinicial.get())
    x4 = float(xfinal.get())
    y1 = float(yinicial.get())
    y2 = float(yfinal.get())

    if b > a and n>0 and n%2==0:
        Resultado = 0
        Resultado+=evaluando_copia_f(a)*(h/3)+evaluando_copia_f(b)*(h/3)
        for i in range(1,n):
            x=a+i*h
            if i%2==0:
                Resultado+=evaluando_copia_f(x)*(2*h/3)
            else:
                Resultado+=evaluando_copia_f(x)*(4*h/3)
        mensaje = "El área bajo la curva es de " + str(Resultado)
        MensajeMetodoSimpson1.config(text = mensaje)

    else:
        mensaje = "El valor de la frontera inferior debe ser menor o igual que el valor de la frontera superior y n debe ser mayor a cero y par, introduce nuevamente tus datos o vuelve a empezar"
        MensajeMetodoSimpson1.config(text = mensaje) 

    #Se crea una lista donde se metan los valores de x.
    lista = []
    aux = a
    for i in range(0, n + 1):
        lista.append(aux)
        aux = aux + h
    #Se crea una lista donde se metan los valores de y.
    lista2 = []
    for i in lista:
        valor = evaluando_copia_f(i)
        lista2.append(valor)
    #Se crean 2 listas que nos ayudan a gráficar.
    lista3 = lista
    lista3.insert(0,a)
    lista3.append (b)
    lista4 = lista2
    lista4.insert(0,0)
    lista4.append (0)


    #n = 100
    m = (x4-x3)/n
    listax = []
    listay = []
    for k in range (n+1):
        x4 = x3 + m*k
        listax.append (x4)
        listay.append (evaluando_copia_f(x4))


    #---------------------------------- Datos de la gráfica Metodo Simpson 1/3 -----------------
    figura = Figure()
    subfigura = figura.add_subplot (111)
    subfigura.set(xlabel = 'Eje X', ylabel = 'Eje Y', title = "Función y área debajo de la curva")
    subfigura.plot (listax,listay,'indigo')
    subfigura.fill(lista3 , lista4, 'darkviolet', alpha=0.5)
    subfigura.legend ()
    subfigura.grid ()
    subfigura.set_ylim(y1,y2)
    canvas = FigureCanvasTkAgg (figura, master = ventanaMetodoSimpson1)
    canvas.get_tk_widget().grid(row = 5, column = 0, padx = 5, pady = 5, sticky = "nsew", columnspan = 10)
    canvas.draw ()
    toolbar = NavigationToolbar2Tk(canvas, ventanaMetodoSimpson1, pack_toolbar=False)
    toolbar.grid(row=6, column=0, padx=6, pady=5, sticky="nsew", columnspan=12)



def Regresar ():
    ventanaMetodoSimpson1.destroy()

#Textos

#---------------------------------- Textos Método Simpson 1/3 -------------------------------------
Simpsonestructura = Label (ventanaMetodoSimpson1, text = "Este programa aproxima el área bajo la curva de intervalos de funciones, usando el Método Simpson 1/3 Compuesto", font = ("Courier", 14))
Simpsonestructura.grid (row = 0,column = 0, padx = 30, pady = 10, columnspan = 8)

Simpsonfl = Label (ventanaMetodoSimpson1, text = "Dame la función:")
Simpsonfl.grid (row = 1,column = 0, padx = 10, pady = 10)

Simpsonal= Label (ventanaMetodoSimpson1, text = "Frontera inferior:")
Simpsonal.grid (row = 1,column = 2, padx = 10, pady = 10)

Simpsonabl = Label (ventanaMetodoSimpson1, text = "Frontera Superior:")
Simpsonabl.grid (row = 1,column = 4, padx = 10, pady = 10)

Simpsonanl= Label (ventanaMetodoSimpson1, text = "Número de intervalos:")
Simpsonanl.grid (row = 1,column = 6, padx = 10, pady = 10)

MetodoSimpson1_x_i = Label (ventanaMetodoSimpson1, text = "-x: ")
MetodoSimpson1_x_i.grid (row = 2,column = 0, padx = 10, pady = 10)

MetodoSimpson1_x_f = Label (ventanaMetodoSimpson1, text = "x:")
MetodoSimpson1_x_f.grid (row = 2,column = 2, padx = 10, pady = 10)

MetodoSimpson1_y_i = Label (ventanaMetodoSimpson1, text = "-y: ")
MetodoSimpson1_y_i.grid (row = 2,column = 4, padx = 10, pady = 10)

Me2doGrado_y_f = Label (ventanaMetodoSimpson1, text = "y: ")
Me2doGrado_y_f.grid (row = 2,column = 6, padx = 10, pady = 10)


#---------------------------------- Entradas Método Simpson 1/3 -------------------------------------
# Colocamos entry para poder tener la entrada del usuario

Simpsonfun = Entry (ventanaMetodoSimpson1, justify = "center")
Simpsonfun.grid (row = 1,column = 1, padx = 10, pady = 10,)

Simpsona = Entry (ventanaMetodoSimpson1, justify = "center")
Simpsona.grid (row = 1,column = 3, padx = 10, pady = 10)

Simpsonb = Entry (ventanaMetodoSimpson1, justify = "center")
Simpsonb.grid (row = 1,column = 5, padx = 10, pady = 10)

Simpsonn = Entry (ventanaMetodoSimpson1, justify = "center")
Simpsonn.grid (row = 1,column = 7, padx = 10, pady = 10)

xinicial = Entry (ventanaMetodoSimpson1, justify = "center")
xinicial.grid (row = 2,column = 1, padx = 10, pady = 10,)

xfinal = Entry (ventanaMetodoSimpson1, justify = "center")
xfinal.grid (row = 2,column = 3, padx = 10, pady = 10,)

yinicial = Entry (ventanaMetodoSimpson1, justify = "center")
yinicial.grid (row = 2,column = 5, padx = 10, pady = 10,)

yfinal = Entry (ventanaMetodoSimpson1, justify = "center")
yfinal.grid (row = 2,column = 7, padx = 10, pady = 10,)

#---------------------------------- Salidas Método Simpson 1/3 -------------------------------------
# Etiqueta para mostrar el mensaje

MensajeMetodoSimpson1 = Label (ventanaMetodoSimpson1)
MensajeMetodoSimpson1.grid(row = 4,column = 0, padx = 30, pady = 10, columnspan = 8)


#---------------------------------- Botones Método Simpson 1/3 -------------------------------------
btnCalcular = Button (ventanaMetodoSimpson1, text = "Calcular", command = Calcular)
btnCalcular.grid  (row = 3,column = 0, padx = 30, pady = 10, columnspan = 8)
btnCalcular.config (cursor = "hand2")

botonRegresar = Button(ventanaMetodoSimpson1, text = "Regresar", command = Regresar)
botonRegresar.grid (row = 7,column = 0, padx = 30, pady = 10)
botonRegresar.config (cursor = "hand2")

#---------------------------------- Fin Método Simpson 1/3 -------------------------------------


ventanaMetodoSimpson1.mainloop ()