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
                print ("Método de 2do grado")
                while True:
                    try:
                        a = float(input("Ingrese coeficiente a: "))
                        b = float(input("Ingrese coeficiente b: "))
                        c = float(input("Ingrese coeficiente c: "))
                        if a==0:
                            print("El coeficiente a no puede ser igual a cero, inserta nuevamente tus datos")
                        else:
                            discriminante = b**2-4*a*c
                            if discriminante >= 0:
                                if discriminante == 0:
                                    x = -b / (2 * a)
                                    print("La raíz única x es"+str(x))
                                    break
                                else:
                                    x1=(-b+ (discriminante**(1/2)))/2*a
                                    x2=(-b- (discriminante**(1/2)))/2*a
                                    print("La raíz real x1 es "+str(x1),"y la raíz real x2 es "+str(x2))
                                    break
                            else:
                                x1=(-b+cmath. sqrt(discriminante))/2*a
                                x2=(-b+cmath. sqrt(discriminante))/2*a
                                print("La raíz imaginaria x1 es "+str(x1),"y la raíz imaginaria x2 es "+str(x2))
                                break
                    except (ValueError):
                        print("Por favor ingresa números válidos, vuelve a empezar")
            elif(opcion == "2"):
                print ("Método de Newton-Rapshon en construcción")
            elif(opcion == "3"):
                print ("Método de Biseccion en construcción")
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



