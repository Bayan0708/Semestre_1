'''
@author: Sebastián González Juárez
'''
#La siguiente paquetería permite obtener valores de varios tipos de funciones
from math import*

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