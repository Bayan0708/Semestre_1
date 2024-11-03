import matplotlib.pyplot as plt
import numpy as np


a=input("Valor de a:\n")
b=input("Valor de b:\n")

ecuacion=input("Ecuación:\n")


def función_calculo(x, ecuacion):
	try:
		return(float(eval(ecuacion)))
	except:
		raise ValueError



x = np.linspace (a,b,100)