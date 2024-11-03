'''
@author: Sebastián
'''

x=input("Dame una función en el formato sen(x) o cos(x)> ")
valor=input("Dame el valor a evaluar x = >")
#sin(x)
#cos(x)

if(x.index("sin" >=0)):
    print("Evaluando senos", x, valor)
if(x.index("cos" >=0)):
    print("Evaluando cosenos", x, valor)

