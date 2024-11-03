# -*- coding: utf-8 -*-

# contador=0
# while(contador < 5):
#     print("Hola")
#     contador=contador+1

# opcion=""
# while(opcion != "S"):
#     opcion=input("Dame una opcion ")
#     print("Seleccionaste "+ opcion)

opcion=""
while(opcion != "S"):
    print("Bienvenido. \r\nEl menu de hoy es:")
    print("[P] Pizza")
    print("[H] Hamburguesa")
    print("[A] Papas")
    print("[C] Carne")
    print("[S] Salir del aqui")
    opcion= input("Que desdeas comer ")
    print("Seleccionaste "+ opcion)
    if(opcion=="P"):
        print("Le sirvo Pizza")
    elif(opcion=="H"):
        print("Le doy hamburguesas")
    elif(opcion=="A"):
        print("Tenemos varios tipos de papas")
        print("[1] Cocidas")
        print("[2] Fritas")
        print("[3] crudas")
        opcionPapas = input("Como quieres sus papas")
        if(opcionPapas == "1"):
            print("Van papas cocidas")
        elif(opcionPapas == "2"):
            print("Van papas fritas")
        elif(opcionPapas == "3"):
            print("Van papas crudas")
    elif(opcion == "C"):
        print("Sale un trozo de carne")
    elif(opcion == "S"):
        print("adios, vuelva pronto")


# termina while
