#Programación orientad a objetos

#ejemplo1

class coche:
    ruedas = 4
    def __init__(self, color, aceleracion) -> None:
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    def acelera (self):
        self.velocidad = self.velocidad + self.aceleracion
    def frena (self):
        v = self.velocidad - self.aceleracion
        if v < 0:
            v = 0
        self.velocidad = v

c1 = coche ('rojo', 20)
c2 = coche ('axul', 30)
c1.frena()
c2.acelera()

print('El coche ',c1.color, 'tiene una velocidad de ', c1.velocidad)
print('El coche ',c2.color, 'tiene una velocidad de ', c2.velocidad)