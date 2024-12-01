saludo = "hola amigo"

# ----------------------------------------------------------------------

# Upper

print(saludo.upper())
resultado = saludo.upper()
print("Ya aplique el upper")
# print(saludo, id(saludo))
# print(resultado, id(resultado))

# Pasa la cadena string todo a mayuscula

# ----------------------------------------------------------------------

# Lower

print(saludo.lower())
resultado = saludo.lower()
print("Ya aplique lower")
# print(saludo, id(saludo))
# print(resultado, id(resultado))

# Pasa la cadena string todo a minuscula

# ----------------------------------------------------------------------

# Capitalize

print(saludo.capitalize())
resultado = saludo.capitalize()
print("Ya aplique capitalize")
# print(saludo, id(saludo))
# print(resultado, id(resultado))

# Convierte la primera letra de la cadena en mayuscula
# Si la primera letra ya es mayuscula no hara nada
# Si el primer indice es un espacio no hara nada

# ----------------------------------------------------------------------

# Title

print(saludo.title())
resultado = saludo.title()
print("Ya aplique title")
# print(saludo, id(saludo))
# print(resultado, id(resultado))

# Convierte en mayusculas todas las primeras letras de cada palabra

# ----------------------------------------------------------------------

# Strip

print(saludo.strip())
resultado = saludo.strip()
print("Ya aplique strip")
# print(saludo, id(saludo))
# print(resultado, id(resultado))

# Quita los espacios en blanco de la cadena al principio y al final de una cadena
# Los espacios del medio los deja

# ----------------------------------------------------------------------

# Replace

print(saludo.replace("o", "@"))
resultado = saludo.replace("o", "@")
print("Ya aplique replace")

# ----------------------------------------------------------------------

# Split

print(saludo.split(" "))
resultado = saludo.split(" ")
print("Ya aplique split")

# Separa la cadena en listas de palabras separadas por un espacio
# Devuelve una lista de palabras

# ----------------------------------------------------------------------

# Join


lista_palabras = ["Pepe", "Juan", "Jose"]
resultado = "_".join(lista_palabras)
print(resultado)
print("Ya aplique join")

# Une colecciones de datos
# Devuelve una cadena


# ----------------------------------------------------------------------

# zfill

documento = "12345678"
resultado = documento.zfill(10)
print(resultado)
print("Ya aplique zfill")

# Completa una cadena de caracteres con ceros a la izquierda

# ----------------------------------------------------------------------

# isalnum

saludo5 = "hola 22"
resultado = saludo5.isalnum() # ¿La cadena es toda numerica? No
print(f"¿La cadena contiene solo numeros?: {resultado}") # False

# ----------------------------------------------------------------------

# isalpha

saludo6 = "hola"
resultado = saludo6.isalpha() # ¿La cadena es toda letra? Si
print(f"¿La cadena contiene solo letras?: {resultado}") # True

# ----------------------------------------------------------------------

# Count 

resultado = saludo.count("a")
print(f"El caracter 'a' aparece {resultado} veces en su cadena.")

# Cuenta las ocurrencias de algun caracter/combinacion de caracteres)

# ----------------------------------------------------------------------

# find

resultado = saludo.find("amigo")
print(f"El caracter 'amigo' se encuentra en la posicion: {resultado}")

# Busca el caracter ingresado en la cadena y devuelve la posicion de la primera ocurrencia

# ----------------------------------------------------------------------

# Center

resultado = saludo.center(50, "-")
print(resultado)

# Crea una cadena de caracteres con un numero de espacios en blanco a la izquierda y derecha.