# TUPLAS
# mi_lista = [1, 2, 3]    # Lista -> Mutable
# mi_tupla = (1, 2, 3, 2) # Tupla -> Inmutable

# def test():
#     val_a = 5
#     val_b = 7
#     # tupla = (val_a, val_b)
#     return val_a, val_b # No recomendado

# a, b = test()
# print(a)
# print(b)

# for i in range(len(mi_tupla)):
#     print(mi_tupla[i])

#print(mi_tupla.index(4))

# mi_tupla = list(mi_tupla) # Tupla a lista
# mi_tupla[1] = 5 # le cambio un valor
# mi_tupla = tuple(mi_tupla) # lista a tupla
# print(mi_tupla)


# SETS

# mi_set = {1, 2, 3, 1}
# print(type(mi_set), mi_set)

# mi_lista = [1, 2, 3, "1"]
# mi_set = set(mi_lista)
# mi_set = list(mi_set)

# print(type(mi_set), mi_set)

# mi_set = {1, 2, 3, 1}
# mi_set.clear()
# print(mi_set)





# DICCIONARIOS
# Item -> Clave Unicas(str) y Valor (any)
# mi_diccionario = {
#     "nombre": "Val", 
#     "edad": 35,
#     "apellido": "Pavlov",
#     "fecha": {"dia": 28, "mes": "Octubre", "anio": 2024}
# } # No es indexable
# Imprimir el nombre:
# print(mi_diccionario['nombre'])
# print(mi_diccionario['edad'])
# print(mi_diccionario['apellido'])
# print(mi_diccionario["fecha"]["mes"])
#mi_diccionario["nombre"] = "Valeriy"

#print(mi_diccionario) # Prohibido 


# Recorrer claves.
# for clave in mi_diccionario.keys():
#     print(clave, mi_diccionario[clave])

# print("=========================================")

# # Recorrer valores.
# for valor in mi_diccionario.values():
#     print(valor)

# print("=========================================")

# # Recorre los items (clave y valor).
# for clave, valor in mi_diccionario.items():
#     print(clave, valor)

mi_diccionario = {
    "nombre": "Val", 
    "edad": 35,
    "apellido": "Pavlov",
    "fecha": {
        "dia": 28, 
        "mes": "Octubre", 
        "anio": 2024
        }
} # No es indexable

# En python tambien es valida esta forma.
for clave in mi_diccionario:
    print(clave, mi_diccionario[clave])

# print(mi_diccionario.get("edad"))
# print(mi_diccionario["edad"])

print(id(mi_diccionario))
# Update: actualiza el diccionario, si la clave existe, modifica el valor, si no existe agrega el item.
mi_diccionario.update({"nombre": "VALERIY"})
print(id(mi_diccionario))

# Pop: elimina un item, devolviendo el valor.
fecha_borrada = mi_diccionario.pop("fecha")
print(fecha_borrada)

for clave in mi_diccionario:
    print(clave, mi_diccionario[clave])