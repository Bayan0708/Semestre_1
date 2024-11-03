from math import *


print('Metodo de Bisseccion\n')
ec=input('De la funcion a resolver: ')  
x1=float(input('de el extremo inferior del intervalo aproximado: '))
x2=float(input('de el extremo superior del intervalo aproximado: '))
errordeseado=float(input('De el error deseado: '))
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
    error=abs(x2-x1)
    if error<errordeseado:
        break
 
print("La raíz es ",xmed, " y las iteraciones fueron ",i-1,)
print ('La raíz es',xmed)




# from math import sin,cos,tan,asin,acos,atan,sqrt,log,exp
# from math import sinh,cosh,tanh,asinh,acosh,atanh
# print('Metodo de Bisseccion\n')
# ec=input('De la funcion a resolver: ')  
# x1=float(input('de el extremo inferior del intervalo aproximado: '))
# x2=float(input('de el extremo superior del intervalo aproximado: '))
# errordeseado=float(input('De el error deseado: '))
 

# def f(x):
#     return eval(ec)

 
# while True:
#     xmed=(x1+x2)/2
#     fxmed=f(xmed)
#     if fxmed==0.0:
#         break
 
#     if (f(x1)*f(xmed))<0:
#         x1=x1
#         x2=xmed
#     else:
#         x1=xmed
#         x2=x2
#     error=abs(x2-x1)
#     if error<errordeseado:
#         break
 

# print ('La raíz es',xmed)
# input(' ')