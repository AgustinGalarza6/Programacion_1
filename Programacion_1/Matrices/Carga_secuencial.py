# Carga secuencial
#   Creamos las funciones para inicializar la matriz y mostrarla

#   Por medio de los ciclos for anidados realizamos la carga de manera secuencial
#   Pidiendole los datos al usuario.

'''
def mostrar_matriz -> Es una funcion que nos permite mostrar la matriz en el formato correspondiente (eliminando el formato de 3 listas anidadas)
def inicializar_matriz -> Es una funcion que se encarga de reservar espacio en memoria a la hora de crear una lista (matriz) vacia.

'''

def mostrar_matriz(matriz:list) -> None:
    for fil in range(len(matriz)):
        #for col in range(len(matriz[0]))
        for col in range(len(matriz[fil])):
            print(matriz[fil][col],end=" ")
        print("")

def inicializar_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas): # Cantidad de filas = 3 (se crean 3 filas)
        fila = [valor_inicial] * cantidad_columnas # Cantidad de columnas = 3 y valor_inicial = 0
        # fila = [0,0,0] -> Osea que dependiendo las filas y las columnas va rellenando con 0 y almacenandolo en "fila"
        # Resultado_matriz = [
#               [0,0,0],
#               [0,0,0],
#               [0,0,0]
#             ]
        matriz += [fila]
    return matriz

# Pasamos los parametros de la matriz a inicializar:
# matriz = (filas(3), columnas(3), valor inicial(N/D))

matriz = inicializar_matriz(3,3,"N/D")
# matriz = [
#     [N/D,N/D,N/D],
#     [N/D,N/D,N/D],
#     [N/D,N/D,N/D]
# ]

print("MATRIZ INICIADA ANTES DE LA CARGA")
mostrar_matriz(matriz)

# Llenamos la matriz de manera secuencial pidiendo los datos al usuario
for fil in range(len(matriz)):
    #for col in range(len(matriz[0]))
    for col in range(len(matriz[fil])):
        #Pedir el dato
        numero = int(input(f"Ingrese el numero (fila: {fil}) (col: {col}): "))
        #Guardar el dato en la matriz
        matriz[fil][col] = numero

print("\nMATRIZ DESPUES DE LA CARGA: ")
mostrar_matriz(matriz)