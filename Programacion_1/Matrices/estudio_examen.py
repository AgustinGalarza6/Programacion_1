import random

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mostrar_matriz(matriz:list) -> None:
    """
    La función recorre la matriz y muestra cada elemento, separando los elementos de la misma fila
    por un espacio, y comenzando una nueva línea para cada fila. Dandole asi un formato visual fácil de leer, sin corchetes ni comas.
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
    La funcion 'es_un_numero_valido_ascii' se encarga de verificar si la cadena ingresada (str) representa un digito valido utilizando el codigo ASCII.
        - Implementemos una bandera la cual sera 'True' si todos los caracteres son digitos, 'False' en caso contrario.
    Por ultimo esta funcion retorna el valor correspondiente dependiendo si es valido o no el ingreso del usuario.
    """
    bandera_es_valido = True
    for digito in numero:
        if ord(digito) < 48 or ord(digito) > 57:
            bandera_es_valido = False
    return bandera_es_valido

def solicitar_entero(mensaje: str, minimo: int = 3, maximo: int = 15) -> int:
    """
    La funcion solicitar_entero se encarga de solicitarle al usuario el ingreso de un numero.
    Asegurandose tambien de que:
        - El valor ingresado sea un digito mediante verificacion por ASCII.
        - El valor ingresado este entre minimo y maximo que es el rango permitido.
        - En el caso de que el valor NO sea valido, se le pide que lo ingrese de nuevo.
            - Una vez que es valido el valor:
            - Parceamos el dato ingresado "str" a "int"
        - Por ultimo devolvemos el valor ingresado si esta dentro del rango permitido. (De 3 al 15)
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
    Esta función genera una lista de letras mayúsculas aleatorias utilizando el código ASCII
    para que no ponga valores no válidos dentro de la lista. (Solo de la 'A' a la 'Z' mayúsculas).
        - Definimos una lista vacia para llenar posteriormente.
        - Le pasamos el valor 'numero_ingresado' a la función (este número proviene de la opción A)
        para que genere la lista con la longitud correspondiente.
        - Le pasamos el valor 'rango_minimo_valido' y 'rango_maximo_valido' que sería '65' y '90'
        para que genere la lista de letras mayúsculas entre 'A' y 'Z'.
        - Cargamos la lista con las letras generadas aleatoriamente
    Retornamos la lista generada.
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
    La funcion 'imprimir_lista' se encarga de imprimir la lista generada en la función anterior si ha sido generada.
        - Mediante un FOR iteramos la longitud de la lista y vamos iterando los elementos
        - Al momento de ir mostrando los elementos siempre y cuando el indice no sea el ultimo vamos mostrando un guion (-) entre cada elemento. (A - B - C - D)
        - Cuando el FOR llega al ultimo indice de la lista generada, muestra solamente el ultimo elemento de la lista sin guion.
            - Tener en cuenta que sino se agrega el else, el último elemento de la lista no se muestra.
            - Tener tambien en cuenta que no se le agrega ningun tipo de 'sep' para no imprimir nada deseado.
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
    Esta funcion se encarga de validar que el usuario ingrese una sola letra mayúscula entre 'A' y 'Z'.
        - Se le pide al usuario que ingrese una sola letra mayúscula por consola.
        - Se valida que el valor ingresado sea una sola letra mayúscula entre 'A' y 'Z' mediante codigo ascii.
        - Se retorna el valor ingresado si es una sola letra comprendida entre la 'A' a la 'Z'.
        - En caso de no ser valida o ingresa mas de 1 letra mayuscula, se le solicitara al usuario nuevamente la letra.
            - En caso de no ser valido el ingreso imprimira [ERROR]
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
    Esta funcion se encarga de buscar dentro de la lista anteriormente generada en el punto B:
        - La letra deseada por el usuario.
    Para ello:
        - Generamos una lista vacia llamada coincidencias que almacena los indices de dicha letra a buscar dentro de la lista.
        - Se ejecuta un FOR para analizar el contenido de la lista generada en el punto B.
        - Por medio de una condicion 'if' a medida que recorre el 'FOR' comparamos si la letra del indice es igual a la letra del usuario
        - Si la condicion se cumple, se agrega el indice a la lista 'coincidencias'.
        - Finalmente retornamos la lista 'coincidencias' con los indices donde se encuentra la letra.
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
    Esta funcion se encarga de solicitar al usuario que ingrese 'ASC' o 'DESC' para ordenar la lista segun se requiera.
        - Se le pide al usuario que ingrese 'ASC' o 'DESC' por consola.
            - En caso de no ser valido se solicitara al usuario de nuevo el criterio a realizar.
        - Se valida que el valor ingresado sea 'ASC' o 'DESC'.
        - Por ultimo si el criterio de ordenamiento es correcto, retorna el valor correspondiente.
    """
    while True:
        criterio = input(mensaje)
        if criterio == "ASC" or criterio == "DESC":
            return criterio

def copiar_lista(lista: list) -> list:
    """
    Esta funcion se encarga de copiar la lista original para no perderla.
        - Se crea una lista vacia para copiar la lista original del punto B.
        - Se recorre con un 'FOR' el contenido de la lista original.
        - Se agrega cada elemento de la lista original a la nueva lista.
        - Y por ultimo retornamos la lista copiada.
    """
    lista_copiada = []
    for elemento in lista:
        lista_copiada += [elemento]  # Agrega cada elemento de la lista original a la nueva lista
    return lista_copiada

def ordenar_lista(lista_mayusculas: list, criterio: str) -> list:
    """
    Esta funcion es la que se encarga de ordenar la lista copiada sin afectar la original y devuelve la lista según el criterio especificado por el usuario
    ('ASC' para ascendente y 'DESC' para descendente).
        - Se crea una variable 'lista ordenada' donde se almacenara la lista original 'lista_mayusculas'.
        - El primer 'FOR' se encarga re recorrer todos los elementos dentro de la longitud de la lista, MENOS el ultimo.
        - El segundo 'FOR' se encarga de recorrer desde el segundo elemento hasta el ultimo elemento de la lista.
            - Dicho proceso se ejecuta para realizar correcta y efectivamente el swapeo de la lista a ordenar.
        - Se implmenta una condicion 'if' la cual se encarga de ir evaluando que:
            - Si el criterio es 'ASC' y la condicion 'if' se cumple que el elemento en [i] es mayor al de [j] intercambiara los valores, de no ser asi no y seguira recorriendo el bucle.
            - Si el criterio es 'DESC' y la condicion 'if' se cumple que el elemento en [i] es menor al de [j] intercambiara los valores, de no ser asi no y seguira recorriendo el bucle.
        - Por ultimo retornamos la lista ordenada.
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
    Esta funcion se encarga de solicitar numeros por consola (2 numeros) por lo cual:
        - Primero se generara una lista vacia para rellenar.
        - Luego se hara un 'FOR' que almacena la cantidad de numeros que se solicitaron y sean validos
        - Se validaran los datos ingresados por consola mediante:
            - Un 'if' que verifique primero que sea un digito valido segun codigo ascii.
                - De ser correcto parcearemos el digito de str a int y lo almacenaremos en 'numero'
            - Posteriormente el segundo if validara que el 'numero' este entre el rango de 3 y 10.
                - De ser valido, lo cargara a la lista
                - De no ser valido, se le notificara al usuario que vuelva a ingresar un digito comprendido entre 3 y 10.
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

def crear_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:int) -> list:
    """
    Esta funcion se encarga de crear una matriz vacia con la cantidad de filas y columnas que se le solicitaron
    en el punto anterior con las filas y columnas especificadas por el usuario
    """
    matriz_vacia = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz_vacia += [fila]
    return matriz_vacia

def llenar_matriz_random(matriz_vacia:list, desde:int, hasta:int) -> None:
    """
    Esta funcion se encarga de rellenar la matriz vacia generada en la anterior funcion auxiliar.
        - Medira las dimensiones de la matriz
        - Por ultimo rellenara la matriz con valores aleatorios
            - Especificandole al random.randint que llene cada espacio vacio con numeros comprendidos entre 1 y 9 (Desde - Hasta)
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
    Esta funcion se encarga de mostrar la matriz con el formato especificado en el enunciado
        - Se encerrara la matriz completa dentro de " | " para marcar de donde a donde es la matriz
        - Se dividira la matriz en "-" (renglones) entre filas.
        - Implementamos un 'if == posicion_inicial' para que si estamos parados en la primera columna de la matriz.
            - Y en caso de estar parados en la primera columna de la matriz, se imprimira un ' | ' y espacio.
            - Seguido de eso empieza la impresion de la matriz ya generada en el punto G
        - El segundo 'if' va evaluando evaluando que:
            - A medida que va imprimiendo preguntamos si llegamos al ultimo elemento de la fila y no es la ultima columna de la matriz:
                - Entonces imprimos un ' | ' directamente un end = " "  que por defecto salta a la fila siguiente (\n) hasta llegar a la ultima columna de la matriz generada.
        - El else se encarga de que cuando se llegue al ultimo elemento de la matriz, se imprimira el ultimo ' | ' al final de todo.
        - El ultimo 'if' se encarga de que siempre que no sea la ultima fila  de la matriz imprima un renglon entre fila y fila
            - Reservando para cada elemento 4 renglones y al final + 1 para que llegue a rellenar todo el largo completo de la matriz.
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