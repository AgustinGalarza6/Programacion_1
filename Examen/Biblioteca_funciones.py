import random

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mostrar_matriz(matriz:list) -> None:
    """
    Muestra los elementos de una matriz de forma legible, separando los elementos de cada fila por un espacio
    y comenzando una nueva linea para cada fila. 

    Parametros:
        matriz (lista): La matriz a mostrar.

    Retorna:
        None
    """
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            print(matriz[fil][col],end=" ")
        print("")


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# A) Solicitar al usuario el ingreso de un número entero por consola, validando su tipo de dato (mediante
# código ASCII) y su pertenencia al rango de 3 y 15, ambos inclusive.

def es_un_numero_valido_ascii(numero: str) -> bool:
    """
    Verifica si la cadena ingresada representa un digito valido utilizando el codigo ASCII.
    
    Parametros:
        numero (str): La cadena que se va a validar.

    Retorna:
        bool: True si la cadena contiene solo digitos validos, False en caso contrario.
    """
    bandera_es_valido = True
    for digito in numero:
        if ord(digito) < 48 or ord(digito) > 57:
            bandera_es_valido = False
    return bandera_es_valido

def solicitar_entero(mensaje: str, minimo: int = 3, maximo: int = 15) -> int:
    """
    Solicita al usuario el ingreso de un numero entero, validando que sea un digito y que este en el rango 
    permitido (minimo a maximo).
    
    Parametros:
        mensaje (str): Mensaje que se muestra al usuario para solicitar el numero.
        minimo (int): Valor minimo permitido. Por defecto es 3.
        maximo (int): Valor maximo permitido. Por defecto es 15.

    Retorna:
        int: El numero ingresado y validado.
    """
    while True:
        numero_ingresado = input(mensaje)
        if es_un_numero_valido_ascii(numero_ingresado):
            numero_ingresado = int(numero_ingresado)
            if (minimo <= numero_ingresado) and (numero_ingresado <= maximo):
                return numero_ingresado 
        print(f"[ERROR] El valor '{numero_ingresado}' no es un número valido o está fuera del rango ({minimo}-{maximo}).")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# B) Generar una lista de letras mayúsculas aleatorias (utilizar el código ASCII), con una longitud igual al
# número ingresado en la opción A (no se debe poder generar la lista si el número aún no fue ingresado).

def cargar_lista_con_mayusculas(numero_ingresado: int, rango_minimo_valido: int = 65, rango_maximo_valido: int = 90) -> list:
    """
    Genera una lista de letras mayusculas aleatorias entre 'A' y 'Z' con una longitud igual al numero ingresado.
    
    Parametros:
        numero_ingresado (int): Longitud de la lista que se va a generar.
        rango_minimo_valido (int): Codigo ASCII minimo para 'A'. Por defecto es 65.
        rango_maximo_valido (int): Codigo ASCII maximo para 'Z'. Por defecto es 90.

    Retorna:
        lista: Lista generada con letras mayusculas aleatorias.
    """

    lista_de_mayusculas = []
    for i in range(numero_ingresado):
        letra_aleatoria = chr(random.randint(rango_minimo_valido, rango_maximo_valido))  # Genera una letra aleatoria entre 'A' y 'Z'
        lista_de_mayusculas += [letra_aleatoria]
    return lista_de_mayusculas

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# C) Mostrar la lista generada, formateada de manera que sea entendible para el usuario (no se debe poder
# mostrar la lista si ésta aún no ha sido generada).

def imprimir_lista(lista:list)->None:
    """
    Imprime la lista generada en un formato legible, separando los elementos con un guion.
    
    Parametros:
        lista (list): Lista de elementos a imprimir.
    """
    for i in range(len(lista)):
        if i != (len(lista) - 1):
            print(lista[i], end= " - ")
        else:
            print(lista[i]) # Ultimo elemento de la lista.


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# D) Solicitar al usuario el ingreso de una letra mayúscula por consola, validando que sea una única letra entre
# la ‘A’ y la ‘Z’. Una vez validada, buscar la letra en la lista generada en la opción B e informar si existe o no.
# En caso de que exista, también informar en qué posiciones/índices se encuentran. No se debe poder
# acceder a esta opción si la lista aún no ha sido generada.

def solicitar_letra_mayuscula(mensaje: str) -> str:
    """
    Pide al usuario que ingrese una unica letra mayuscula y valida que este en el rango de 'A' a 'Z'.

    Parametros:
        mensaje (str): Mensaje que se muestra al usuario para solicitar la letra.

    Retorna:
        str: La letra ingresada y validada.
    """
    flag = False
    while True:
        letra_ingresada = input(mensaje)
        if (len(letra_ingresada) == 1) and ('A' <= letra_ingresada <= 'Z'):
            flag = True
            return letra_ingresada
        else:
            print(f"[ERROR] Ingrese una letra mayuscula nuevamente: ")


def buscar_letra_en_lista(lista_mayusculas: list, letra_ingresada: str) -> list:
    """
    Busca la letra ingresada en la lista generada y devuelve las posiciones donde se encuentra.

    Parametros:
        lista_mayusculas (list): Lista en la que se realizara la busqueda.
        letra_ingresada (str): Letra a buscar en la lista.

    Retorna:
        list: Lista de indices donde se encuentra la letra buscada.
    """
    coincidencias = []  # Lista para almacenar las posiciones donde se encuentra la letra
    for i in range(len(lista_mayusculas)):
        if lista_mayusculas[i] == letra_ingresada:
            coincidencias += [i]
    return F'La letra "{letra_ingresada}" se encuentra en la posicion: {coincidencias}'


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# E) Solicitar al usuario el ingreso de una cadena de caracteres “ASC” o “DESC” por consola y validarla. Luego,
# ordenar una COPIA de la lista generada en la opción B según el criterio ingresado por el usuario, y
# mostrarla. No se debe poder acceder a esta opción si la lista aún no ha sido generada y la lista original no
# debe ser modificada.

def solicitar_ordenamiento(mensaje: str) -> str:
    """
    Pide un criterio de ordenamiento al usuario ('ASC' o 'DESC') y lo valida.

    Parametros:
        mensaje (str): Mensaje que se muestra al usuario para solicitar el criterio.

    Retorna:
        str: Criterio de ordenamiento ingresado y validado.
    """
    while True:
        criterio = input(mensaje)
        if criterio == "ASC" or criterio == "DESC":
            return criterio

def copiar_lista(lista: list) -> list:
    """
    Crea una copia de la lista original para preservarla sin modificar.

    Parametros:
        lista (list): Lista que se va a copiar.

    Retorna:
        list: Copia de la lista original.
    """
    lista_copiada = []
    for elemento in lista:
        lista_copiada += [elemento]  # Agrega cada elemento de la lista original a la nueva lista
    return lista_copiada

def ordenar_lista(lista_mayusculas: list, criterio: str) -> list:
    """
    Ordena una copia de la lista segun el criterio especificado ('ASC' o 'DESC') y devuelve la lista ordenada.

    Parametros:
        lista_mayusculas (list): Lista de letras mayusculas a ordenar.
        criterio (str): Criterio de ordenamiento ('ASC' o 'DESC').

    Retorna:
        list: Lista ordenada segun el criterio especificado.
    """
    lista_ordenada = copiar_lista(lista_mayusculas)
    for i in range(len(lista_ordenada) - 1):
        for j in range(i + 1, len(lista_ordenada)):
            if (criterio == "ASC" and lista_ordenada[i] > lista_ordenada[j]) or (criterio == "DESC" and lista_ordenada[i] < lista_ordenada[j]):
                aux = lista_ordenada[i]
                lista_ordenada[i] = lista_ordenada[j]
                lista_ordenada[j] = aux
    return lista_ordenada


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# F) Solicitar al usuario el ingreso de dos (2) números enteros por consola, validando su tipo de dato
# (mediante código ASCII) y su pertenencia al rango de 3 a 10, ambos inclusive. El primer número
# representará la cantidad de filas, y el segundo, la cantidad de columnas.
# 1

def solicitar_numeros(cantidad:int, mensaje:str) -> list:
    """
    Solicita dos numeros enteros al usuario, validando su tipo de dato y su pertenencia al rango de 3 a 10.
    
    Parametros:
        cantidad (int): Cantidad de numeros a solicitar.
        mensaje (str): Mensaje que se mostrara al usuario para ingresar los numeros.

    Retorna:
        list: Lista con los numeros validos ingresados por el usuario.
    """
    lista = []
    for _ in range(cantidad):
        while True:
            numero = input(mensaje)
            if es_un_numero_valido_ascii(numero):
                numero = int(numero)
                if 3 <= numero <= 10:
                    lista += [numero]
                    break
            print("[ERROR] Ingrese un número válido entre 3 y 10.")
    return lista


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# G) Generar una matriz de números enteros aleatorios entre 1 y 9, utilizando los números ingresados en la
# opción F como cantidad de filas y columnas. No se debe poder acceder a esta opción si el usuario aún no
# ha ingresado la cantidad de filas y columnas.

def crear_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:int=0) -> list:
    """
    Crea una matriz vacia con la cantidad de filas y columnas especificadas por el usuario.

    Parametros:
        cantidad_filas (int): Cantidad de filas de la matriz.
        cantidad_columnas (int): Cantidad de columnas de la matriz.
        valor_inicial (int): Valor inicial para llenar la matriz (por defecto es 0).

    Retorna:
        list: Matriz vacia con las dimensiones solicitadas, llena de valores iniciales.
    """
    matriz_vacia = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz_vacia += [fila]
    return matriz_vacia

def llenar_matriz_random(matriz_vacia:list, desde:int, hasta:int) -> None:
    """
    Rellena la matriz vacia generada en la funcion crear_matriz con numeros aleatorios.

    Parametros:
        matriz_vacia (list): Matriz que sera llenada con valores aleatorios.
        desde (int): Valor minimo para los numeros aleatorios (inclusive).
        hasta (int): Valor maximo para los numeros aleatorios (inclusive).
    
    Retorna:
        None: Esta funcion no retorna ningun valor.
    """
    for i in range(len(matriz_vacia)):
        for j in range(len(matriz_vacia[i])):
            matriz_vacia[i][j] = random.randint(desde, hasta)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# H) Mostrar la matriz generada en la opción G, separando las filas entre sí con guiones medios (“-”) y las
# columnas con barras verticales (“|”). No se debe poder acceder a esta opción si la matriz aún no ha sido
# generada.

def mostrar_matriz_separada(matriz: list, posicion_inicial:int = 0) -> None:
    """
    Muestra la matriz generada, separando las filas con guiones medios y las columnas con barras verticales.

    Parametros:
        matriz (list): Matriz que se desea mostrar.
        posicion_inicial (int): Posicion inicial para la separacion de columnas (por defecto es 0).
    
    Retorna:
        None: Esta funcion no retorna ningun valor.
    """
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            if col == posicion_inicial:
                print("|", end=" ")
            print(matriz[fil][col], end=" ")
            if col != len(matriz[fil]) - 1: 
                print("|", end=" ")
            else:
                print("|")
        if fil != len(matriz) - 1:
            print("-" * (len(matriz[fil]) * 4 + 1))


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# I) Salir del programa.