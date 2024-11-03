#Visual python

# import vpython as vp

#Ejemplo 1
#cubo= vp.box()

#Ejemplo 2
from vpython import *
# mysphere = sphere(radius=1,color = color.cyan)


from vpython import *

s1 = sphere( radius=0.1, pos=vector(0,0,0), color=color.cyan )
s2 = sphere( radius=0.2, pos=vector(1,0,0), color=color.red )
s3 = sphere( radius=0.2, pos=vector(0,1,0), color=color.green )
s4 = sphere( radius=0.2, pos=vector(0,0,1), color=color.blue )
b1 = box(pos=vector(0.0,0.5,0.5), size=vector(0.03, 1, 1),color=color.red)
b2 = box(pos=vector(0.5,0.5,0.0), size=vector(1, 1, 0.03),color=color.green)
b2 = box(pos=vector(0.5,0.0,0.5), size=vector(1, 0.03, 1),color=color.blue)