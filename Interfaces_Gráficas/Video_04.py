from tkinter import*


#Ejemplo 1
# raiz = Tk ()

# miFrame = Frame (raiz, width = 1200, height = 600)
# miFrame.pack ()

# cuadroTexto = Entry (miFrame) #Creo un cuadro de texto con entrada
# #cuadroTexto.pack () #enpaqueto el texto
# cuadroTexto.place (x = 100, y = 100)

# nombreLabel = Label(miFrame, text = "Nombre: ") #Ponemos un Label
# nombreLabel.place (x = 100, y = 75) #Ubicamos el label

# raiz.mainloop () #Debe ir al final



#Ejemplo 2
# raiz = Tk ()

# miFrame = Frame (raiz, width = 1200, height = 600)
# miFrame.pack ()

# cuadroNombre = Entry (miFrame) #Creo un cuadro de texto con entrada
# cuadroNombre.grid (row = 0,column = 1) #Fila y columna donde se desa colocar el elemento

# cuadroApellido = Entry (miFrame) 
# cuadroApellido.grid (row = 1,column = 1)

# cuadroDireccion = Entry (miFrame) 
# cuadroDireccion.grid (row = 2,column = 1)


# nombreLabel = Label(miFrame, text = "Nombre: ") #Ponemos un Label
# nombreLabel.grid (row = 0,column = 0, sticky = "e") #Ubicamos el label

# ApellidoLabel = Label(miFrame, text = "Apellido: ")
# ApellidoLabel.grid (row = 1,column = 0,sticky = "w")

# DireccionLabel = Label(miFrame, text = "Dirección de casa: ")
# DireccionLabel.grid (row = 2,column = 0)

# raiz.mainloop () #Debe ir al final



#Ejemplo 3
raiz = Tk ()

miFrame = Frame (raiz, width = 1200, height = 600)
miFrame.pack ()


cuadroNombre = Entry (miFrame) #Creo un cuadro de texto con entrada
cuadroNombre.grid (row = 0,column = 1, padx = 5, pady = 10) #Fila y columna donde se desa colocar el elemento
cuadroNombre.config (fg = "red", justify = "center")

cuadroPass = Entry (miFrame)
cuadroPass.grid (row = 1,column = 1, padx = 5, pady = 10) 
cuadroPass.config (show = "*")

cuadroApellido = Entry (miFrame) 
cuadroApellido.grid (row = 2,column = 1, padx = 5, pady = 10)
cuadroApellido.config (fg = "darkviolet", justify = "right")

cuadroDireccion = Entry (miFrame) 
cuadroDireccion.grid (row = 3,column = 1, padx = 5, pady = 10)



nombreLabel = Label(miFrame, text = "Nombre: ") #Ponemos un Label
nombreLabel.grid (row = 0,column = 0, sticky = "e", padx = 5, pady = 10) #Ubicamos el label

PassLabel = Label(miFrame, text = "Constraseña: ")
PassLabel.grid (row = 1,column = 0,sticky = "e", padx = 5, pady = 10)

ApellidoLabel = Label(miFrame, text = "Apellido: ")
ApellidoLabel.grid (row = 2,column = 0,sticky = "e", padx = 5, pady = 10)

DireccionLabel = Label(miFrame, text = "Dirección de casa: ")
DireccionLabel.grid (row = 3,column = 0,sticky = "e", padx = 5, pady = 10)

raiz.mainloop () #Debe ir al final