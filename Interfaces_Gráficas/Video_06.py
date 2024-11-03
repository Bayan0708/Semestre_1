from tkinter import*

#Crear una calculadora

raiz = Tk()

miFrame = Frame (raiz)

miFrame.pack ()

#-----------Pantalla---------
pantalla = Entry (miFrame)
pantalla.grid (row = 1,column = 1, padx = 10, pady = 10, columnspan = 4)
pantalla.config (background = "black",fg = "#2CC26B", justify = "right")

#-----------Botones---------

#-----------Fila 1---------
botton7 = Button (miFrame, text = "7", width = 3)
botton7.grid(row = 2, column = 1)
botton8 = Button (miFrame, text = "8", width = 3)
botton8.grid(row = 2, column = 2)
botton9 = Button (miFrame, text = "9", width = 3)
botton9.grid(row = 2, column = 3)
bottonDiv = Button (miFrame, text = "/", width = 3)
bottonDiv.grid(row = 2, column = 4)

#-----------Fila 2---------
botton4 = Button (miFrame, text = "4", width = 3)
botton4.grid(row = 3, column = 1)
botton5 = Button (miFrame, text = "5", width = 3)
botton5.grid(row = 3, column = 2)
botton6 = Button (miFrame, text = "6", width = 3)
botton6.grid(row = 3, column = 3)
bottonMult = Button (miFrame, text = "x", width = 3)
bottonMult.grid(row = 3, column = 4)

#-----------Fila 3---------
botton1 = Button (miFrame, text = "1", width = 3)
botton1.grid(row = 4, column = 1)
botton2 = Button (miFrame, text = "2", width = 3)
botton2.grid(row = 4, column = 2)
botton3 = Button (miFrame, text = "3", width = 3)
botton3.grid(row = 4, column = 3)
bottonRest = Button (miFrame, text = "-", width = 3)
bottonRest.grid(row = 4, column = 4)

#-----------Fila 3---------
botton0 = Button (miFrame, text = "0", width = 3)
botton0.grid(row = 5, column = 1)
bottonComa = Button (miFrame, text = ",", width = 3)
bottonComa.grid(row = 5, column = 2)
bottonIgual = Button (miFrame, text = "=", width = 3)
bottonIgual.grid(row = 5, column = 3)
bottonSum = Button (miFrame, text = "+", width = 3)
bottonSum.grid(row = 5, column = 4)


raiz.mainloop()