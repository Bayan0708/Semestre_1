#Archivo

with open ('ejemplo.txt','r') as archivo:
    linea = archivo.readline()
    while linea != '':
        print (linea, end='')
        linea = archivo.readline()

