# EXAMEN TN - TEMA 1
# Pablo Agustin Galarza
# DNI: 43.171.637

# Usuarios vendedores de MercadoLibre
# Cargar 10 usuarios/vendedores de MercadoLibre con sus respectivas
# publicaciones.

# ● Los datos que se cargarán son:
# ● Nombre de usuario
# ● Edad (validar)
# ● Cantidad de productos (validar-número entero positivo).
# ● Número de publicaciones (validar-número entero positivo, hasta 1000).
# ● Tipo ("producto", "servicio", "subasta")
# ● Cuenta activa ("si", "no")

# Se necesita saber
# Tema A:
# 1. Cantidad de usuarios con la cuenta activa cuyo producto sea del tipo “producto”, cuya edad esté entre 25 y 35 años inclusive.
# 2. Nombre y tipo del usuario de menor edad con más de 500 publicaciones.
# 3. Porcentaje de publicaciones de tipo subasta.
# 4. Mostrar el promedio de edad de los usuarios cuyas publicaciones fueron del tipo “producto”.
# 5. Determinar el tipo con más publicaciones, cuya cuenta se encuentre “activa”.

# Variables
carga_usuarios = 0 
personas_edad_25_35 = 0
contador_de_subastas = 0
contador_usuarios_total = 0
acumulador_edades_producto = 0
comprador_producto = 0
nombre_menor_edad = None
tipo_menor_edad = None
edad_menor_edad = None
acumulador_publicaciones_producto = 0
publicaciones_servicio = 0
publicaciones_subasta = 0
tipo_maximo = None
max_publicaciones = 0

while carga_usuarios < 10:
    # ● Nombre de usuario
    nombre_de_usuario = input("Ingrese su nombre: ")
    while not nombre_de_usuario.isalpha(): # Validamos que el nombre solo contenga letras
        print("Nombre no válido")
        nombre_de_usuario = input("Ingrese de nuevo el nombre: ")

    # ● Edad (validar)
    edad_de_usuario = int(input("Ingrese su edad: "))
    while (edad_de_usuario <= 0):
        print("Edad no válida")
        edad_de_usuario = int(input("Ingrese de nuevo la edad: "))
    
    # ● Cantidad de productos (validar-número entero positivo).
    cantidad_de_productos = int(input("Ingrese la cantidad de productos: "))
    while (cantidad_de_productos < 0):
        print("Cantidad de productos no válida")
        cantidad_de_productos = int(input("Ingrese de nuevo la cantidad de productos: "))
        
    # ● Número de publicaciones (validar-número entero positivo, hasta 1000).
    numero_de_publicaciones = int(input("Ingrese el número de publicaciones: "))
    while (numero_de_publicaciones < 0) or (numero_de_publicaciones > 1000):
        print("Número de publicaciones no válido")
        numero_de_publicaciones = int(input("Ingrese de nuevo el número de publicaciones: "))
    
    # ● Tipo ("producto", "servicio", "subasta")
    tipo_de_producto = input("Tipo de producto: \n[1] Producto\n[2] Servicio\n[3] Subasta\nIngrese una opción: ")
    while (tipo_de_producto != "1") and (tipo_de_producto != "2") and (tipo_de_producto != "3"):
        tipo_de_producto = input("Tipo de producto: \n[1] Producto\n[2] Servicio\n[3] Subasta\nIngrese una opción: ")
    
    if tipo_de_producto == "1":
        tipo_de_producto = "producto"
        # Acumulamos edades para calcular promedio (PUNTO 4)
        acumulador_edades_producto += edad_de_usuario
        # Contamos los usuarios para calcular promedio de edad (PUNTO 4)
        comprador_producto += 1
        # Acumulamos publicaciones totales para saber el tipo con más publicaciones (PUNTO 5)
        acumulador_publicaciones_producto += numero_de_publicaciones
        
    elif tipo_de_producto == "2":
        tipo_de_producto = "servicio"
        publicaciones_servicio += numero_de_publicaciones
    else:
        tipo_de_producto = "subasta"
        contador_de_subastas += 1
        publicaciones_subasta += numero_de_publicaciones
    
    # ● Cuenta activa ("si", "no")
    cuenta_activa = input("Cuenta activa: \n[1] Sí\n[2] No\nIngrese una opción: ")
    while (cuenta_activa != "1") and (cuenta_activa != "2"):
        cuenta_activa = input("Cuenta activa: \n[1] Sí\n[2] No\nIngrese una opción: ")
    
    if cuenta_activa == "1":
        # Incrementamos el contador total de usuarios con cuenta activa
        contador_usuarios_total += 1
    
        # Contamos usuarios cuyo producto es del tipo "producto" y tienen entre 25 y 35 años inclusive
        if tipo_de_producto == "producto" and (edad_de_usuario >= 25) and (edad_de_usuario <= 35):
            personas_edad_25_35 += 1

        # Preguntamos si el número de publicaciones es mayor a 500 para calcular punto 2
        if numero_de_publicaciones > 500:
            # Y si se cumple que hay alguien con más de 500 publicaciones, guardamos los datos necesarios
            if (edad_menor_edad == None) or (edad_de_usuario < edad_menor_edad):
                edad_menor_edad = edad_de_usuario
                nombre_menor_edad = nombre_de_usuario
                tipo_menor_edad = tipo_de_producto

    carga_usuarios += 1

# INFORMES

# 1. Cantidad de usuarios con la cuenta activa cuyo producto sea del tipo “producto”, cuya edad esté entre 25 y 35 años inclusive.
print(f"La cantidad de usuarios con la cuenta activa y llevan un 'producto', cuya edad esté entre 25 y 35 años inclusive es de: {personas_edad_25_35} personas")

# 2. Nombre y tipo del usuario de menor edad con más de 500 publicaciones.
if nombre_menor_edad:
    print(f"Nombre y tipo del usuario de menor edad con más de 500 publicaciones: {nombre_menor_edad} ({tipo_menor_edad})")
else:
    print("No se encontró un usuario con más de 500 publicaciones.")

# 3. Porcentaje de publicaciones de tipo subasta.
#CALCULO TOTAL DE APLICACIONES
total_publicaciones = acumulador_publicaciones_producto + publicaciones_servicio + publicaciones_subasta
if total_publicaciones > 0:
    porcentaje_publi_subasta = (publicaciones_subasta * 100) / total_publicaciones
    print(f"El porcentaje de publicaciones de tipo subasta es de: {porcentaje_publi_subasta}%")
else:
    print("No hay publicaciones para calcular el porcentaje.")

# 4. Mostrar el promedio de edad de los usuarios cuyas publicaciones fueron del tipo “producto”.
if comprador_producto > 0:
    promedio_edad_usuarios_producto = acumulador_edades_producto / comprador_producto
    print(f"El promedio de edad de los usuarios cuyas publicaciones fueron del tipo 'producto' es de: {promedio_edad_usuarios_producto}")
else:
    print("No hubo compradores de productos")
    
# 5. Determinar el tipo con más publicaciones, cuya cuenta se encuentre “activa”.
if acumulador_publicaciones_producto > max_publicaciones:
    tipo_maximo = "producto"
    max_publicaciones = acumulador_publicaciones_producto
if publicaciones_servicio > max_publicaciones:
    tipo_maximo = "servicio"
    max_publicaciones = publicaciones_servicio
if publicaciones_subasta > max_publicaciones:
    tipo_maximo = "subasta"
    max_publicaciones = publicaciones_subasta

# Mostrar el tipo con más publicaciones
print(f"El tipo con más publicaciones, cuya cuenta se encuentre 'activa' es: {tipo_maximo}")