import tkinter as tk



ventana = tk.Tk()

def Calcular ():
    dias = int (edad.get()) * 365
    mensaje = nombre.get()+" has vivido " + str (dias) + "dias"
    lblMensaje.config(text = mensaje)


# Creamos una etiqueta para indicar que ahí va el nombre
tk.Label(ventana, text = "Nombre").pack ()

# Colocamos entry para poder tener la entrada del usuario
nombre = tk.StringVar()
nomb = tk.Entry (ventana, textvariable = nombre).pack ()


tk.Label (ventana, text = "Edad").pack ()

edad = tk.IntVar()
ed = tk.Entry (ventana, textvariable = edad).pack ()


# Etiqueta para mostrar el mensaje
lblMensaje = tk.Label (ventana)
lblMensaje.pack()

btnCalcular = tk.Button(ventana, text = "Clacular", command = Calcular).pack ()



ventana.mainloop()
