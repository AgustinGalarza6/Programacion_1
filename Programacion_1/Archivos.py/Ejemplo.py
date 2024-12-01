def ordenar_lista(funcion, lista):
    """Ordena una lista segun una funcion de comparacion"""
    lista.sort(key=funcion)
    return lista

def ordenar_por_longitud(cadena):
    return len(cadena)

palabras = ["manzana", "pera", "banana", "naranja"]
resultado = ordenar_lista(ordenar_por_longitud, palabras)
print(resultado)

mi_numero = 5
print((lambda numero: "Es par" if numero % 2 == 0 else "No es par")(5))