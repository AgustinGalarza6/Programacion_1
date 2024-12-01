#lista = [1, 2, 3]
# print(id(lista))
# #lista += [4]
# print(id(lista))

# lista.append(4) # Agrega un elemento al final de la lista

# print(lista) # Prohibido!




# lista.insert(2, 4) # -> [1, 4, 2, 3].
# # lista_copia = []
# # for i in range(len(lista)): # 0, 1, 2, 3
# #     if i == 1:
# #         lista_copia += [4]
# #         lista_copia += [lista[i]]
# #     else:
# #         lista_copia += [lista[i]]

# print(lista) # Prohibido!



# lista.extend("Hola") 

# print(lista)


############################################################
lista = [1, 2, 3, 4, 5]
# Exceptions
try: # try (en otros lenguajes)
    lista.remove(6) # * Volvemos a este metodo en un momento.
except Exception as error: # catch (en otros lenguajes)
    print("Exploto", error)

#lista.remove(6) # * Volvemos a este metodo en un momento.
print(lista)




# retorno_del_pop = lista.pop(3) # * Volvemos a este metodo en un momento.

# print(lista)
# print(retorno_del_pop)


# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# indice_del_once = lista.index(4, 0, 9) # * Volvemos a este metodo en un momento.
# print(indice_del_once)
# print(lista)


# lista = [3, 1, 2]
# lista.sort(reverse=True)
# print(lista)


# lista = [3, 1, 2, 4, 5, 6]
# lista.reverse()
# print(lista)   # Prohibido!


# lista = [3, 1, 2, 4, 5, 6]
# print(id(lista))
# lista.clear()
# print(id(lista))
# print(lista)

# import copy

# # copia_lista = lista.copy() # Shallow Copy, no confundir con shadow copy, shower copy
# # copia_lista = lista[:] # Shallow copy
# # copia_lista = copy.copy(lista) # Shallow copy
# lista = [3, [1, 2], 4, 5, 6]
# copia_lista = copy.deepcopy(lista) # Deep copy / Copia profunda
# # for i in range(len(lista)):
# #     copia_lista += [lista[i]]

# lista[1][0] = 9
# print(id(lista[1]))
# print(id(copia_lista[1]))
# print(lista)
# print(copia_lista)
# print(id(lista))
# print(id(copia_lista))

lista = [3, 1, 7, 4, 5, 7, 3, 7]
# resultado = lista.count(7)

# print(f"El numero 7 aparece {resultado} veces.")