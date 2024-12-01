# 2) Desarrolle y pruebe las siguientes funciones en un archivo separado al de trabajo práctico sobre
# diccionarios:
# - Desarrolle una función que genere una matriz de 9 filas por 9 columnas con números aleatorios del 1
# al 9 inclusive.
import random

def inicializar_matriz(filas:int, columnas:int, valor_inicial:any = None)->list:
    """
    """
    lista = []
    for _ in range(filas):
        fila = [valor_inicial] * columnas
        lista += [fila]
    
    return lista

def generar_matriz_aleatoria(matriz:list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = random.randint(1, 9)

mi_matriz = inicializar_matriz(9, 9)
#print(mi_matriz)
generar_matriz_aleatoria(mi_matriz)
#print(mi_matriz)

# - Desarrolle una función que guarde la matriz generada aleatoriamente en un archivo con formato CSV,
# donde las columnas están separadas por comas y las filas por saltos de línea (\n).

# def guardar_archivo_CSV(matriz:list, ruta:str):
#     with open(ruta, "w") as archivo:
#         for i in range(len(matriz)):
#             for j in range(len(matriz[i])):
#                 if j == len(matriz[i])-1:
#                     dato_a_escribir = str(matriz[i][j])+"\n"
#                 else:
#                     dato_a_escribir = str(matriz[i][j])+","
#                 archivo.writelines(dato_a_escribir)

#Versión de Ulises
# def guardar_archivo_CSV(matriz:list,ruta:str):
#     with open(ruta,"w") as archivo:
#         for fila in matriz:
#             archivo.write(str(fila).strip("[").strip("]"))
#             archivo.write("\n")
#             #archivo.write(str(fila).strip("[").strip("]")+"\n") -> En una sola línea

# guardar_archivo_CSV(mi_matriz, "Clase17/matriz.csv")

# 2) Desarrolle y pruebe las siguientes funciones en un archivo separado al de trabajo práctico sobre
# diccionarios:
# - Desarrolle una función que genere una matriz de 9 filas por 9 columnas con números aleatorios del 1
# al 9 inclusive.
import random

def inicializar_matriz(filas:int, columnas:int, valor_inicial:any = None)->list:
    """
    """
    lista = []
    for _ in range(filas):
        fila = [valor_inicial] * columnas
        lista += [fila]
    
    return lista

def generar_matriz_aleatoria(matriz:list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = random.randint(1, 9)

mi_matriz = inicializar_matriz(9, 9)
#print(mi_matriz)
generar_matriz_aleatoria(mi_matriz)
#print(mi_matriz)

# - Desarrolle una función que guarde la matriz generada aleatoriamente en un archivo con formato CSV,
# donde las columnas están separadas por comas y las filas por saltos de línea (\n).

def guardar_archivo_CSV(matriz:list, ruta:str):
    with open(ruta, "w") as archivo:
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if j == len(matriz[i])-1:
                    dato_a_escribir = str(matriz[i][j])+"\n"
                else:
                    dato_a_escribir = str(matriz[i][j])+","
                archivo.writelines(dato_a_escribir)

#Versión de Ulises
def guardar_archivo_CSV(matriz:list,ruta:str):
    with open(ruta,"w") as archivo:
        for fila in matriz:
            archivo.write(str(fila).strip("[").strip("]"))
            archivo.write("\n")
            #archivo.write(str(fila).strip("[").strip("]")+"\n") -> En una sola línea

# guardar_archivo_CSV(mi_matriz, "clase 18 viernes 8 de noviembre/matriz.csv")

# - Desarrolle una función para poder leer un archivo CSV y a partir de su contenido construir una matriz en Python.

def importar_matriz(ruta:str)->list:

    with open(ruta, "r") as mi_archivo:
        datos = mi_archivo.read()
        # print(datos, type(datos))
        
        lista_filas = datos.strip("\n").split("\n")
        lista_vacia = []
        for fila in lista_filas:
            lista_numeros = fila.split(", ")
            for i in range(len(lista_numeros)):
                lista_numeros[i] = int(lista_numeros[i])
            lista_vacia += [lista_numeros]
    return lista_vacia

def mostrar_matriz(matriz:list)->None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()


matriz = importar_matriz("clase 18 viernes 8 de noviembre/matriz.csv")
# print(matriz)
mostrar_matriz(matriz)



""""
1)-Desarrolle una función que reciba una matriz de números enteros y guarde todos los números pares
en un archivo de texto con el nombre “numeros_pares.txt” y todos los números impares en otro
archivo con el nombre “numeros_impares.txt”.
2)- Desarrolle una función que pueda agregar su nombre, apellido y división al final del archivo que
guarda la matriz aleatoria.
"""

def guardar_pares_y_impares(matriz:list, ruta:str, criterio:str) -> None:
    with open(ruta, "w") as mi_archivo:
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if criterio == "par" and matriz[i][j] % 2 == 0:
                    mi_archivo.write(str(matriz[i][j]) + " ")
                elif criterio == "impar" and matriz[i][j] % 2 == 1:
                    mi_archivo.write(str(matriz[i][j]) + " ")

guardar_pares_y_impares(matriz, "clase 18 viernes 8 de noviembre/pares.txt", "par")

guardar_pares_y_impares(matriz, "clase 18 viernes 8 de noviembre/impares.txt", "impar")