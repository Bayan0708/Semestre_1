# -- coding: utf-8 --
from math import *
import matplotlib.pyplot as plot
import matplotlib
matplotlib.style.use("seaborn")
gr=1
matplotlib.rcParams["figure.figsize"]=(16*gr, 9*gr)
matplotlib.rcParams["axes.labelsize"]=(16*gr)
matplotlib.rcParams["xtick.labelsize"]=(16*gr)
matplotlib.rcParams["ytick.labelsize"]=(16*gr)

"""
Aquí unos ejemplos que estarían útiles:

-((1509+38)/7)
(936/4)-11
log10(fabs(1/(x+15.3*2))) + (e2/(x+15.32))*pi*3 + (x/18)*sin(x)

-3*e
2*pi
sin(x**2)-sqrt(fabs(x))

-(e**2 + pi)
(pi-e)**3
cos(5*sin(2*x) + e/pi) + sin(5*x*sqrt(fabs(x))) + 2*sin(x)

-sqrt(17424+12)
(pi+e)**e
20*log10( (fabs(x+20)+1/5) / (fabs(x-10)+1/5)) + (e*2 / (7*fabs(x+60)+10))*pi*3 + (x/20)*sin(fabs(x))
"""

def esperar():
	input("\nPuedes decirme lo que sea cuando termines, incluso puedes solo presionar enter sin escribir nada. Te espero. （＾ω＾）")

def función_calculo(x, fun):
	try:
		return(float(eval(fun)))
	except:
		raise ValueError

def grafica_integral(x_f,valores_f):
	fig, ax = plot.subplots()
	plot.xlabel("Eje X")
	plot.ylabel("Eje Y")
	ax.plot(x_f,valores_f,"b")
	x_val=[x_f[0]]+x_f+[x_f[-1]]
	f_val=[0]+valores_f+[0]
	ax.fill(x_val,f_val,"g",alpha=.2)
	ax.vlines(x=x_f[0], ymin=0, ymax=valores_f[0])
	ax.vlines(x=x_f[-1], ymin=0, ymax=valores_f[-1])
	ax.hlines(y=0,xmin=x_f[0],xmax=x_f[-1])
	plot.show()
	print("Así se ve la aproximación hecha en intervalos")

def integral_trapecio(a,b,inval,fun):
	try:
		base=(b-a)/inval
		valores_f=[]
		x_f=[]
		for paso in range(inval+1):
			x_o=a+(paso*base)
			valor=función_calculo(x_o,fun)
			valores_f.append(valor)
			x_f.append(x_o)
		integral=valores_f[0]+valores_f[-1]
		for valor in valores_f[1:-1]:
			integral+=2*valor
		grafica_integral(x_f,valores_f)
		print(f"\nLa integral definida de {fun} entre {a} y {b} aproximada con {inval} intervalos es {integral*(base/2)}")
	except:
		raise ValueError

def pregunta_trapecio(end):
	while True:
		try:
			print("\nRecuerda que puedes usar, por ejemplo. 'e', '97/4', '7.22'. uwu")
			return(float(eval(input(f"Dime donde quieres que {end} la integral. :3\nTú: Quiero que {end} en "))))
		except:
			print("\nEse no fue un número real. Uwu")

def trapecio():
	print("Quieres calcular Trapecio.")
	print("\nPara escribir los valores del intervalo puedes usar operaciones usando el leguaje Python")
	print("ya sea para escribir operaciones soportadas por Python y el módulo math.")
	a=pregunta_trapecio("empiece")
	b=a-1
	while a>=b:
		b=pregunta_trapecio("acabe")
		if a>=b:
			print("\nEl punto en que termina debe ser mayor al punto en que acaba, si no no tiene sentido. 'n.n")
	while True:
		try:
			inval = float(input("¿Cuantos intervalos (tiene que ser un número natural) de trapecios quieres? :3\nTú: Quiero que tenga "))
			if inval!=int(inval) or inval<=0:
				raise ValueError
			elif inval>1000000:
				raise RuntimeError
			inval = int(inval)
			break
		except RuntimeError:
			print("\nEse valor es excesivamente grande, te pido no poner valores mayores a 1 000 000 de favor. QwQ")
		except:
			print("\nEse no fue un número natural. Uwu")
	while True:
		print("\nVoy a necesitar que escribas la función usando lenguaje de Python para calcular. ^^")
		print("Pon la función usando adecuadamente el módulo math de Python. UuU")
		print("\nPor ejemplo, puedes usar 'log10(x) + x' o '(3*(x**2)-7*x) / 2'")
		fun = input("\nAhora,dime, que función quieres calcular. :3\nTú: Mi función será f(x) = ")
		try:
			integral_trapecio(a,b,inval,fun)
			break
		except:
			print("\nPor favor repítelo, asegúrate de que escribiste adecuadamente la función y es continua en el intervalo. D:")
	esperar()

trapecio()