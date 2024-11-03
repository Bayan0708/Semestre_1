import math

x_0=input("Valor de a:\n")
x_1=input("Valor de b:\n")
repeticiones=input("Número de iteraciones:\n")
ecuacion=input("Ecuación:\n")

def función_calculo(x, ecuacion):
	try:
		return(float(eval(ecuacion)))
	except:
		raise ValueError

def Biseccion(ecuacion,x_0,x_1,repeticiones):
    x_0=float(eval(x_0))
    x_1=float(eval(x_1))
    repeticiones=int(eval(repeticiones))
    x_2=(x_0+x_1)/2
    f_0=función_calculo(x_0, ecuacion)
    f_1=función_calculo(x_1, ecuacion)
    f_2=función_calculo(x_2, ecuacion)
    if f_0==0:
        print(f"Existe una raíz en {round(x_0,4)}")
        return()
    elif f_1==0:
        print(f"Existe una raíz en {round(x_1,4)}")
        return()
    elif f_2==0:
        print(f"Existe una raíz en {round(x_2,4)}")
        return()
    for rep in range(repeticiones+1):
        x_2=(x_0+x_1)/2
        f_0=función_calculo(x_0, ecuacion)
        f_1=función_calculo(x_1, ecuacion)
        f_2=función_calculo(x_2, ecuacion)
        if f_0==0:
            print(f"Existe una raíz en {round(x_0,4)}")
            return()
        elif f_1==0:
            print(f"Existe una raíz en {round(x_1,4)}")
            return()
        elif f_2==0:
            print(f"Existe una raíz en {round(x_2,4)}")
            return()
        elif (f_1>0 and f_0>0) or (f_1<0 and f_0<0):
            x_0=x_2
        elif (f_0>0 and f_2>0) or (f_0<0 and f_2<0):
            x_0=x_2
        elif (f_1>0 and f_2>0) or (f_1<0 and f_2<0):
            x_1=x_2

    print(f"Existe una raíz cerca de {round(x_2,4)}")
    print(f"Se tiene una exactitud de {math.fabs(x_0-x_1)}")
        
Biseccion(ecuacion,x_0,x_1,repeticiones)