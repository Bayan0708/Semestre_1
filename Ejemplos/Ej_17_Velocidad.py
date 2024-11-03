# -*- coding: utf-8 -*-

# def generarDatos():
#     posicionInicial=[0,30]
#     posicionFinal=[0,0]

#     archivo=open("datos.data", "w")
#     archivo.write("t\tPX\tPY\tn")   #Solo encabezado
#     #t  Px  Py
#     #1  0   30

#     cont = 1
#     for i in range (posicionInicial[1], posicionFinal[1]-1,-1):
#         print(cont, i, 0)
#         archivo. write(""+str(cont)+"\t0\t"+str(i)+"\n")
#         cont+=1
#     archivo. close()


piy = 30
pfy = 0
cont=1
while piy >= pfy:
    print(cont, 0, piy)
    piy -= 1
    cont += 1
