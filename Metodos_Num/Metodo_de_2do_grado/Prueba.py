from tkinter import *

raiz = Tk()
raiz.title("Ecuaciones 2do Grado")


#Funciones




def Calcular ():
    a = int (coeficientea.get())

    b = int (coeficienteb.get())

    c = int (coeficientec.get())
    

    if a==0:
        mensaje = "El coeficiente a no puede ser igual a cero, ingresa otros datos"
        lblMensaje.config(text = mensaje)
    else:
        discriminante = b**2 - 4 * a * c
        if discriminante >= 0:
            if discriminante == 0:
                x = -b / (2 * a)
                mensaje = "La raíz única es {:.3f}".format(x)
                lblMensaje.config(text = mensaje)
            else:
                x1 = (-b + (discriminante**0.5)) / (2 * a)
                x2 = (-b - (discriminante**0.5)) / (2 * a)
                mensaje = "Las raíces reales son: x1 = {:.3f}".format(x1) + "   y   " + "x2 = {:.3f}".format(x2)
                lblMensaje.config(text = mensaje)

        else:
            discriminante = abs(discriminante)
            parteReal = -b / (2 * a)
            parteImaginaria =(discriminante**0.5) / (2 * a)
            mensaje = "Las raíces complejas son: x1 = {:.3f} + {:.3f}i".format(parteReal, parteImaginaria) + "   y   " + "x2 = {:.3f} - {:.3f}i".format(parteReal, parteImaginaria)
            lblMensaje.config(text = mensaje)          

def SalirTotal ():
    raiz.destroy()

def Regresar ():
    raiz.destroy()

#Textos

estructura = Label (raiz, text = "Este programa encuentra las raíces de ecuaciones con la forma: ax^2+bx+c", font = ("Courier", 11))
estructura.grid (row = 0,column = 0, padx = 30, pady = 10, columnspan = 6)

Primero = Label (raiz, text = "Coeficiente a:")
Primero.grid (row = 1,column = 0, padx = 10, pady = 10)


Segundo = Label (raiz, text = "Coeficiente b:")
Segundo.grid (row = 1,column = 2, padx = 10, pady = 10)

Tercero = Label (raiz, text = "Coeficiente c:")
Tercero.grid (row = 1,column = 4, padx = 10, pady = 10)



# Colocamos entry para poder tener la entrada del usuario

coeficientea = Entry (raiz, justify = "center")
coeficientea.grid (row = 1,column = 1, padx = 10, pady = 10,)

coeficienteb = Entry (raiz, justify = "center")
coeficienteb.grid (row = 1,column = 3, padx = 10, pady = 10)

coeficientec = Entry (raiz, justify = "center")
coeficientec.grid (row = 1,column = 5, padx = 10, pady = 10)



# Etiqueta para mostrar el mensaje

lblMensaje = Label (raiz)
lblMensaje.grid(row = 3,column = 0, padx = 30, pady = 10, columnspan = 6)

btnCalcular = Button (raiz, text = "Clacular", command = Calcular)
btnCalcular.grid  (row = 2,column = 0, padx = 30, pady = 10, columnspan = 6)
btnCalcular.config (cursor = "hand2")


botonSalirTotal = Button(raiz, text = "Salir", command = SalirTotal)
botonSalirTotal.grid (row = 4,column = 5, padx = 30, pady = 10, columnspan = 6)
botonSalirTotal.config (cursor = "hand2")

botonRegresar = Button(raiz, text = "Regresar", command = Regresar)
botonRegresar.grid (row = 4,column = 0, padx = 30, pady = 10)
botonRegresar.config (cursor = "hand2")

raiz.mainloop ()