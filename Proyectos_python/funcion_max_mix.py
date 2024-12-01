# Máximo de tres números:
# Desarrolla una función llamada maximo que reciba tres números como argumentos y devuelva el mayor de los tres.

# def valor_maximo(n1, n2, n3):
#     if n1 > n2 and n1 > n3:
#         numero_maximo = n1
#     elif n2 > n1 and n2 > n3:
#         numero_maximo = n2
#     else:
#         numero_maximo = n3
#     return f"El valor maximo es: {numero_maximo}"


# # Mínimo de tres números:
# # Desarrolla una función llamada minimo que reciba tres números como argumentos y devuelva el menor de los tres.

# def valor_minimo(n1:str, n2:str, n3:str)-> str:
#     if n1 < n2 and n1 < n3:
#         numero_minimo = n1
#     elif n2 < n1 and n2 < n3:
#         numero_minimo = n2
#     else:
#         numero_minimo = n3
#     return f"El valor minimo es: {numero_minimo}"


def hayar_max_min(n1, n2, n3, tipo='max'):
    if tipo == 'max':
        if n1 > n2 and n1 > n3:
            numero_extremo = n1
        elif n2 > n1 and n2 > n3:
            numero_extremo = n2
        else:
            numero_extremo = n3
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
# print(hayar_max_min(10, 20, 30, 'min' o 'max' dependiendo que valor quieras hayar.))