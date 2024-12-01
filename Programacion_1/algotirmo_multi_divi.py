def obtener_relaciones(lista, tipo):
    """
    Obtiene relaciones matemáticas de múltiplos o divisores entre los números de una lista.

    :param lista: Lista de números proporcionada por el usuario.
    :param tipo: String que especifica 'multiplos' o 'divisores'.
    :return: Lista de relaciones en forma de pares ordenados (a, b).
    """
    relaciones = []
    for a in lista:
        for b in lista:
            if tipo == "multiplos" and b != 0 and a % b == 0:
                relaciones.append((a, b))
            elif tipo == "divisores" and b != 0 and b % a == 0:
                relaciones.append((a, b))
    return relaciones

# Ejemplo de uso
lista_numeros = [2, 3, 12, 15, 24, 60]
tipo_relacion = "multiplos"  # O puede ser "divisores"
resultado = obtener_relaciones(lista_numeros, tipo_relacion)

# Mostrar el resultado
print(f"Relaciones de tipo '{tipo_relacion}': {resultado}")
