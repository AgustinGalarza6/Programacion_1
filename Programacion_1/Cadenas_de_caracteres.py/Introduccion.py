# Las cadenas de texto son indexcables, significa que podemos
#acceder a un elemento mediante el indice (posición: 0...5, etc)

saludo = "Hola mundo"  # INMUTABLE

# print(saludo[4])
# Por medio de esta indexacion mostraremos dentro del saludo la letra "m"

# Por ejemplo podemos extraer la letra "m" de la variable saludo

# letra_extraida = saludo[5]
# print(letra_extraida)

# En python como tal no existe SLICE pero podemos reemplazarlo por:
# Extraemos "mundo"    variable[DESDE : HASTA]

slice = saludo[5:10]
print(f"Extraje la palabra {slice}") 

slice2 = saludo[:4]
print(f"Extraje la palabra {slice2}")

# str + str -> concatenacion
# int + int -> suma
# list + list -> Union de listas
# str + int -> ERROR

saludo_parte_1 = "Hola "
saludo_parte_2 = "mundo!"
saludo_completo = saludo_parte_1 + saludo_parte_2
print(saludo_completo)

# f-string NO es concatenacion.

#saludo_completo = (f"{saludo_parte_1} {saludo_parte_2}")
# ESTO NO ES CONCATENACION

# str * int -> Repetición
lista = [None] * 5
# NONE NONE NONE NONE NONE


