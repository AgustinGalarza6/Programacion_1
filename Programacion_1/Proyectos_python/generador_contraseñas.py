import string
import random

def generador_password(longitud:int) -> str:
    '''
    Genera una contraseña aleatoria de una longitud dada

    import string nos trae la libreria que contiene todas las letras, numero y simbolos
    import random la vamos a implementar para que el codigo este siempre generando nuevas opciones aleatorias

    Recibe:
        longitud (int): la longitud de la contraseña que se generara segun desee el usuario
    Retorna:
        str: la contraseña generada
    '''
    caracteres = string.ascii_letters + string.digits # Llamamos a la libreria string (podriamos agregarle el string.punctuation pero en este caso no queremos emplearlo.)
    password = "" # Declaramos la variable vacia donde posteriormente se guardara la contraseña

    for i in range(longitud):
        password += random.choice(caracteres)

    return f"Tu nueva contraseña es: {password}"

# Ejemplo de uso:
longitud = int(input("Ingrese la longitud de la contraseña deseada: "))
nueva_password = generador_password(longitud)
print(nueva_password)