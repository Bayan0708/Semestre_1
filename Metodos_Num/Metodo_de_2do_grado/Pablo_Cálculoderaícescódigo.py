import math
import cmath
import numpy as np
import matplotlib.pyplot as plt

print("Cálculo de raíces de polinomio de segundo grado") 

def calculator():
    try:
        global a
        global b
        global c
        a = int(input("Eliga el número para el primer valor $"))
        b = int(input("Eliga el número para el segundo valor $"))
        c = int(input("Eliga el número para el tercer valor $"))
    except ValueError as ERROR:
        print("Por favor ingresa un número")
        return

    print("Usted ha elegido los siguentes valores: a = " + str(a) + ", b = " + str(b) + ", c = " + str(c))

    if a == 0: 
        print("No calculo raíces de grado 1")
    elif a != 0:
        d = b ** 2 + (-4*a*c)
        if d == 0:
            x = (-b) / (2*a)
            print("x1 = " + str(x), "x2 = " + str(x))
        elif d > 0: #Determinante pertenece números reales
            x1 = ((-b) + math.sqrt(d))/(2*a)
            x2 = ((-b) - math.sqrt(d))/(2*a)
            print("x1 = " + str(x1), "x2 = " + str(x2))

            #Grafica función
            x_val = np.linspace(-50, 50, 500)
            y_val = np.array([a*x**2 + b*x + c for x in x_val])
            fig, ax = plt.subplots(figsize=(10,6))
            ax.plot(x_val, y_val)
            ax.set_title(f'{a:.0f}' + "x**2 + " + f'{b:.0f}' + "x + " + f'{c:.0f}')
            ax.grid(True, color="black")
            plt.xlabel("Eje x")
            plt.ylabel("Eje y")
            plt.show()
        elif d < 0: #Detereminante pertence números imaginarios
            x1 = (-b + cmath.sqrt(d))/(2*a)
            x2 = (-b - cmath.sqrt(d))/(2*a)
            #Imprimir todos los decimáles
            #print("x1 = " + str(x1), "x2 = " + str(x2))
            print(f'{x1:.2f}', f'{x2:.2f}') 
            print("No se puede generar una gráfica por el momento")
    else:
        print("No conozco esa opción por favor selecciona una correcta")

while True:
    calculator()