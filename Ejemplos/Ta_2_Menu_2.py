# -*- coding: utf-8 -*-
#Diseñe un menú Matemático
import math
import cmath

opcion=""
while(opcion !="*"):
    print("Bienvenido al menu matematico")
    print("[+] Calculo")
    print("[-] Raiz")
    print("[*] Salir")
    opcion = input("Selecciona la opcion deseada > ")
    if(opcion == "+"):
        while(opcion !="d"):
            print("Bienvenido al menu de calculo")
            print("[a] Trapecio")
            print("[b] Simpson 1/3")
            print("[c] Simpson 3/8")
            print("[d] Regresar")
            print("[e] salir")
            opcion = input("Selecciona la opcion deseada > ")
            if(opcion == "a"):
                print ("Metodo del Trapecio en construccion")
                print ("Adios")
            elif(opcion == "b"):
                print ("Metodo de Simpson 1/3 en construccion")
                print ("Adios")
            elif(opcion == "c"):
                print ("Metodo de Simpson 3/8 en construccion")
                print ("Adios")
            elif(opcion == "d"):
                print ("Adios")
            elif(opcion=="e"):
                exit()
            else:
                print ("Opcion no valida, usa solo las del menu")
    elif(opcion == "-"):  
        print("Bienvenido al menu de raices")
        while(opcion !="4"):
            print ("Bienvenido al menu de raices")
            print("[1] 2do grado")
            print("[2] Newton-Rapshon")
            print("[3] Biseccion")
            print("[4] Regresar")
            print("[5] salir")
            opcion = input("Selecciona la opcion deseada > ")
            if(opcion == "1"):
                print ("Metodo de 2do grado en construccion")
            elif(opcion == "2"):
                print ("Metodo de Newton-Rapshon en construccion")
            elif(opcion == "3"):
                print ("Metodo de Biseccion en construccion")
            elif(opcion=="4"):
                print("Adios")
            elif(opcion=="5"):
                exit()
            else:
                print ("Opcion no valida, usa solo las del menu")
    elif(opcion == "*"):  
        print("Adios")
    else:
        print ("Opcion no valida, usa solo las del menu")
