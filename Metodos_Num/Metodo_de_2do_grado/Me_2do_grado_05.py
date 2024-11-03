'''
@author: Sebastián González Juárez
Universidad Nacional Autónoma de México 
Facultad de Ciencias
Computación
Programa Ecuaciones 2do grado
'''

#Calcular raicez de ecuaciones de segundo grado



print ("Metodo de 2do grado")

while True:
    a = float(input("Ingrese coeficiente a: "))
    b = float(input("Ingrese coeficiente b: "))
    c = float(input("Ingrese coeficiente c: "))
    if a==0:
        print("El coeficiente a no puede ser igual a cero")
    else:
        discriminante = b**2 - 4 * a * c
        if discriminante >= 0:
            if discriminante == 0:
                x = -b / (2 * a)
                print("La raíz única es {:.3f}".format(x))
                break
            else:
                x1 = (-b + (discriminante**0.5)) / (2 * a)
                x2 = (-b - (discriminante**0.5)) / (2 * a)
                print("La raíz real x1 es {:.3f}".format(x1))
                print("La raíz real x2 es {:.3f}".format(x2))
                break
        else:
            discriminante = abs(discriminante)
            parteReal = -b / (2 * a)
            parteImaginaria =(discriminante**0.5) / (2 * a)
            print("La raíz compleja x1 es {:.3f} + {:.3f}i".format(parteReal, parteImaginaria))
            print("La raíz compleja x2 es {:.3f} - {:.3f}i".format(parteReal, parteImaginaria))
            break