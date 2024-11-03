from math import *

print('Metodo de Bisseccion\n')
ec=input('De la funcion a resolver: ')  
x1=float(input('de el extremo inferior del intervalo aproximado: '))
x2=float(input('de el extremo superior del intervalo aproximado: '))
Criteriodeconvergencia=float(input('Criterio de convergencia: '))
Criteriodeexactitud=float(input('Criterio de exactitud: '))

n=float(input("Número de iteraciones: "))
 

def f(x):
    return eval(ec)

i = 0
while i <= n :
    i=i+1
    xmed=(x1+x2)/2
    fxmed=f(xmed)
    if fxmed==0.0:
        break
 
    if (f(x1)*f(xmed))<0:
        x1=x1
        x2=xmed
    else:
        x1=xmed
        x2=x2
    error1=abs(x2-x1)
    error2=abs(f(xmed))
    if error1<Criteriodeconvergencia and error2<Criteriodeexactitud:
        break
 
print("La raíz es ",xmed, " y las iteraciones fueron ",i-1,)


