from tkinter import *
from tkinter import messagebox
from math import *
import matplotlib.pyplot as plt




raiz = Tk()
raiz.title("Método Trapezoidal")

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

    if a > b and n>0 and n%2==0:
        mensaje = "El valor de la frontera inferior debe ser menor o igual que el valor de la frontera superior, introduce nuevamente tus datos"
        lblMensaje.config(text = mensaje)              
    else:
        Resultado = 0
        Resultado+=evaluando_copia_f(a)*(h/3)+evaluando_copia_f(b)*(h/3)
        for i in range(1,n):
            x=a+i*h
            if i%2==0:
                Resultado+=evaluando_copia_f(x)*(2*h/3)
            else:
                Resultado+=evaluando_copia_f(x)*(4*h/3)
    mensaje = "El área bajo la curva es de " + str(Resultado)
    lblMensaje.config(text = mensaje)
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

#---------------------------------- Datos de la gráfica Método Trapezoidal -----------------
    plt.plot (lista,lista2,'indigo')
    plt.fill(lista3 , lista4, 'darkviolet', alpha=0.5)
    plt.xlabel('Eje X') # Etiqueta del eje X
    plt.ylabel('Eje Y') # Etiqueta del eje Y
    plt.title('Función y área debajo de la curva')
    plt.grid() # se activa la malla
    plt.show() # Se manda crear la gráfica



def SalirTotal ():
    raiz.destroy()

def Regresar ():
    raiz.destroy()

#Textos


Simpsonestructura = Label (raiz, text = "Este programa aproxima el área bajo la curva de intervalos de funciones, usando el Método Trapezoidal Compuesto", font = ("Courier", 14))
Simpsonestructura.grid (row = 0,column = 0, padx = 30, pady = 10, columnspan = 4)

Simpsoni1 = Label (raiz, text = "Antes de ingresar tu función, lee las siguientes especificaciones:",font = (14))
Simpsoni1.grid (row = 1,column = 0, padx = 10, pady = 10, columnspan = 4)
Simpsoni2 = Label (raiz, text = "1. Introduce funciones que el programa math pueda leer y revisa que estén bien escritas.      2. Revisa bien tu intervalo, ya que necesitamos continuidad en la función.      3. Toma en cuenta que tu función debe estar en función de x.")
Simpsoni2.grid (row = 2,column = 0, padx = 10, pady = 10, columnspan = 4)

Simpsoni5 = Label (raiz, text = "En caso de no cumplir con lo anterior, el programa tendrá un error o probablemente obtengamos un resultado erróneo.")
Simpsoni5.grid (row = 3,column = 0, padx = 10, pady = 10, columnspan = 4)


Simpsonfl = Label (raiz, text = "Dame la función:")
Simpsonfl.grid (row = 4,column = 1, padx = 10, pady = 10)

Simpsonal= Label (raiz, text = "Frontera inferior:")
Simpsonal.grid (row = 5,column = 1, padx = 10, pady = 10)

Simpsonabl = Label (raiz, text = "Frontera Superior:")
Simpsonabl.grid (row = 6,column = 1, padx = 10, pady = 10)

Simpsonanl= Label (raiz, text = "Número de intervalos:")
Simpsonanl.grid (row = 7,column = 1, padx = 10, pady = 10)


# Colocamos entry para poder tener la entrada del usuario

Simpsonfun = Entry (raiz, justify = "center")
Simpsonfun.grid (row = 4,column = 2, padx = 10, pady = 10,)

Simpsona = Entry (raiz, justify = "center")
Simpsona.grid (row = 5,column = 2, padx = 10, pady = 10)

Simpsonb = Entry (raiz, justify = "center")
Simpsonb.grid (row = 6,column = 2, padx = 10, pady = 10)

Simpsonn = Entry (raiz, justify = "center")
Simpsonn.grid (row = 7,column = 2, padx = 10, pady = 10)



# Etiqueta para mostrar el mensaje

lblMensaje = Label (raiz)
lblMensaje.grid(row = 9,column = 0, padx = 30, pady = 10, columnspan = 6)

btnCalcular = Button (raiz, text = "Calcular", command = Calcular)
btnCalcular.grid  (row = 8,column = 0, padx = 30, pady = 10, columnspan = 6)
btnCalcular.config (cursor = "hand2")

botonSalirTotal = Button(raiz, text = "Salir", command = SalirTotal)
botonSalirTotal.grid (row = 10,column = 3, padx = 30, pady = 10)
botonSalirTotal.config (cursor = "hand2")

botonRegresar = Button(raiz, text = "Regresar", command = Regresar)
botonRegresar.grid (row = 10,column = 0, padx = 30, pady = 10)
botonRegresar.config (cursor = "hand2")

raiz.mainloop ()
