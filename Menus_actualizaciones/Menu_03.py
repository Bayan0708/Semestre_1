#menú Matemático 
# -*- coding: utf-8 -*-
'''
@author: Sebastián González Juárez
'''
import math
import cmath
from math import*

def Me_2do_grado():
    while True:
        try:
            a = float(input("Ingrese coeficiente a: "))
            b = float(input("Ingrese coeficiente b: "))
            c = float(input("Ingrese coeficiente c: "))
            if a==0:
                print("\nEl coeficiente a no puede ser igual a cero, inserta nuevamente tus datos")
            else:
                discriminante = b**2-4*a*c
            if discriminante >= 0:
                if discriminante == 0:
                    x = -b / (2 * a)
                    print("\nLa raíz única x es"+str(x))
                    break
                else:
                    x1=(-b+math. sqrt(discriminante))/2*a
                    x2=(-b+math. sqrt(discriminante))/2*a
                    print("\nLa raíz real x1 es "+str(x1),"y la raíz real x2 es "+str(x2))
                    break
            else:
                x1=(-b+cmath. sqrt(discriminante))/2*a
                x2=(-b+cmath. sqrt(discriminante))/2*a
                print("\nLa raíz imaginaria x1 es "+str(x1),"y la raíz imaginaria x2 es "+str(x2))
                break
        except (ValueError):
            print("\nPor favor ingresa números válidos, vuelve a empezar")

def Me_Simpson_1_3():
    def evaluando_copia_f (x):
        copia_f=f.copy()
        for i in range(len(copia_f)):
            if copia_f[i]=="x":
                copia_f[i]==x
        return eval("".join(copia_f))

    print("\nMétodo Simpson 1/3 Compuesto")
    Especificaciones=["\nAntes de ingresar tu función, lee las siguientes especificaciones:","1. Introduce funciones que el programa math pueda leer y revisa que estén bien escritas.","2. Revisa bien tu intervalo, ya que necesitamos continuidad en la función.","3. Toma en cuenta que tu función debe estar en función de x.","En caso de no cumplir con lo anterior, el programa se cerrará o probablemente obtengamos un resultado erróneo." ]
    for v in Especificaciones:
        print(v)

    f=list(input("\nDame la función: "))

    while True:
        while True:
            try:
                inferior=float(input("\nDame la frontera inferior del intervalo: "))
                break
            except ValueError:
                print("\nInserta únicamente números reales")
        while True:
            try:
                superior=float(input("\nDame la frontera superior del intervalo: "))
                break
            except ValueError:
                print("\nInserta únicamente números reales")
        if superior>=inferior:
            break
        else:
            print("\nEl valor de la frontera inferior debe ser menor o igual que el valor de la frontera superior, introduce nuevamente tus datos")
    inferior=inferior
    superior=superior

    while True:
        while True:
            try:
                n=int(input("\nDame el número de intervalos: "))
                break
            except ValueError:
                print("\nInserta únicamente números enteros pares mayores a 0")
        if n>0 and n%2==0:
            break
        else:
            print("\nInserta únicamente números enteros pares mayores a 0")
    n=n
    h=(superior-inferior)/n
    Resultado=0
    Resultado+=evaluando_copia_f(inferior)*(h/3)+evaluando_copia_f(superior)*(h/3)
    for i in range(1,n):
        x=inferior+i*h
        if i%2==0:
            Resultado+=evaluando_copia_f(x)*(2*h/3)
        else:
            Resultado+=evaluando_copia_f(x)*(4*h/3)
    print ("\nLa aproximación del área bajo la curva de tu función, es = "+str( Resultado))

def Me_Trapezoidal():
    def evaluando_copia_f (x):
        copia_f=f.copy()
        for i in range(len(copia_f)):
            if copia_f[i]=="x":
                copia_f[i]==x
        return eval("".join(copia_f))
    print("\nMétodo Trapezoidal Compuesto")
    Especificaciones=["\nAntes de ingresar tu función, lee las siguientes especificaciones:","1. Introduce funciones que el programa math pueda leer y revisa que estén bien escritas.","2. Revisa bien tu intervalo, ya que necesitamos continuidad en la función.","3. Toma en cuenta que tu función debe estar en función de x.","En caso de no cumplir con lo anterior, el programa se cerrará o probablemente obtengamos un resultado erróneo." ]
    for v in Especificaciones:
        print(v)
    f=list(input("\nDame la función: "))
    while True:
        while True:
            try:
                inferior=float(input("\nDame la frontera inferior del intervalo: "))
                break
            except ValueError:
                print("\nInserta únicamente números reales")
        while True:
            try:
                superior=float(input("\nDame la frontera superior del intervalo: "))
                break
            except ValueError:
                print("\nInserta únicamente números reales")
        if superior>=inferior:
            break
        else:
            print("\nEl valor de la frontera inferior debe ser menor o igual que el valor de la frontera superior, introduce nuevamente tus datos")
    inferior=inferior
    superior=superior
    while True:
        while True:
            try:
                n=int(input("\nDame el número de intervalos: "))
                break
            except ValueError:
                print("\nInserta únicamente números enteros mayores a 0")
        if n>0:
            break
        else:
            print("\nInserta únicamente números enteros mayores a 0")
    n=n
    h=(superior-inferior)/n
    Resultado=0
    Resultado+=evaluando_copia_f(inferior)*(h/2)+evaluando_copia_f(superior)*(h/2)
    for i in range(1,n):
        x=inferior+i*h
        Resultado+=evaluando_copia_f(x)*h
    print ("\nLa aproximación del área bajo la curva de tu función, es = "+str( Resultado))

opcion=""
while(opcion !="*"):   
    print("\nBienvenido al menú matemático")
    Menú_Mate = ["[+] Cálculo", "[-] Raíz", "[*] Salir"]
    for M in Menú_Mate:
        print(M)
    opcion = input("\nSelecciona la opción deseada: ")
    if(opcion == "+"):
        while(opcion !="d"):
            print("\nBienvenido al menú de cálculo")
            Menú_Calculo = ["[a] Trapecio", "[b] Simpson 1/3", "[c] Simpson 3/8","[d] Regresar","[e] salir"]
            for C in Menú_Calculo:
                print(C)
            opcion = input("\nSelecciona la opción deseada: ")
            if(opcion == "a"):
                Me_Trapezoidal()
            elif(opcion == "b"):
                Me_Simpson_1_3()
            elif(opcion == "c"):
                print ("\nMétodo de Simpson 3/8 en construcción")
                print ("Adiós")
            elif(opcion == "d"):
                print ("")
            elif(opcion=="e"):
                exit()
            else:
                print ("\nOpción no válida, usa solo las del menú")
    elif(opcion == "-"):  
        while(opcion !="4"):
            print("\nBienvenido al menú de raíces")
            Menú_Raíz = ["[1] 2do grado", "[2] Newton-Rapshon", "[3] Bisección","[4] Regresar","[5] salir"]
            for R in Menú_Raíz:
                print(R)
            opcion = input("\nSelecciona la opción deseada: ")
            if(opcion == "1"):
                print ("\nMétodo de 2do grado")
                Me_2do_grado()
            elif(opcion == "2"):
                print ("\nMétodo de Newton-Rapshon en construcción")
            elif(opcion == "3"):
                print ("\nMétodo de Biseccion en construcción")
            elif(opcion=="4"):
                print("")
            elif(opcion=="5"):
                exit()
            else:
                print ("\nOpción no válida, usa solo las del menú")
    elif(opcion == "*"):  
        print("Adiós")
    else:
        print ("\nOpcion no válida, usa solo las del menú")