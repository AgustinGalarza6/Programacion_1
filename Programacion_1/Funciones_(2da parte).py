# 1) Desarrollar una función que determine si un número entero es par o impar. Debe recibir un número por
# parámetro y devolver True en caso de que sea par, de lo contrario devolverá False.

# def determinar_par_o_impar(numero:int) -> bool:
#     '''
#     Esta funcion recibe un numero entero y devuelve True si es par, False en caso contrario
#         Segun que ingrese el usuario retornara un mensaje informando si es par o impar.
#     '''
#     if numero % 2 == 0:
#         print(f"El numero {numero} es par")
#     else:
#         print(f"El numero {numero} es impar")


# 2) Desarrollar una función que permita validar un número entero. Deberá recibir por parámetro el número a
# validar, y dos números que representan el rango mínimo y máximo permitido. Devolverá True en caso de
# ser válido, False de lo contrario.

def validar_entero_en_rango(numero:int, minimo:int, maximo:int) -> bool:
    '''
    La funcion determina si un numero se encuentra dentro de un rango determinado por dos enteros
        Recibe: 
            numero (int): representa el numero a analizar
            minimo (int): representa el minimo permitido
            maximo (int): representa el maximo permitido
        Devuelve: 
            validacion (bool): True o False dependiendo de si el numero se encuentra dentro del rango
    '''
    if type(numero) != int:
        return False
    else:
        if type(numero) == int and type(minimo) == int and type(maximo) == int:
            if numero >= minimo and numero <= maximo:
                validacion = True
            else:
                validacion = False
    return validacion



# 3) Desarrollar una función que se encargue de solicitar un número entero al usuario, validarlo (reutilizando la
# función del punto anterior) y retornar el número validado y transformado a entero. Deberá recibir por
# parámetro un mensaje que se le mostrará al usuario y los rangos de validación.

def solicitar_entero(mensaje:str, minimo:int, maximo:int) -> int:
    numero = (input(mensaje))
    flag = True
    
    for digito in numero:
        if ord(digito) < 48 or ord(digito) > 57:
            flag = False
            break

    if flag == True:
        # Si la bandera es True, parceamos el numero a int
        numero = int(numero)
    
    while flag == False:
        # Si la bandera es False, pedimos un nuevo numero indefinidamente.
        numero = input(mensaje)

    while validar_entero_en_rango(numero, minimo, maximo) != True:
        # Si el numero no esta dentro del rango minimo y maximo, pedimos un nuevo numero
        numero = int(input(mensaje))

    return numero

# 4) Desarrollar una función que se encargue de solicitar una cadena de caracteres al usuario, validarla y
# retornar la misma. Deberá recibir como parámetro un mensaje para indicarle al usuario y 1, 2 o 3 cadenas
# de caracteres que representarán las opciones válidas de ingreso.

def validar_characteres(mensaje: str, opcion_valida_1:str, opcion_valida_2: None, opcion_valida_3: None) -> str:
    '''
    Solicita una cadena de caracteres al usuario, la valida contra un conjunto de opciones válidas,
    y la devuelve si es válida. Pide la entrada hasta que sea una de las opciones válidas.

    Recibe:
        mensaje (str): el mensaje que se mostrará al usuario.
        opciones_validas (str): uno o más valores válidos que la entrada debe coincidir.

    Devuelve:
        str: la cadena de caracteres validada.
    '''
    cadena = input(mensaje)

    while cadena != opcion_valida_1 and cadena != opcion_valida_2 and cadena != opcion_valida_3:
        cadena = input(mensaje)
    return cadena


# Ejemplo de uso
# print(validar_characteres("Ingresa una cadena: ", "hola", "amigo", "mundo"))


# 5) Desarrollar una función que se encargue de medir el largo de una cadena de caracteres, deberá recibir por
# parámetro la cadena de caracteres a evaluar y devolverá un número entero representando la longitud de
# la cadena recibida.

def longitud_cadena(cadena:str) -> int:
    contador = 0
    for i in cadena:
        contador += 1
    return contador

cadena = "Amigo, sos un fenomeno"
print(longitud_cadena(cadena))

# -----------------------------------------------------------------------------------------

# def longitud_cadena(cadena:str) -> int:
#     for cantidad_de_letras in range (1, len(cadena)):
#         cantidad_de_letras += 1
#     return f"Tu cadena de caracteres tiene: {cantidad_de_letras} letras"


# 6) Desarrollar una función que determine si un número que recibirá por parámetro es primo. Si es primo
# deberá devolver un True, de lo contrario False.

def es_primo(numero:int) -> bool:
    divisores = 0
    for i in range (1, numero + 1):
        if numero % i == 0:
            divisores += 1

    if divisores == 2:
        print("Es primo")
    else:
        print("No es primo")

# # Ejemplo de uso
# numero = int(input("Ingresa un número: "))
# es_primo(numero)

# 7) Desarrollar una función que recibirá un número entero por parámetro, y devolverá el resultado del
# factorial de ese número.

def factorial(numero: int) -> str:
    # Factorial de 0 es 1.
    if numero == 0:
        return "El factorial de 0 es: 1"
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        return f"El factorial de {numero} es: {factorial}"

# # Ejemplo de uso
# numero = int(input("Ingresa un número: "))
# print(factorial(numero))

# 8) Desarrollar una función que reciba un carácter y determine si ese carácter está comprendido entre a…z o
# A…Z, en caso afirmativo devolverá True, de lo contrario False.

def determinar_caracter(caracter:str) -> bool:
    if(ord(caracter) >= 97 and ord(caracter) <= 122) or (ord(caracter) >= 65 and ord(caracter) <= 90):
        return True
    else:
        print("Este caracter no esta comprendido entre a...z o A…Z")

# # Ejemplo de uso
# caracter = input("Ingresa un caracter: ")
# print(determinar_caracter(caracter))

# 9) Desarrollar una función que reciba un carácter y determine si ese carácter está comprendido entre 0…9,
# devolverá un valor boolean indicando si el carácter recibido es numérico o no.

def es_char_numerico(caracter: str) -> bool:
    # while caracter == "":
    #     print("No ingresaste ningún carácter")
    #     caracter = input("Ingresa un carácter: ")

    if ord(caracter) >= 48 and ord(caracter) <= 57:
        return True
    else:
        print("El carácter no es numérico.")

# # Ejemplo de uso
# caracter = input("Ingresa un carácter: ")
# print(es_char_numerico(caracter))


# 10) Desarrollar una función que verifique el DNI de una persona, la misma recibirá una cadena de caracteres
# (se asume que solamente contiene caracteres numéricos). Si la cantidad de caracteres es menor a 6 o
# mayor a 8, retornara False. Si la cantidad de caracteres está comprendida entre 6 y 8 devolverá True.

def verificar_DNI(cadena: str) -> bool:
    contador_DNI = 0
    for num in cadena:
        contador_DNI += 1

    if (contador_DNI >= 6) and (contador_DNI <= 8):
        return True
    else:
        return False

# def verificar_DNI2(cadena: str) -> bool:
#     if (longitud_cadena(cadena) >= 6) or (longitud_cadena(cadena) > 8):
#         return True
#     else:
#         print("La longitud de tu DNI no es valida.")

# # Ejemplo de uso
# cadena = input("Ingresa tu DNI: ")
# print(verificar_DNI(cadena))

# 11) Desarrollar una función que complete el número de DNI de una persona. Recibirá una cadena de
# caracteres (se asume que solamente contiene caracteres numéricos), deberá medirla y completar con ceros
# a la izquierda hasta llegar a un total de 8 caracteres, y devolviendo la cadena resultante. Ej: Se ingresa
# “123456”, y devolverá “00123456”.

# def completar_DNI (cadena: str) -> str:
#     while len(cadena) < 8:
#         cadena = "0" + cadena
#     return f"Tu DNI es completo es: {cadena}"

# Ejemplo de uso
# cadena = input("Ingresa tu DNI: ")
# print(completar_DNI(cadena))

def completar_DNI2 (cadena: str, total_digitos: int = 8, relleno: str = "0") -> str:
    numero = total_digitos - longitud_cadena(cadena)
    cadena_a_rellenar = ""
    for _ in range(numero):
        cadena_a_rellenar += relleno

    return cadena_a_rellenar + cadena

# cadena = input("Ingresa tu DNI: ")
# print(completar_DNI2(cadena))

# 12) Desarrollar una función que transforme una cadena de caracteres numérica a su equivalente en letras.
# Recibirá por parámetro la cadena a transformar y devolverá el resultado en letras. Ej: “987” ->
# "novecientos ochenta y siete". Como máximo tomar el número más grande de 3 dígitos.

def convertir_numero_a_palabra(n):
    # Variables para las partes del número
    palabra = ""
    centena = n // 100
    decena = (n % 100) // 10
    unidad = n % 10
    
    # Manejo de centenas
    if centena == 1:
        if decena == 0 and unidad == 0:
            palabra += "cien"
        else:
            palabra += "ciento"
    elif centena == 2:
        palabra += "doscientos"
    elif centena == 3:
        palabra += "trescientos"
    elif centena == 4:
        palabra += "cuatrocientos"
    elif centena == 5:
        palabra += "quinientos"
    elif centena == 6:
        palabra += "seiscientos"
    elif centena == 7:
        palabra += "setecientos"
    elif centena == 8:
        palabra += "ochocientos"
    elif centena == 9:
        palabra += "novecientos"

    if palabra and (decena != 0 or unidad != 0):
        palabra += " "
    
    # Manejo de decenas especiales (10-19)
    if decena == 1:
        if unidad == 0:
            palabra += "diez"
        elif unidad == 1:
            palabra += "once"
        elif unidad == 2:
            palabra += "doce"
        elif unidad == 3:
            palabra += "trece"
        elif unidad == 4:
            palabra += "catorce"
        elif unidad == 5:
            palabra += "quince"
        elif unidad == 6:
            palabra += "dieciséis"
        elif unidad == 7:
            palabra += "diecisiete"
        elif unidad == 8:
            palabra += "dieciocho"
        elif unidad == 9:
            palabra += "diecinueve"
        return palabra  # Retornar aquí porque decenas especiales no tienen unidades separadas
    
    # Manejo de decenas normales (20, 30, ..., 90)
    if decena == 2:
        palabra += "veinte"
    elif decena == 3:
        palabra += "treinta"
    elif decena == 4:
        palabra += "cuarenta"
    elif decena == 5:
        palabra += "cincuenta"
    elif decena == 6:
        palabra += "sesenta"
    elif decena == 7:
        palabra += "setenta"
    elif decena == 8:
        palabra += "ochenta"
    elif decena == 9:
        palabra += "noventa"
    
    # Manejo de la conjunción "y"
    if decena > 2 and unidad != 0:
        palabra += " y "

    # Manejo de unidades
    if unidad == 1 and decena != 1:
        palabra += "uno"
    elif unidad == 2 and decena != 1:
        palabra += "dos"
    elif unidad == 3 and decena != 1:
        palabra += "tres"
    elif unidad == 4 and decena != 1:
        palabra += "cuatro"
    elif unidad == 5 and decena != 1:
        palabra += "cinco"
    elif unidad == 6 and decena != 1:
        palabra += "seis"
    elif unidad == 7 and decena != 1:
        palabra += "siete"
    elif unidad == 8 and decena != 1:
        palabra += "ocho"
    elif unidad == 9 and decena != 1:
        palabra += "nueve"
    
    # Caso para cero solo si no hay centenas ni decenas
    if n == 0:
        palabra = "cero"
    
    return palabra

# Ejemplo de uso
# numero = int(input("Ingresa un número del 0 al 999: "))
# print(numero_a_palabra(numero))