# 6- Desarrollar un programa que cuente con un menú y las siguientes opciones:
# a) Generar una matriz con números aleatorios. Las dimensiones y los rangos de números se deben pasar
# por parámetros de la función generadora. No se debe poder acceder a las demás opciones si la matriz
# no fue generada.
# b) Mostrar la matriz generada.
# c) Determinar si la matriz contiene series de números consecutivos (en horizontal o en vertical).
# d) Determinar la cantidad total de series (las series de números consecutivos de más de dos números
# cuentan como una sola).
# e) Determinar el largo de la serie más corta, y mostrar todas las series de ese largo.
# f) Determinar el largo de la serie más larga, y mostrar todas las series de ese largo.
# g) Salir

import random

def crear_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:int) -> list:
    matriz = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def mostrar_matriz(matriz:list) -> None:
    for fil in range(len(matriz)):
        #for col in range(len(matriz[0]))
        for col in range(len(matriz[fil])):
            print(matriz[fil][col],end=" ")
        print("")

def llenar_matriz_random(matriz_vacia:list, desde:int, hasta:int) -> None:
    """
    """
    for i in range(len(matriz_vacia)):
        for j in range(len(matriz_vacia[i])):
            matriz_vacia[i][j] = random.randint(desde, hasta)


def recorrer_matriz_horizontal(matriz:list) -> None:
    for a in range(len(matriz)):
        for b in range (len(matriz[a])):
            # print(matriz[a][b],end=" ")
            print("recorriendo horizontal")
            buscar_numeros_consecutivos(matriz[a])

def recorrer_matriz_vertical(matriz:list) -> None:
    for a in range(len(matriz)):
        for b in range(len(matriz[a])):
            # print(matriz[b][a], end=" ")
            print("recorriendo vertical")
            buscar_numeros_consecutivos(matriz[b])

def buscar_numeros_consecutivos(fila:list) -> None:
    for posicion in range(len(fila)-1):
        valor_actual = fila[posicion]
        valor_siguiente = fila[posicion + 1]
        # Verificamos si son consecutivos
        if valor_actual == valor_siguiente - 1:
            print(f"{valor_actual}, {valor_siguiente} son consecutivos")
        # else:
        #     print(f"{valor_actual}, {valor_siguiente} no son consecutivos")


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def main():
    while True:
        print("1) Generar una Matriz con numeros aleatorios")
        print("2) Mostrar Matriz generada")
        print("3) Determinar si la matriz contiene series de números consecutivos (en horizontal o en vertical).")
        print("4) Determinar la cantidad total de series (las series de números consecutivos de más de dos números")
        print("5) Determinar el largo de la serie más corta, y mostrar todas las series de ese largo.")
        print("6) Determinar el largo de la serie más corta, y mostrar todas las series de ese largo.")
        print("7) Salir")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":
            matriz = crear_matriz(5, 5, 0)
            llenar_matriz_random(matriz, 1, 9)
            print("Matriz generada correctamente!\n")
        elif opcion == "2":
            print("Matriz generada: \n")
            mostrar_matriz(matriz)
        elif opcion == "3":
            recorrer_matriz_vertical(matriz)
            recorrer_matriz_horizontal(matriz)
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        elif opcion == "6":
            pass
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion inválida. Por favor seleccione nuevamente.")


if __name__ == "__main__":
    main()