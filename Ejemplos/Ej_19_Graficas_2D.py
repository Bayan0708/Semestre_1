#Graficas 2D

import matplotlib.pyplot as plt
import numpy as np


#Ejemplo 1
# plt.plot([ 1, 2, 3, 4],[ 1, 4,9, 16],'r')
# plt.xlabel ('Eje X')
# plt.ylabel ('Eje Y')
# plt.show()

# Ejemplo 2
# t = np.arange(0.,5.,0.2)
# plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
# plt.axis([-1,6,-10,5**3])
# plt.grid()
# plt.show()

#Ejemplo 3
# x = [1,2,3,4]
# y = [1,4,9,16]
# px = [1,1,2,3,4,4]
# py = [0,1,4,9,16,0]

# plt.plot (x,y,'r')
# plt.fill (px, py, 'g', alpha=0.5)
# plt.xlabel ('Eje X')
# plt.ylabel ('Eje Y')
# plt.title ('Relleno del área bajo la curva')
# plt.grid()
# plt.show()


#Ejemplo 4
x = [1,2,3,4]
y = [1,4,9,16]
py = [0,1,4,9,16,0]
px = x[0:len(x)]
px.append (x[len (x-1)])
px.insert (0,x[0])
print(px)

plt.plot (x,y,'r')
plt.fill (px, py, 'g', alpha=0.5)
plt.xlabel ('Eje X')
plt.ylabel ('Eje Y')
plt.title ('Relleno del área bajo la curva')
plt.grid()
plt.show()