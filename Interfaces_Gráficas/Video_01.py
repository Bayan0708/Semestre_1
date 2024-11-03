from tkinter import*

raiz = Tk()

raiz.title("Ventana de prebas") #pone titulo

raiz.resizable(True,True) #ancho y alto (en 0,0 no nos dejara cambiar el tamaño de la ventana)

raiz.geometry("650x350") #tamaño de pestaña

raiz.config(bg = "black") #color de fondo

raiz.mainloop() #siempre debe estar al final
