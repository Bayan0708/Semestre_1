# -*- coding: utf-8 -*-
#Diseñe un menú Matemático



print("Bienvenido al menu matematico")
print("[+] Calculo")
print("[-] Raiz")
print("[*] Salir")

opcion=""

opcion = input("Selecciona la opcion deseada ")
if(opcion == "+"):
    print("Bienvenido al menu de calculo")
    print("[a] Trapecio")
    print("[b] Simpson 1/3")
    print("[c] Simpson 3/8")
    print("[q] Salir")
    opcion=""
    opcion = input("Selecciona la opcion deseada ")
    if(opcion == "a"):
        print ("Metodo del Trapecio en construccion")
        print ("Adios")
        exit
    elif(opcion == "b"):
        print ("Metodo de Simpson 1/3 en construccion")
        print ("Adios")
        exit
    elif(opcion == "c"):
        print ("Metodo de Simpson 3/8 en construccion")
        print ("Adios")
        exit
    elif(opcion == "q"):
        print ("Adios")
        exit
    else:
        print ("Opcion no valida")
        print ("Adios")
        exit
elif(opcion == "-"):  
    print ("Bienvenido al menu de raices")
    print("[1] 2do grado")
    print("[2] Newton-Rapshon")
    print("[3] Biseccion")
    print("[4] Salir")
    opcion=""
    opcion = input("Selecciona la opcion deseada ")
    if(opcion == "1"):
        print ("Metodo de 2do grado en construccion")
        print ("Adios")
        exit
    elif(opcion == "2"):
        print ("Metodo de Newton-Rapshon en construccion")
        print ("Adios")
        exit
    elif(opcion == "3"):
        print ("Metodo de Biseccion en construccion")
        print ("Adios")
        exit
    elif(opcion == "4"):
        print ("Adios")
        exit
    else:
        print ("Opcion no valida")
        print ("Adios")
        exit
elif(opcion == "*"):  
    print ("Adios")
    exit
else:
    print ("Opcion no valida")
    print ("Adios")
    exit