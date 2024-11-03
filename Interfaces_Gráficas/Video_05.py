from tkinter import*

raiz = Tk ()

miFrame = Frame (raiz, width = 1200, height = 600)
miFrame.pack ()

#Agregamos un nombre
minombre = StringVar()

cuadroNombre = Entry (miFrame, textvariable = minombre) 
cuadroNombre.grid (row = 0,column = 1, padx = 5, pady = 10)
cuadroNombre.config (fg = "red", justify = "center")

cuadroPass = Entry (miFrame)
cuadroPass.grid (row = 1,column = 1, padx = 5, pady = 10) 
cuadroPass.config (show = "*")

cuadroApellido = Entry (miFrame) 
cuadroApellido.grid (row = 2,column = 1, padx = 5, pady = 10)
cuadroApellido.config (fg = "darkviolet", justify = "right")

cuadroDireccion = Entry (miFrame) 
cuadroDireccion.grid (row = 3,column = 1, padx = 5, pady = 10)


#Agregamos texto
textoComentario = Text (miFrame, width = 16, height = 5)
textoComentario.grid (row = 4, column = 1,padx = 5, pady = 10)


#Agregamos una barrita y la colocamos
scrollVert = Scrollbar(miFrame, command = textoComentario.yview)
scrollVert.grid(row = 4, column = 2, sticky = "nsew")

textoComentario.config (yscrollcommand = scrollVert.set)



nombreLabel = Label(miFrame, text = "Nombre: ") #Ponemos un Label
nombreLabel.grid (row = 0,column = 0, sticky = "e", padx = 5, pady = 10) #Ubicamos el label

PassLabel = Label(miFrame, text = "Constraseña: ")
PassLabel.grid (row = 1,column = 0,sticky = "e", padx = 5, pady = 10)

ApellidoLabel = Label(miFrame, text = "Apellido: ")
ApellidoLabel.grid (row = 2,column = 0,sticky = "e", padx = 5, pady = 10)

DireccionLabel = Label(miFrame, text = "Dirección de casa: ")
DireccionLabel.grid (row = 3,column = 0,sticky = "e", padx = 5, pady = 10)

ComentariosLabel = Label(miFrame, text = "Comentarios: ")
ComentariosLabel.grid (row = 4,column = 0,sticky = "e", padx = 5, pady = 10)


#Hacer un boton

def codigoBoton ():
    minombre.set ("Sebas")

botonEnvio = Button (raiz, text = "Enviar", command = codigoBoton)
botonEnvio.pack()


raiz.mainloop () #Debe ir al final