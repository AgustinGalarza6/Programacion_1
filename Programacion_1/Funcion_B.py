def identificar_patente(patente):
    resultado = ""  # Inicializamos una variable para almacenar el resultado

    # Verificar si la longitud de la patente es 6 diditos
    if len(patente) != 6:
        resultado = "Formato de patente incorrecto"
    elif patente[:3].isalpha() and patente[3:].isdigit():
        resultado = "Esto es la patente de un auto"
    elif patente[:3].isdigit() and patente[3:].isalpha():
        resultado = "Esto es la patente de una moto"
    else:
        resultado = "Formato de patente no válido"

    return resultado

# Solicitar la patente al usuario
patente_usuario = input("Ingresa la patente (formato LLLNNN o NNNLLL): ")
print(identificar_patente(patente_usuario))


