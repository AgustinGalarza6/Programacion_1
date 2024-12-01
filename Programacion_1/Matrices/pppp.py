# def generar_rango(inicio, fin):
#     """Genera un rango de números desde inicio hasta fin (sin incluir fin)."""
#     return range(inicio, fin)

# def generar_celdas(filas, columnas):
#     """Genera una lista de celdas en un tablero de filas x columnas."""
#     celdas = []
#     for fila in filas:
#         for columna in columnas:
#             celdas.append((fila, columna))
#     return celdas

# def obtener_celdas_tablero(filas:list, columnas:list, tamano_filas:int=10, tamano_columnas=10):
#     """
#     Obtiene todas las celdas de un tablero de tamaño tamano x tamano.
#     """
#     filas = generar_rango(1, tamano_filas)
#     columnas = generar_rango(1, tamano_columnas)
#     return generar_celdas(filas, columnas)

def generar_rango(inicio, fin):
    """Genera un rango de números desde inicio hasta fin (sin incluir fin)."""
    return range(inicio, fin)

def generar_celdas(filas, columnas):
    """Genera una lista de celdas en un tablero de filas x columnas."""
    celdas = []
    for fila in filas:
        for columna in columnas:
            celdas.append((fila, columna))
    return celdas

def obtener_celdas_tablero(filas=None, columnas=None, tamano_filas=10, tamano_columnas=10):
    """
    Obtiene todas las celdas de un tablero de tamaño tamano x tamano.

    Parámetros:
        filas (list o range, opcional): Lista o rango que define las filas del tablero.
        columnas (list o range, opcional): Lista o rango que define las columnas del tablero.
        tamano_filas (int, opcional): Tamaño predeterminado de filas si no se pasa `filas`.
        tamano_columnas (int, opcional): Tamaño predeterminado de columnas si no se pasa `columnas`.

    Retorna:
        list: Lista de celdas como pares (fila, columna).
    """
    if filas is None:
        filas = generar_rango(1, tamano_filas + 1)
    if columnas is None:
        columnas = generar_rango(1, tamano_columnas + 1)

    return generar_celdas(filas, columnas)

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


# Ejemplo de uso
filas = generar_rango(1, 10)
columnas = generar_rango(1, 10)
celdas = obtener_celdas_tablero(filas, columnas)

mostrar_matriz_sudoku(celdas)