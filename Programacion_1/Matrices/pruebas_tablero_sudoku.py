import random

def mostrar_matriz_sudoku(matriz: list) -> None:
    """
    Muestra la matriz de Sudoku con separaciones de submatrices cada 3 filas y columnas.

    Parámetros:
        matriz (list): Matriz del Sudoku que se desea mostrar.

    Retorna:
        None: Esta función no retorna ningún valor.
    """
    for fila in range(len(matriz)):
        if fila % 3 == 0 and fila != 0:  # Separación horizontal cada 3 filas
            print("-" * 21)
        for columna in range(len(matriz[fila])):
            if columna % 3 == 0 and columna != 0:  # Separación vertical cada 3 columnas
                print("|", end=" ")
            print(matriz[fila][columna], end=" ")
        print()

#---------------------------------------------------------------------------------------------------------------------------------

def crear_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:int) -> list:
    """
    Esta función se encarga de crear una matriz vacía.
        Recibe:
            cantidad_filas (int): representa las filas que va a tener la matriz.
            cantidad_columans (int): representa las columnas que va a tener la matriz.

        Devuelve:
            matriz (list): la matriz creada.
    """
    matriz = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

#---------------------------------------------------------------------------------------------------------------------------------

def verificar_numero_repetido_en_fila(matriz: list, numero: int, fila: int) -> bool:
    """
    Verifica si un número está repetido en la fila especificada de la matriz de Sudoku.
    
    Parámetros:
        matriz (list): La matriz de Sudoku.
        numero (int): El número que se desea verificar.
        fila (int): Índice de la fila donde se desea verificar.
    
    Retorna:
        bool: True si el número está repetido en la fila, False en caso contrario.
    """
    
    resultado = False
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == numero:
            resultado = True
            break
    return resultado

#---------------------------------------------------------------------------------------------------------------------------------

def verificar_numero_repetido_en_columna(matriz: list, numero: int, columna: int) -> bool:
    """
    Verifica si un número está repetido en la columna especificada de la matriz de Sudoku.
    
    Parámetros:
        matriz (list): La matriz de Sudoku.
        numero (int): El número que se desea verificar.
        columna (int): Índice de la columna donde se desea verificar.
    
    Retorna:
        bool: True si el número está repetido en la columna, False en caso contrario.
    """
    
    resultado = False
    for i in range(len(matriz)):
        if matriz[i][columna] == numero:
            resultado = True
            break
    return resultado

#---------------------------------------------------------------------------------------------------------------------------------

def verificar_numero_repetido_en_submatriz(matriz:list, fila:int, columna:int, numero:int, posicion_inicial_en_fila:int, posicion_inicial_en_columna:int) -> bool:
    bandera_numero_repetido = False
    # Indice ij (0,0) de la matriz
    if (columna < 3) and (fila < 3):
        posicion_inicial_en_fila = 0 # seteamos el inicio en 0 de la fila
        posicion_inicial_en_columna = 0 # seteamos el inicio en 0 de la columna
    elif (columna < 6) and (fila < 6):
        posicion_inicial_en_fila = 3
        posicion_inicial_en_columna = 3
    else:
        posicion_inicial_en_fila = 6
        posicion_inicial_en_columna = 6
    
    for indices_fila in range(posicion_inicial_en_fila, posicion_inicial_en_fila + 3):
        for indices_columna in range(posicion_inicial_en_columna, posicion_inicial_en_columna + 3):
            if matriz[indices_fila][indices_columna] == numero:
                bandera_numero_repetido = True
                break
        if bandera_numero_repetido == True:
            break
    return bandera_numero_repetido # valor booleano

#----------------------------------------------------------------------------------------------------------------------------------

