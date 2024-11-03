#Programa para intentar abrir pestañas
#En este tutorial aprenderas a usar la libreria tkinter asi como a crear una ventana principal y ventanas hijas
#Código:

from tkinter import *
ventana=Tk()
ventana.geometry("400x400")
ventana.title("Bienvenido")

#---------------------------------- Funciones -----------------------------------------------------------------

def v2():
    ventana2=Toplevel()
    ventana2.geometry("400x400")
    ventana2.title("Bienveido otra vez")
    def v3():
        ventana3=Toplevel()
        ventana3.geometry("400x400")
        ventana3.title("Bienveido otra vez por tercera vez")
    
    boton2=Button(ventana2,text="Aceptar",command=v3).pack()

        


#------------------------------ Botones ------------------------------------------------------------

boton1=Button(ventana,text="Aceptar",command=v2).pack()




ventana.mainloop()
