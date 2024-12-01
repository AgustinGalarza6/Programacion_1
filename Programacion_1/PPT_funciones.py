# chr() ---> convierte un entero en un caracter
# ord() ---> convierte un caracter en un entero


def extraer_string(cadena:str, desde:int, hasta:int) -> str:
    '''
    Esta funcion se encarga de recorrer una cadena de strings y extraer un pedazo de la cadena
    que se desee, indicandole de donde hasta donde se hara la extracción.
    - Retorna como resultado la porcion del string que se quiere extraer.
    '''
    contador = 1
    resultado = ""
    for letra in cadena:
        if contador >= desde and contador <= hasta:
            resultado += letra 
        contador += 1
    
    return resultado

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mostrar_edad(fecha_nacimiento:str, fecha_actual:str) -> int:
    '''
    Esta funcion recibe como parametros las fecha de nacimiento y fecha actual
        - Retorna la edad actual del usuario por medio de la resta entre la fecha actual y la fecha de nacimiento
        - En caso de que la resta de las fechas de el resultado, pero, previo a su cumpleaños
        (osea que da 24 pero todavia en ese año no cumplio años) se le resta 1 año.
        - Finaliza retornando la edad de la persona.
    '''
    dia_nacimiento = extraer_string(fecha_nacimiento, 1, 2)
    mes_nacimiento = extraer_string(fecha_nacimiento, 4, 5)
    año_nacimiento = extraer_string(fecha_nacimiento, 7, 10)

    dia_actual = extraer_string(fecha_actual, 1, 2)
    mes_actual = extraer_string(fecha_actual, 4, 5)
    año_actual = extraer_string(fecha_actual, 7, 10)

    edad = int(año_actual) - int(año_nacimiento)

    if (mes_actual < mes_nacimiento) or (mes_actual == mes_nacimiento and dia_actual < dia_nacimiento):
        edad -= 1

    return edad

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mostrar_vehiculo(patente:str) -> str:
    '''
    Esta funcion recibe una patente como parametro
        - Verifica si es una moto o un auto
        - Retorna tipo de vehiculo
    '''
    letra1 = extraer_string(patente, 1, 1)
    
    if ord(letra1) > 47 and ord(letra1) < 58:
        vehiculo = "Moto"
    else:
        vehiculo = "Auto"

    return vehiculo

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

def determinar_par_o_impar(numero:int) -> bool:
    '''
    Esta funcion recibe un numero entero y devuelve True si es par, False en caso contrario
        Segun que ingrese el usuario retornara un mensaje informando si es par o impar.
    '''
    if numero % 2 == 0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

def valor_maximo(n1, n2, n3):
    '''
    Máximo de tres números:
    Esta función llamada "valor_maximo" recibe tres números (o más) como argumentos y devuelva el mayor de los tres o mas numeros.
    '''
    if n1 > n2 and n1 > n3:
        numero_maximo = n1
    elif n2 > n1 and n2 > n3:
        numero_maximo = n2
    else:
        numero_maximo = n3
    return f"El valor maximo es: {numero_maximo}"


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

def valor_minimo(n1:str, n2:str, n3:str)-> str:
    '''
    Máximo de tres números:
    Esta función llamada "valor_minimo" recibe tres números (o más) como argumentos y devuelva el menor de los tres o mas numeros.
    '''
    if n1 < n2 and n1 < n3:
        numero_minimo = n1
    elif n2 < n1 and n2 < n3:
        numero_minimo = n2
    else:
        numero_minimo = n3
    return f"El valor minimo es: {numero_minimo}"

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

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


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

def solicitar_entero(mensaje:str, minimo:int, maximo:int) -> int:
    '''
    Esta funcion solicita un dato del usuario y lo valida
    si esta dentro del rango minimo y maximo.
        - Por un lado tenemos la validacion para corroborar que el ingreso sea un numero con el FOR
        - Si la flag es True, osea que es un numero, lo parceamos a int
        - Si la flag es False, osea que no es un numero, pedimos un nuevo numero mediante el ciclo While
        - Por ulitmo si todo esta correcto, pasamos a corroborar con el ultimo While el rango minimo y maximo
        a ver si el numero ingresado esta dentro del rango valido.
    '''
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

    return f"El numero {numero} es valido"

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

def longitud_cadena(cadena:str) -> int:
    '''
    Esta funcion se encarga de medir una cadena str
        - Retorna como resultado la longitud de la cadena
    '''
    contador = 0
    for i in cadena:
        contador += 1
    return contador

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

def es_primo(numero:int) -> bool:
    '''
    Esta funcion se encarga de verificar si un numero es primo
        - Retorna como resultado True o False dependiendo de si el numero es primo o no
    '''
    divisores = 0
    for i in range (1, numero + 1):
        if numero % i == 0:
            divisores += 1

    if divisores == 2:
        print("Es primo")
    else:
        print("No es primo")

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

def factorial(numero: int) -> str:
    '''
    Esta funcion se encarga de calcular el factorial de un numero
        - Retorna como resultado el factorial del numero.
    '''
    # Factorial de 0 es 1.
    if numero == 0:
        return "El factorial de 0 es: 1"
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        return f"El factorial de {numero} es: {factorial}"

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

def determinar_caracter(caracter:str) -> bool:
    '''
    Esta funcion se encarga de verificar si el str ingresado es un caracter
        - Para ello, verificamos mediante codigo ascii y el operador logico OR
        si esta comprendido entre a...z (minuscula) o A…Z (mayuscula)
        - Retorna como resultado True si el caracter esta comprendido en a...z o A…Z
        - Retorna como resultado False si el caracter no esta comprendido en a...z o A…Z
    '''
    if(ord(caracter) >= 97 and ord(caracter) <= 122) or (ord(caracter) >= 65 and ord(caracter) <= 90):
        return True
    else:
        print("Este caracter no esta comprendido entre a...z o A…Z")

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

def es_char_numerico(caracter: str) -> bool:
    '''
    Esta funcion se encarga de determinar si un caracter es numerico o no
    Su verificacion la realizamos mediante codigo ascii a modo de validacion tambien para saber si es un numero int
        - Retorna como resultado True o False dependiendo de si el caracter es numerico o no
    '''
    if ord(caracter) >= 48 and ord(caracter) <= 57:
        return True
    else:
        print("El carácter no es numérico.")

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

def completar_DNI (cadena: str) -> str:
    '''
    Esta funcion se encarga de completar un DNI de 8 digitos.
        - Mientras que la cadena no sea de 8 digitos, la rellena con 0 al principio
        - Retorna finalmente el DNI completo.
    '''
    while len(cadena) < 8:
        cadena = "0" + cadena
    return f"Tu DNI es completo es: {cadena}"

'''
def completar_DNI2 (cadena: str, total_digitos: int = 8, relleno: str = "0") -> str:
    numero = total_digitos - longitud_cadena(cadena)
    cadena_a_rellenar = ""
    for _ in range(numero):
        cadena_a_rellenar += relleno

    return cadena_a_rellenar + cadena
'''

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

def hayar_max_min(n1:str, n2:str, n3:str, tipo:str) -> str:
    '''
    Esta funcion busca el MAX o MIN de 3 numeros dependiendo lo que se le indique
        - Si indicamos 3 numeros + 'min' nos retornara el valor minimo.
        - Si indicamos 3 numeros + 'max' nos retornara el valor maximo.
    Como mensaje final nos informa que numero de los ingresados es el maximo o minimo.
    '''
    if tipo == 'max':
        if n1 > n2 and n1 > n3:
            numero_extremo = n1
        elif n2 > n1 and n2 > n3:
            numero_extremo = n2
        else:
            numero_extremo = n3

    elif tipo == 'min':
        if n1 < n2 and n1 < n3:
            numero_extremo = n1
        elif n2 < n1 and n2 < n3:
            numero_extremo = n2
        else:
            numero_extremo = n3
    else:
        return "Tipo inválido. Usa 'max' o 'min'."

    return f"El valor {tipo}imo es: {numero_extremo}"

# Ejemplo de uso
# print(hayar_max_min(1900, 455, 222, 'min')) # En este ejemplo buscamos el minimo
# print(hayar_max_min(1900, 455, 222, 'max')) # En este ejemplo buscamos el maximo

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

def sumar(num_a:int, num_b:int)->int:
    '''
    Esta funcion calcula la suma de dos numeros
        Recibe:
        num_a (int) seria el primer numero a sumar
        num_b (int) seria el segundo numero a sumar
        Devuelve:
        suma (int) seria la suma de los numeros
    '''
    suma = num_a + num_b
    return suma

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

def restar(num_a:int, num_b:int)->int:
    '''
    Esta funcion calcula la resta de dos numeros
        Recibe:
        num_a (int) seria el primer numero a restar
        num_b (int) seria el segundo numero a restar
        Devuelve:
        resta (int) seria la resta de los numeros
    '''
    resta = num_a - num_b
    return resta

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

def multiplicar(num_a:int, num_b:int)->int:
    '''
    Esta funcion calcula la multiplicacion de dos numeros
        Recibe:
        num_a (int) seria el primer numero a multiplicacion
        num_b (int) seria el segundo numero a multiplicacion
        Devuelve:
        multiplicacion (int) seria la multiplicacion de los numeros
    '''
    multiplicacion = num_a * num_b
    return multiplicacion

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

def dividir(num_a:int, num_b:int)->float:
    '''
    Esta funcion calcula la division de dos numeros
        Recibe:
        num_a (int) seria el primer numero a division
        num_b (int) seria el segundo numero a division
        Devuelve:
        division (float) seria la division de los numeros
    '''
    division = None
    if num_b != 0:
        division = num_a / num_b
    return division

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

def calcular_resto(num_a:int, num_b:int)-> int:
    '''
    Esta funcion calcula el resto entre dos numeros
        Recibe:
        num_a (int) seria el primer numero 
        num_b (int) seria el segundo numero 
        Devuelve:
        resto(float) seria el resto entre  los numeros
        esta funcion sirve tanto como para enteros como para flotantes
    '''
    resto = None
    if num_b != 0:
        resto = num_a % num_b
    return resto

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

