def mostrar_matriz(matriz:list) -> None:
    for fil in range(len(matriz)):
        #for col in range(len(matriz[0]))
        for col in range(len(matriz[fil])):
            print(matriz[fil][col],end=" ")
        print("")

# Un array bidimensional es una estructura de datos que contiene elementos dispuestos en filas y columnas formando una tabla -> Se lo conoce como matriz
# A las matrices se las representa en python como listas anidadas (Una lista que dentro tiene un conjunto de listas)

#Declaración

matriz_a = [
    [1,5],
    [-3,6],
    [2,1]
]

#matriz_a = [[1,5],[-3,6],[2,1]] -> NO (por ahora)

matriz_b = [
    [4,3,9],
    [-1,2,-5]
]

matriz_c = [
    [4,7,1],
    [-2,5,9],
    [5,4,-4]
]

#Acceso

#Acceder a todos los elementos de la fila 1
print(matriz_c[0]) 
#Acceder a todos los elementos de la fila 2
print(matriz_c[1])
#Acceder a todos los elementos de la última fila
print(matriz_c[2])
#Acceder a todos los elementos de la última fila
#print(matriz_c[-1]) #SOLO FUNCIONA EN PYTHON

#Acceder a cada uno de los elementos

#FILA 1
print(matriz_c[0][0]) #Accedo al elemento ubicado en la fila 1 columna 1
print(matriz_c[0][1]) #Accedo al elemento ubicado en la fila 1 columna 2
print(matriz_c[0][2]) #Accedo al elemento ubicado en la fila 1 última columna
# print(matriz_c[0][-1]) #Accedo al elemento ubicado en la fila 1 última columna -> SOLO FUNCIONA EN PYTHON

#FILA 2
print(matriz_c[1][0]) #Accedo al elemento ubicado en la fila 2 columna 1
print(matriz_c[1][1]) #Accedo al elemento ubicado en la fila 2 columna 2
print(matriz_c[1][2]) #Accedo al elemento ubicado en la fila 2 última columna

#FILA 3
print(matriz_c[2][0]) #Accedo al elemento ubicado en la fila 3 columna 1
print(matriz_c[2][1]) #Accedo al elemento ubicado en la fila 3 columna 2
print(matriz_c[2][2]) #Accedo al elemento ubicado en la fila 3 última columna
#print(matriz_c[-1][-1]) #Accedo al elemento ubicado en la fila 3 última columna -> SOLO FUNCIONA EN PYTHON

#MOSTRAR MIS MATRICES

#print(matriz_c) NOOOOOOOOOOOOO

mostrar_matriz(matriz_c)

print("MATRIZ ANTES DE MODIFICAR")
mostrar_matriz(matriz_c)


#Modificacion

matriz_c[0][0] = 5 #Cambio el 4 por un 5
matriz_c[0][1] = 4 #Cambio el 7 por un 4
matriz_c[1][0] = 3 #Cambio el -2 por un 3
matriz_c[2][2] = -2 #Cambio el -4 por un -2
# matriz_c[-1][-1] = -2 #Cambio el -4 por un -2 -> SOLO FUNCIONA EN PYTHON

print("MATRIZ DESPUES DE MODIFICAR")
mostrar_matriz(matriz_c)
