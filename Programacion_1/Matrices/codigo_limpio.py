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

def inicializar_tablero_9x9(cantidad_filas: int = 9, cantidad_columnas: int = 9, valor_inicial: int = 0) -> list:
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
def obtener_posicion_inicial_de_fila(fila:int) -> int:
    posicion_de_fila = 0
    if fila < 3:
        posicion_de_fila = 0
    elif fila < 6:
        posicion_de_fila = 3
    else:
        posicion_de_fila = 6
    return posicion_de_fila

#---------------------------------------------------------------------------------------------------------------------------------
def obtener_posicion_inicial_de_columna(columna:int) -> int:
    posicion_de_columna = 0
    if columna < 3:
        posicion_de_columna = 0
    elif columna < 6:
        posicion_de_columna = 3
    else:
        posicion_de_columna = 6
    return posicion_de_columna

#---------------------------------------------------------------------------------------------------------------------------------

def verificar_numero_repetido_en_submatriz(matriz:list, numero:int, posicion_inicial_en_fila:int, posicion_inicial_en_columna:int) -> bool:
    bandera_numero_repetido = False
    for indices_fila in range(posicion_inicial_en_fila, posicion_inicial_en_fila + 3):
        for indices_columna in range(posicion_inicial_en_columna, posicion_inicial_en_columna + 3):
            if matriz[indices_fila][indices_columna] == numero:
                bandera_numero_repetido = True
                break
        if bandera_numero_repetido == True:
            break
    return bandera_numero_repetido

#---------------------------------------------------------------------------------------------------------------------------------

def lista_posibles_numeros(desde: int = 1, hasta: int = 9) -> list:
    posibles_numeros = list(range(desde, hasta + 1))
    return posibles_numeros

#---------------------------------------------------------------------------------------------------------------------------------

def es_numero_valido(matriz: list, numero: int, fila: int, columna: int) -> bool:
    numero_valido = False
    if (not verificar_numero_repetido_en_fila(matriz, numero, fila) and
        not verificar_numero_repetido_en_columna(matriz, numero, columna) and
        not verificar_numero_repetido_en_submatriz(matriz, numero, obtener_posicion_inicial_de_fila(fila), obtener_posicion_inicial_de_columna(columna))):
        matriz[fila][columna] = numero
        numero_valido = True
    return numero_valido

#---------------------------------------------------------------------------------------------------------------------------------

def resolver_sudoku(matriz: list, posibles_numeros: list) -> bool:
    solucion_encontrada = True
    for fila in range(9):
        for columna in range(9):
            if matriz[fila][columna] == 0:
                solucion_encontrada = False 
                random.shuffle(posibles_numeros)
                for numero in posibles_numeros:
                    if es_numero_valido(matriz, numero, fila, columna):
                        matriz[fila][columna] = numero
                        if resolver_sudoku(matriz, posibles_numeros):
                            solucion_encontrada = True
                            break
                        matriz[fila][columna] = 0
                break
        if solucion_encontrada == False:
            break
    return solucion_encontrada

#---------------------------------------------------------------------------------------------------------------------------------

tablero = inicializar_tablero_9x9()
posibles_numeros = lista_posibles_numeros()
resolver_sudoku(tablero, posibles_numeros)
mostrar_matriz_sudoku(tablero)
print("\n")

#---------------------------------------------------------------------------------------------------------------------------------

def mostrar_tablero_oculto(matriz: list, celdas_ocultas: list, caracter: str) -> None:
    """
    Muestra el tablero de Sudoku con ciertas celdas ocultas.
    
    Parámetros:
        matriz (list): Matriz de Sudoku.
        celdas_ocultas (list): Lista de posiciones (fila, columna) de las celdas ocultas.
        caracter (str): Carácter que se mostrará en las celdas ocultas.
    """
    for fila in range(len(matriz)):
        if fila % 3 == 0 and fila != 0:
            print("-" * 21)
        for columna in range(len(matriz[fila])):
            if columna % 3 == 0 and columna != 0:
                print("|", end=" ")

            if (fila, columna) in celdas_ocultas:
                print(caracter, end=" ")
            else:
                print(matriz[fila][columna], end=" ")
        print()

#---------------------------------------------------------------------------------------------------------------------------------

def generar_celdas(tamaño_del_tablero: int = 9) -> list:
    """
    Genera una lista de todas las posiciones del tablero.
    
    Args:
        tamaño_del_tablero (int): Tamaño del tablero (n x n).
        
    Returns:
        list: Lista de tuplas con las posiciones del tablero.
    """
    celdas = []
    for fila in range(tamaño_del_tablero):
        for columna in range(tamaño_del_tablero):
            celdas.append((fila, columna))
    return celdas

#---------------------------------------------------------------------------------------------------------------------------------

def seleccionar_celdas_ocultas(celdas, celdas_a_ocultar):
    """
    Selecciona aleatoriamente las celdas que se van a ocultar.
    
    Args:
        celdas (list): Lista de celdas disponibles.
        celdas_a_ocultar (int): Número de celdas a ocultar.
        
    Returns:
        list: Lista de celdas seleccionadas para ocultar.
    """
    celdas_a_ocultar = random.sample(celdas, celdas_a_ocultar)
    return celdas_a_ocultar

#---------------------------------------------------------------------------------------------------------------------------------

def ocultar_datos_matriz_segun_dificultad(matriz: list) -> list:
    """
    Función para ocultar celdas aleatorias en el tablero según el nivel de dificultad.
    
    Args:
        matriz (list): Matriz del Sudoku (9x9) que se desea modificar.
        
    Returns:
        list: Matriz modificada con celdas ocultas.
    """
    # Solicitar la dificultad
    parametro = input("Seleccione la dificultad (facil, intermedio, dificil): ").lower()
    dificultades = ("facil", "intermedio", "dificil")
    
    # Validación de la dificultad ingresada
    while parametro not in dificultades:
        print("Dificultad no valida.")
        parametro = input("Ingrese nuevamente la dificultad: ").lower()

    total_celdas = 81
    # Determinamos cuántas celdas ocultar según la dificultad
    if parametro == "facil":
        celdas_a_ocultar = int(total_celdas * 0.20)  # 20% de las celdas = 16
    elif parametro == "intermedio":
        celdas_a_ocultar = int(total_celdas * 0.40)  # 40% de las celdas = 32
    elif parametro == "dificil":
        celdas_a_ocultar = int(total_celdas * 0.60)  # 60% de las celdas = 48

    # Generar todas las celdas del tablero
    celdas = generar_celdas()

    # Seleccionar aleatoriamente las celdas que se van a ocultar
    celdas_ocultas = seleccionar_celdas_ocultas(celdas, celdas_a_ocultar)

    # Ocultar las celdas en la matriz
    for fila, columna in celdas_ocultas:
        matriz[fila][columna] = "*"  # Valor de celda oculta
    return matriz

#---------------------------------------------------------------------------------------------------------------------------------

tablero = inicializar_tablero_9x9()
posibles_numeros = lista_posibles_numeros()
resolver_sudoku(tablero, posibles_numeros)
tablero = ocultar_datos_matriz_segun_dificultad(tablero)
mostrar_matriz_sudoku(tablero)

#---------------------------------------------------------------------------------------------------------------------------------

def jugar_sudoku(matriz, fila, columna, numero, celdas_ocultas):
    """
    Permite al usuario ingresar un número en la celda seleccionada del Sudoku.

    Parámetros:
        matriz (list): La matriz del Sudoku (9x9) que se desea modificar.
        fila (int): Fila de la celda seleccionada.
        columna (int): Columna de la celda seleccionada.
        numero (int): Número a ingresar en la celda seleccionada.
        celdas_ocultas (set): Conjunto de celdas que están ocultas y no se pueden modificar.

    Retorna:
        tuple: (matriz, errores) - La matriz actualizada y el número de errores.
    """
    if not es_celda_modificable(fila, columna, celdas_ocultas):
        print("No puedes modificar esta celda.")
        return matriz, 0

    if not ingreso_del_usuario_valido(numero):
        print("Número inválido. Debe ser entre 1 y 9.")
        return matriz, 0

    return colocar_numero(matriz, fila, columna, numero)

#---------------------------------------------------------------------------------------------------------------------------------

def es_celda_modificable(valor_en_fila, valor_en_columna, celdas_ocultas):
    """
    Verifica si la celda seleccionada se puede modificar.

    Parámetros:
        fila (int): Fila de la celda seleccionada.
        columna (int): Columna de la celda seleccionada.
        celdas_ocultas (set): Conjunto de celdas que están ocultas y no se pueden modificar.

    Retorna:
        bool: True si la celda es modificable, False en caso contrario.
    """
    celda_modificable = False
    if (valor_en_fila, valor_en_columna) not in celdas_ocultas:
        celda_modificable = True
    return celda_modificable

#---------------------------------------------------------------------------------------------------------------------------------

def ingreso_del_usuario_valido(numero_ingresado:int, bandera_numero_valido:bool) -> bool:
    """
    Verifica si el número ingresado es válido (entre 1 y 9).

    Parámetros:
        numero (int): El número que se desea verificar.

    Retorna:
        bool: True si el número es válido, False en caso contrario.
    """
    bandera_numero_valido = True
    if numero_ingresado not in (posibles_numeros):
        bandera_numero_valido = False
    return bandera_numero_valido

#---------------------------------------------------------------------------------------------------------------------------------

def colocar_numero(matriz, fila, columna, numero):
    """
    Intenta colocar un número en la celda especificada.

    Parámetros:
        matriz (list): La matriz del Sudoku.
        fila (int): Índice de la fila donde se desea colocar el número.
        columna (int): Índice de la columna donde se desea colocar el número.
        numero (int): El número a colocar.

    Retorna:
        tuple: (matriz, errores) - La matriz actualizada y el número de errores.
    """
    if es_numero_valido(matriz, numero, fila, columna):
        matriz[fila][columna] = numero
    return matriz

#---------------------------------------------------------------------------------------------------------------------------------

def contar_errores(matriz, numero, fila, columna) -> int:
    contador = 0
    if es_numero_valido(matriz, numero, fila, columna) == False:
        contador += 1
    return contador

#---------------------------------------------------------------------------------------------------------------------------------

# import pygame

# def manejar_input_sudoku(matriz, fila_seleccionada, columna_seleccionada):
#     """
#     Maneja la entrada de números en una celda vacía del Sudoku.

#     Parámetros:
#         matriz (list): La matriz del Sudoku (9x9).
#         fila_seleccionada (int): Fila de la celda seleccionada.
#         columna_seleccionada (int): Columna de la celda seleccionada.

#     Retorna:
#         None: Esta función no retorna ningún valor.
#     """
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key in range(pygame.K_1, pygame.K_10):  # Verifica si la tecla es un número del 1 al 9
#                 numero = event.key - pygame.K_0  # Convierte la tecla a su valor numérico
#                 if matriz[fila_seleccionada][columna_seleccionada] == " ":  # Verifica si la celda está vacía
#                     if es_numero_valido(matriz, numero, fila_seleccionada, columna_seleccionada):
#                         matriz[fila_seleccionada][columna_seleccionada] = numero  # Coloca el número en la celda
#             elif event.key == pygame.K_ESCAPE:
#                 print("Entrada cancelada.")
#             else:
#                 event.key == pygame.K_DELETE:
#                 matriz[fila_seleccionada][columna_seleccionada] = " "