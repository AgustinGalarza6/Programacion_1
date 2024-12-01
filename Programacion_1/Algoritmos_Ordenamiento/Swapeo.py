# algoritmos de ordenamiento.

# son un conjunto de instrucciones que buscar organizar
# elementos en un orden particular

# Concepto de swapeo: Es una operacion de intercambio

lista = []

lista.sort() # Prohibido (organiza una lista)
print(lista) # Prohibido

numero_a = 5
numero_b = 7

# Swapeo

aux = numero_a
numero_a = numero_b
numero_b = aux

print(numero_a, numero_b) # 7, 5 (cambiamos el valor de la variable con un AUX)
print("-----------------------------------------------")


# Criterios de swapeo
# Ordenar lista de menor a mayor (Ascendente)
def ordenar_ascendente(lista:list) -> list:
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    print(lista)
    return lista

# ejemplo
lista = [5, 4, 3, 2, 1]
print("Lista vieja")
print(lista)
print("-----------------------------------------------")
print("Lista ordenada: ")
ordenar_ascendente(lista)



# Ordenar lista de mayor a menor (Descendente)
def ordenar_descendente(lista:list) -> list:
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] < lista[j]:
                # Para que haya un correcto swapeo deben usarse 2 veces cada variable
                # 2 aux, 2 lista[i], 2 lista[j]
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    print(lista)
    return lista

# ejemplo
lista = [5, 3, 4, 1, 2]
print("-----------------------------------------------")
print("Lista vieja")
print(lista)
print("-----------------------------------------------")
print("Lista ordenada: ")
ordenar_ascendente(lista)