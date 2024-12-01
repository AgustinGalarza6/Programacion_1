import random


def verificar_fila(matriz, fila, numero):
    """
    Verifica si el número está en la fila indicada.
    """
    for valor in matriz[fila]:
        if valor == numero:
            return False
    return True


def verificar_columna(matriz, columna, numero):
    """
    Verifica si el número está en la columna indicada.
    """
    for i in range(9):
        if matriz[i][columna] == numero:
            return False
    return True


def calcular_inicio_submatriz(indice):
    """
    Calcula el índice inicial de la submatriz 3x3 correspondiente.
    """
    if indice < 3:
        return 0
    elif indice < 6:
        return 3
    return 6


def verificar_submatriz(matriz, fila, columna, numero):
    """
    Verifica si el número está en la submatriz 3x3 correspondiente.
    """
    inicio_fila = calcular_inicio_submatriz(fila)
    inicio_columna = calcular_inicio_submatriz(columna)

    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_columna, inicio_columna + 3):
            if matriz[i][j] == numero:
                return False
    return True


def validar_celda(matriz, fila, columna, numero):
    """
    Valida si un número puede colocarse en la celda dada.
    """
    fila_valida = verificar_fila(matriz, fila, numero)
    columna_valida = verificar_columna(matriz, columna, numero)
    submatriz_valida = verificar_submatriz(matriz, fila, columna, numero)

    if fila_valida and columna_valida and submatriz_valida:
        return True
    return False


def buscar_celda_vacia(matriz):
    """
    Encuentra la primera celda vacía en la matriz.
    """
    for fila in range(9):
        for columna in range(9):
            if matriz[fila][columna] == 0:
                return fila, columna
    return -1, -1  # Indicador de que no hay celdas vacías


def inicializar_tablero():
    """
    Crea un tablero vacío.
    """
    return [[0 for _ in range(9)] for _ in range(9)]


def rellenar_celda(matriz, fila, columna, numero):
    """
    Coloca un número en la celda especificada.
    """
    matriz[fila][columna] = numero


def limpiar_celda(matriz, fila, columna):
    """
    Limpia una celda devolviéndola a 0.
    """
    matriz[fila][columna] = 0


def intentar_resolver(matriz, fila, columna):
    """
    Intenta resolver el tablero desde la posición actual.
    """
    for numero in range(1, 10):
        if validar_celda(matriz, fila, columna, numero):
            rellenar_celda(matriz, fila, columna, numero)
            if resolver_tablero(matriz):
                return True
            limpiar_celda(matriz, fila, columna)
    return False


def resolver_tablero(matriz):
    """
    Resuelve el tablero de Sudoku.
    """
    fila, columna = buscar_celda_vacia(matriz)
    if fila == -1:
        return True  # No hay celdas vacías, está resuelto
    return intentar_resolver(matriz, fila, columna)


def rellenar_celdas_iniciales(matriz, celdas_iniciales):
    """
    Llena un número específico de celdas iniciales en el tablero.
    """
    contador = 0
    while contador < celdas_iniciales:
        fila = random.randint(0, 8)
        columna = random.randint(0, 8)
        numero = random.randint(1, 9)
        if matriz[fila][columna] == 0 and validar_celda(matriz, fila, columna, numero):
            rellenar_celda(matriz, fila, columna, numero)
            contador += 1


def vaciar_celdas(matriz, celdas_a_vaciar):
    """
    Vacía celdas del tablero para generar un desafío.
    """
    celdas_vaciadas = 0
    while celdas_vaciadas < celdas_a_vaciar:
        fila = random.randint(0, 8)
        columna = random.randint(0, 8)
        if matriz[fila][columna] != 0:
            limpiar_celda(matriz, fila, columna)
            celdas_vaciadas += 1


def generar_tablero_sudoku():
    """
    Genera un tablero de Sudoku válido.
    """
    matriz = inicializar_tablero()
    celdas_iniciales = random.randint(12, 20)
    rellenar_celdas_iniciales(matriz, celdas_iniciales)

    if not resolver_tablero(matriz):
        return generar_tablero_sudoku()

    celdas_a_vaciar = random.randint(40, 50)
    vaciar_celdas(matriz, celdas_a_vaciar)

    return matriz


def mostrar_tablero(matriz):
    """
    Muestra el tablero de Sudoku en formato visual.
    """
    for fila in range(9):
        if fila % 3 == 0 and fila != 0:
            print("-" * 21)
        for columna in range(9):
            if columna % 3 == 0 and columna != 0:
                print("|", end=" ")
            valor = matriz[fila][columna]
            print(valor if valor != 0 else ".", end=" ")
        print()


# Ejemplo de uso
if __name__ == "__main__":
    tablero = generar_tablero_sudoku()
    print("Tablero generado:")
    mostrar_tablero(tablero)
