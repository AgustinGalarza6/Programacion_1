lista = [1, 2, 3]

# Opcion anterior
# lista = [4]

# Opcion nueva
lista.append(4) # Añade un elemento al final de la lista (solo 1)
print(lista)

print("------------------------")

# Insert (A diferencia de append, insert agrega un elemento en una posicion determinada)

lista.insert(0, 8) 
# (posicion "indice", elemento nuevo)
print(lista)

# Insert casero

# lista_copia = []
# for i in range(len(lista)):
#     if i == 1:
#         lista_copia += [4]
#         lista_copia += [lista[i]]
#     else:
#         lista_copia += [lista[i]]
# print(lista_copia)

print("------------------------")

# Extend (A diferencia de append, extend es mejor aplicarlo para agregarle x cantidad de elementos)

lista.extend([5, 6, 7]) # Agrega elementos de una lista a la lista original
print(lista)

print("------------------------")

# Remove (Elimina un elemento de la lista)

lista.remove(8) # Elimina un elemento de la lista
# Si en la lista hay elementos iguales, se elimina solo el primero
print(lista)

print("------------------------")

# Pop (Elimina un elemento de la lista)

lista.pop() # Elimina el ultimo elemento de la lista
# Pop() no solo elimina el ultimo elemento, sino que retorna el indice del valor eliminado
# Pop() tambien tiene un retorno
# Por ejemplo:

retorno_del_pop = lista.pop(1)
print(lista)
print("Retorno del pop:",retorno_del_pop)

print("------------------------")

# Index (Nos da la posicion de un elemento en la lista)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)
indice_del_7 = lista.index(7)
print("El indice buscado es el:",indice_del_7)

# Si pasamos un index inexistente nos arroja un error, el index no existe

print("------------------------")

# Sort
# Los objetos de lista tienen un sort() método que ordenará la lista alfanuméricamente
# en orden ascendente, de forma predeterminada

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista.sort(reverse=True)
print(lista)

print("------------------------")

# Reverse

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista.reverse()
print(lista)

print("------------------------")

# Clear (Elimina todos los elementos de la lista)
lista.clear()
print(lista)

print("------------------------")

# Copy (Copia una lista)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_copia = lista.copy()
print("Lista original:",lista)
print("Lista copia:",lista_copia)

print("------------------------")

# Count (Cuenta cuantas veces aparece un elemento en la lista)

print("Lista original:",lista)
print(f"El elemento 2 aparece {lista.count(2)} vez")