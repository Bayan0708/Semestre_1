'''
@author: Sebastián González Juárez
Universidad Nacional Autónoma de México 
Facultad de Ciencias
Computación
Menú
'''
# -*- coding: utf-8 -*-
#menú Matemático
import math
import cmath

opcion=""
while(opcion !="*"):
    print("Bienvenido al menú matemático")
    print("[+] Cálculo")
    print("[-] Raíz")
    print("[*] Salir")
    opcion = input("Selecciona la opción deseada: ")
    if(opcion == "+"):
        while(opcion !="d"):
            print("Bienvenido al menú de cálculo")
            print("[a] Trapecio")
            print("[b] Simpson 1/3")
            print("[c] Simpson 3/8")
            print("[d] Regresar")
            print("[e] salir")
            opcion = input("Selecciona la opción deseada: ")
            if(opcion == "a"):
                print ("Método del Trapecio en construcción")
                print ("Adios")
            elif(opcion == "b"):
                print ("Método de Simpson 1/3 en construcción")
                print ("Adios")
            elif(opcion == "c"):
                print ("Método de Simpson 3/8 en construcción")
                print ("Adios")
            elif(opcion == "d"):
                print ("")
            elif(opcion=="e"):
                exit()
            else:
                print ("Opción no válida, usa solo las del menú")
    elif(opcion == "-"):  
        while(opcion !="4"):
            print ("Bienvenido al menú de raíces")
            print("[1] 2do grado")
            print("[2] Newton-Rapshon")
            print("[3] Bisección")
            print("[4] Regresar")
            print("[5] salir")
            opcion = input("Selecciona la opción deseada: ")
            if(opcion == "1"):
                print ("Método de 2do grado en construcción")
                print ("Adios")
            elif(opcion == "2"):
                print ("Método de Newton-Rapshon en construcción")
                print ("Adios")                
            elif(opcion == "3"):
                print ("Método de Biseccion en construcción")
                print ("Adios")                
            elif(opcion=="4"):
                print("")
            elif(opcion=="5"):
                exit()
            else:
                print ("Opción no válida, usa solo las del menú")
    elif(opcion == "*"):  
        print("Adios")
    else:
        print ("Opcion no válida, usa solo las del menú")