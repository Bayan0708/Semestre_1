from tkinter import*

#Crear una calculadora 3

raiz = Tk()
miFrame = Frame (raiz)
miFrame.pack ()


operacion = ""
resultado = 0

#-----------Pantalla---------

numeroPantalla = StringVar ()

pantalla = Entry (miFrame, textvariable = numeroPantalla)
pantalla.grid (row = 1,column = 1, padx = 10, pady = 10, columnspan = 4)
pantalla.config (background = "black",fg = "#2CC26B", justify = "right")


#-----------Pulsasiones Teclado---------
def numeroPulsado(num):
    global operacion 
    if operacion != "":
        numeroPantalla.set(num)
        operacion = ""
    else:            
        numeroPantalla.set(numeroPantalla.get () + num)


#-----------funcion suma---------
def suma(num):
    global operacion 
    global resultado
    resultado += float(num)
    operacion = "suma"

    numeroPantalla.set(resultado)

#-----------funcion el resultado---------
def el_resultado():
    global resultado
    numeroPantalla.set(resultado+float(numeroPantalla.get()))
    resultado = 0

#-----------Botones---------

#-----------Fila 1---------
botton7 = Button (miFrame, text = "7", width = 3, command = lambda:numeroPulsado("7"))
botton7.grid(row = 2, column = 1)
botton8 = Button (miFrame, text = "8", width = 3, command = lambda:numeroPulsado("8"))
botton8.grid(row = 2, column = 2)
botton9 = Button (miFrame, text = "9", width = 3, command = lambda:numeroPulsado("9"))
botton9.grid(row = 2, column = 3)
bottonDiv = Button (miFrame, text = "/", width = 3)
bottonDiv.grid(row = 2, column = 4)

#-----------Fila 2---------
botton4 = Button (miFrame, text = "4", width = 3, command = lambda:numeroPulsado("4"))
botton4.grid(row = 3, column = 1)
botton5 = Button (miFrame, text = "5", width = 3, command = lambda:numeroPulsado("5"))
botton5.grid(row = 3, column = 2)
botton6 = Button (miFrame, text = "6", width = 3, command = lambda:numeroPulsado("6"))
botton6.grid(row = 3, column = 3)
bottonMult = Button (miFrame, text = "x", width = 3)
bottonMult.grid(row = 3, column = 4)

#-----------Fila 3---------
botton1 = Button (miFrame, text = "1", width = 3, command = lambda:numeroPulsado("1"))
botton1.grid(row = 4, column = 1)
botton2 = Button (miFrame, text = "2", width = 3, command = lambda:numeroPulsado("2"))
botton2.grid(row = 4, column = 2)
botton3 = Button (miFrame, text = "3", width = 3, command = lambda:numeroPulsado("3"))
botton3.grid(row = 4, column = 3)
bottonRest = Button (miFrame, text = "-", width = 3)
bottonRest.grid(row = 4, column = 4)

#-----------Fila 3---------
botton0 = Button (miFrame, text = "0", width = 3, command = lambda:numeroPulsado("0"))
botton0.grid(row = 5, column = 1)
bottonComa = Button (miFrame, text = ".", width = 3, command = lambda:numeroPulsado("."))
bottonComa.grid(row = 5, column = 2)
bottonIgual = Button (miFrame, text = "=", width = 3, command = lambda:el_resultado())
bottonIgual.grid(row = 5, column = 3)
bottonSum = Button (miFrame, text = "+", width = 3, command = lambda:suma(numeroPantalla.get()))
bottonSum.grid(row = 5, column = 4)


raiz.mainloop()