# # Desarrollar una funcion que reciba como parametros fecha actual y fecha de nacimiento, y retorne la edad.

# # Solicitamos día de nacimiento del usuario y lo validamos.
# dia_de_nacimiento = input('Ingrese en qué día nació (En números): ')
# while not dia_de_nacimiento.isdigit():
#     print("[ERROR] Ingrese un número válido.")
#     dia_de_nacimiento = input("Ingrese de nuevo su día de nacimiento (En números): ")
# dia_de_nacimiento = int(dia_de_nacimiento)

# # Solicitamos el mes en que nació del usuario y lo validamos.
# mes_de_nacimiento = input('Ingrese en qué mes nació (En números): ')
# while not mes_de_nacimiento.isdigit():
#     print("[ERROR] Ingrese un número válido.")
#     mes_de_nacimiento = input('Ingrese de nuevo en qué mes nació (En números): ')
# mes_de_nacimiento = int(mes_de_nacimiento)

# # Solicitamos año de nacimiento del usuario y lo validamos.
# año_de_nacimiento = input('Ingrese en qué año nació (En números): ')
# while not año_de_nacimiento.isdigit():
#     print("[ERROR] Ingrese un número válido.")
#     año_de_nacimiento = input("Ingrese de nuevo en qué año nació (En números): ")
# año_de_nacimiento = int(año_de_nacimiento)

# # Solicitamos día actual
# dia_actual = input('Ingrese qué fecha es hoy (En números): ')
# while not dia_actual.isdigit():
#     print("[ERROR] Ingrese un número válido.")
#     dia_actual = input("Ingrese de nuevo el día actual (En números): ")
# dia_actual = int(dia_actual)

# # Solicitamos mes actual
# mes_actual = input('Ingrese qué mes es (En números): ')
# while not mes_actual.isdigit():
#     print("[ERROR] Ingrese un número válido.")
#     mes_actual = input("Ingrese de nuevo el mes actual (En números): ")
# mes_actual = int(mes_actual)

# # Solicitamos año actual
# año_actual = input('Ingrese el año actual (En números): ')
# while not año_actual.isdigit():
#     print("[ERROR] Ingrese un número válido.")
#     año_actual = input("Ingrese de nuevo el año actual (En números): ")
# año_actual = int(año_actual)

# # Funcion de calculo de edad.
# def calculo_edad():
#     '''
#     En esta funcion lo que vamos a hacer es solicitar los datos necesarios sobre en que fecha nacio
#     el usuario y en que fecha actual se encuentra de manera individual.

#         Logrando asi que por medio de un pedido invidual para cada cosa podamos parcear de STR a INT.

#         La funcion de calculo_edad se encarga de tomar los datos del año actual y de nacimiento ya parceados
#         para poder hacer el calculo y nos returne por resultado final que edad tiene nuestro usuario.
#     '''
#     edad_actual_usuario = año_actual - año_de_nacimiento
#     return f"\nLa edad del usuario es {edad_actual_usuario} años"

# print(calculo_edad())


# 1) Desarrollar una función que reciba como parámetros fecha actual y fecha de nacimiento; y retorne la edad.

def extraer_string(cadena:str, desde:int, hasta:int) -> str:
    contador = 1
    resultado = ""
    for letra in cadena:
        if contador >= desde and contador <= hasta:
            resultado += letra 
        contador += 1
    
    return resultado

# extraer_string("02-09-2024", 7, 10)
def mostrar_edad(fecha_nacimiento:str, fecha_actual:str) -> int:
    '''
    pide una fecha de nacimiento y fecha actual
        muestra la edad actual del usuario    
    '''
    # (02-09-2024)
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
    
print(mostrar_edad("04-11-2000", "02-09-2024"))