from tkinter import*

raiz = Tk()

raiz.title("Ventana de prebas") #pone titulo
raiz.resizable(True,True) #ancho y alto (en 0,0 no nos dejara cambiar el tamaño de la ventana)
raiz.geometry("650x350") #tamaño de pestaña
raiz.config(bg = "black") #color de fondo


raiz.config(bd = 20) #Tamaño del borde de la raiz
raiz.config (relief = "sunken") #Estilo del borde de la raiz


miFrame = Frame () #abre un frame
miFrame.pack (side = "top", anchor = "e") #mete al frame al interior de la raiz y lo coloca en un espacio, anchor ayuda a dar una segunda coordenada
#miFrame.pack (fill = "x") #Hace que el frame se expanda horizontalmente
#miFrame.pack (fill = "y", expand = "True") #Hace que el frame se expanda verticalmente
#miFrame.pack (fill = "both", expand = "True") #Hace que el frame se expanda para ambas partes
miFrame.config(bg = "white") #Le da color a un frame
miFrame.config(width = "300", height = "150") #Le da tamaño al frame

miFrame.config (bd = 10) #Pone bordes al Frame
miFrame.config (relief = "groove") #Estilo del borde del frame

miFrame.config (cursor = "hand2") #Cambia el estilo del cursos al pasar por el frame

raiz.mainloop() #siempre d#ebe estar al final