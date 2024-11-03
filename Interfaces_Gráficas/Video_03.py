from tkinter import*

#Practicar Label

root = Tk () #invocamos la raíz

miFrame = Frame (root, width=500, height=400) #Invocamos un Frame
miFrame.pack() #en paqueta el Frame
#miImagen = PhotoImage(file = "Foto_python.png")

# miLabel = Label (miFrame, text = "Hola UwU") #Crea un label y un texto
# #miLabel.pack () #en paqueta el label
# miLabel.place (x = 100, y = 200) #ubica el Label
Label (miFrame, text = "Wenas UwU", fg = "blue", font = ("Comic Sans MS", 18)).place (x = 100, y= 200) #abrevia lo de arriba
#Label (miFrame, image = miImagen).place (x = 300, y= 100)

root.mainloop () #siempre deebe estar al final