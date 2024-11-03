#Documentción

def miFuncion():
    """ Esta funcion imprime nada """
    print("Nada")

def areaRectangulo(base, altura):
    """Calcula el area de un rectangulo:param float base: La base del rectangulo:param float altura: La altura del rectangulo:return: El area del rectangulo:rtype: float"""
    return base*altura
area = areaRectangulo(6, 8)
print(area)