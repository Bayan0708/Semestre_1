'''
@author: Sebastián González Juárez
'''
#La siguiente paquetería permite obtener valores de varios tipos de funciones
from math import*
import matplotlib.pyplot as plt


# Función: evaluando_copia_f. Lo que hace esta función es crear una copia de la función f que se pedirá en el programa.
# Como la función f la declaramos lista, la copia también lo será y de la cuál podemos editar sus valores de x.
# Esto es una manera con la cual no editaremos nuestra variable f y así poderla evaluar en los valores asignados.
# Usando la librería math, podemos evaluar en muchas funciones, lo cual hace muy útil el programa.

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
        a = float(input("\nDame la frontera inferior del intervalo: "))
        break
      except ValueError:
        print("\nInserta únicamente números reales")
    while True:
      try:
        b = float(input("\nDame la frontera superior del intervalo: "))
        break
      except ValueError:
        print("\nInserta únicamente números reales")
    if b >= a:
      break
    else:
     print("\nEl valor de la frontera inferior debe ser menor o igual que el valor de la frontera superior, introduce nuevamente tus datos")
a = a
b = b

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
h=(b-a)/n
Resultado=0

lista = []
lista1 = [] 

Resultado+=evaluando_copia_f(a)*(h/3)+evaluando_copia_f(b)*(h/3)
for i in range(1,n):
  x=a+i*h
  lista.append(x)
  if i%2==0:
    ef = evaluando_copia_f(x)
    lista1.append(ef)
    Resultado+=ef*(2*h/3)
  else:
    ef = evaluando_copia_f(x)
    lista1.append(ef)    
    Resultado+=ef*(4*h/3)
print ("\nLa aproximación del área bajo la curva de tu función, es = "+str( Resultado))



#Se crean 2 listas que nos ayudan a gráficar.
lista2 = lista
lista2.insert(0,a)
lista2.append (b)
lista3 = lista1
lista3.insert(0,0)
lista3.append (0)

#Datos de la gráfica.
plt.plot (lista,lista1,'indigo')
plt.fill(lista2 , lista3, 'darkviolet', alpha=0.5)
plt.xlabel('Eje X') # Etiqueta del eje X
plt.ylabel('Eje Y') # Etiqueta del eje Y
plt.title('Función y área debajo de la curva')
plt.grid() # se activa la malla
plt.show() # Se manda crear la gráfica