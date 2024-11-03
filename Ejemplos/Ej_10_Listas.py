#Listas, Tuplas, Diccionarios

# lista_vacia=[]
# print(type(lista_vacia))
# lista_vacia=list()
# print(type(lista_vacia))
# lista=[1,2,3.5,"cuatro",["sublista", "dentro"],True, False]
# print(lista)


# a=[90, "Python", 3.87]
# print(a[0]) #90
# print(a[1]) #Python
# print(a[2]) #3.87

#modificar elementos
# a = [90, "Python", 3.87]
# a[0] = 1
# print(a)

#agregar elementos 
#append premite agregar uno valor nuevo, inset inserta  un elemen en la possción desada
# a = [90, "Python", 3.87]
# a.append("nuevo")
# a.insert(1, "insertado")
# print(a)


# eliminar elementos
# a = [90, "Python", 3.87, 8]
# a.pop() #elimina el último
# a.pop(1) # es igual a: del a[1]
# a.remove(90) # por su valor
# print(a) 


# 0 1 2 3 4 5
# a = [1, 2, 3, 4, 5, 6]
# print(a[0:2]) #[1, 2]
# print(a[2:6]) #[3, 4, 5, 6]
# print(a[0: -1])#[1, 2, 3, 4, 5]
# print(a[2:])

# lista = [5, 9, 10]
# for v in lista:
#     print(v)

# lista = [5, 9, 10]
# for index, l in enumerate(lista):
#     print(index, l)


# lista = [5, 9, 10]
# for i in range(0, len(lista)):
#     print(lista[i])


# #Invertir el orden de los elementos
# a = [1, 2, 3]
# a.reverse()
# print(a) #[3, 2, 1]

# #Ordenar los elementos de forma ascendente
# a = [3, 1, 2]
# a.sort()
# print(a) #[1, 2, 3]

# a = ["hola", "sebas", "amigo"]
# a.sort()
# print(a) 

# #Ordenar los elementos de forma descendente
# a = [3, 1, 2]
# a.sort(reverse=True)
# print(a) #[3, 2, 1]

# a = ["hola", "sebas", "amigo"]
# a.sort(reverse=True)
# print(a)


## Índice de un elemento
# a = ['a', 'b', 'c', 'd']
# print(a.index('b')) # 1
# a = [1, 1, 1, 1, 2, 1, 4, 5]
# print(a.index(1, 4)) #5

# #Número de apariciones de un elemento
# a = [3, 1, 2, 1]
# print(a.count(1)) #2

# #Tuplas

# a = (1, 3, 4)
# print(a) # (1, 3, 4)

# a = tuple([1, 3, 4])
# print(a) # (1, 3, 4)


#set

# s = set([5, 4, 6, 8, 8, 1])
# print(s) #{1, 4, 5, 6, 8}
# print(type(s)) #<class 'set'>

# s = {5, 4, 6, 8, 8, 1}
# print(s) #{1, 4, 5, 6, 8}
# print(type(s)) #<class 'set'>



# #Recorrer conjuntos
# s = set([5, 7, 7, 6, 8])
# for ss in s:
#     print(ss, end=", ") #8, 5, 6, 7,

# #Longitud del conjunto
# print(len(s)) # 4

#Saber si un elemento perteneceal conjunto
# s = set(["Guitarra", "Bajo"])
# print("Guitarra" in s) #True


#Diccionarios
# d1 = {
# "Nombre": "Sara",
# "Edad": 27,
# "Documento": 1003882
# }
# print(d1)
# #{'Nombre': 'Sara', 'Edad': 27, 'Documento': 1003882}

# d3 = dict(Nombre='Sara',
# Edad=27,
# Documento=1003882)




# lista = ["hola", "ei", "XD"]
# for v in lista:
#     print(v)